#!/usr/bin/python
"""
A simple routine to load in a LIGGGHTS hybrid dump file containing
contact and contact force data and convert into a .vtk unstructured
grid which can be used to visualise the force network.

evtk is used to write binary VTK files:
https://bitbucket.org/pauloh/pyevtk

The pizza.py bdump command is used to handle LIGGGHTS dump files and
therefore PYTHONPATH must include the pizza/src location.

NOTE: bdump is NOT included in granular pizza, and should be taken
from the standard LAMMPS pizza package!

NOTE: it is impossible to tell from the bdump header which values
have been requested in the compute, so check that your compute
and dump match the format here - this will be checked in future!

"""

from evtk.vtk import VtkFile, VtkGroup, VtkUnstructuredGrid
from bdump import bdump
import numpy as np
import sys, os

# TODO: use a try/except here to check for missing modules, and fallback to ASCII VTK if evtk not found
# TODO: ask for timestep or timestep range as input (code is NOT efficient and large files = long runtimes!)
# TODO: write celldata for contact area and heat flux (if present)

# Check for command line arguments
if len(sys.argv) != 2:
        sys.exit('Usage: dump2forcenetwork.py <filename>, where filename is typically dump.<runname>')
        
elif len(sys.argv) == 2: # we have one input param, that should be parsed as a filename
    filename = str(sys.argv[1])
    if not os.path.isfile(filename):
        sys.exit('File ' + filename + ' does not exist!')

splitname = filename.split('.')

if len(splitname) == 2 and splitname[0].lower() == 'dump':
    fileprefix = splitname[1]
else:
    fileprefix = splitname[0]

inputpath = os.path.abspath(filename)
inputdir = os.path.split(inputpath)[0]

# create a sub-directory for the output .vtu files
outputdir = os.path.join(inputdir,fileprefix)
try:
    os.mkdir(outputdir)
except:
    pass

# Read in the dump file - since we can have many contacts (i.e. >> nparticles)
# and many timesteps I will deal with one timestep at a time in memory,
# write to the appropriate .vtu file for a single timestep, then move on.

forcedata = bdump(filename,0)

groupfile = fileprefix
groupfile = os.path.join(inputdir,groupfile)
groupfile = VtkGroup(groupfile)

fileindex = 0
timestep = forcedata.next()

# check that we have the right number of colums (>11)
#
# NOTE: the first timesteps are often blank, and then natoms returns 0, so this doesn't really work...
#
if forcedata.snaps[fileindex].natoms !=0 and len(forcedata.snaps[0].atoms[0]) < 12:
    print "Error - dump file requires at least all parameters from a compute pair/gran/local id pos force (12 in total)"
    sys.exit()

# loop through available timesteps
# 
while timestep >= 0:

    # default data are stored as pos1 (3) pos2 (3) id1 id2 periodic_flag force (3) -> 12 columns
    #
    # if contactArea is enabled, that's one more (13) and heatflux (14)
    #
    # assign names to atom columns (1-N)
    forcedata.map(1,"x1",2,"y1",3,"z1",4,"x2",5,"y2",6,"z2",7,"id1",8,"id2",9,"periodic",10,"fx",11,"fy",12,"fz")
    # forcedata.map(1,"x1",2,"y1",3,"z1",4,"x2",5,"y2",6,"z2",7,"id1",8,"id2",9,"periodic",10,"fx",11,"fy",12,"fz",13,"area",14,"heatflux")

    # check for contact data (some timesteps may have no particles in contact)
    #
    # NB. if one loads two datasets into ParaView with defined timesteps, but in which
    # one datasets has some missing, data for the previous timestep are still displayed - 
    # this means that it is better here to generate "empty" files for these timesteps.

    if forcedata.snaps[fileindex].natoms == 0:   
        vtufile = fileprefix+'_'+str(timestep)+'.vtu'
        vtufile = os.path.join(outputdir,vtufile)
        vtuwrite = file(vtufile,'w')
        vtuwrite.write("""<?xml version="1.0"?>
<VTKFile byte_order="LittleEndian" version="0.1" type="UnstructuredGrid">
<UnstructuredGrid>
        <Piece NumberOfCells="0" NumberOfPoints="0">
                <Cells>
                        <DataArray NumberOfComponents="1" offset="0" type="Int64" Name="connectivity"/>
                        <DataArray NumberOfComponents="1" offset="0" type="Int64" Name="offsets"/>
                        <DataArray NumberOfComponents="1" offset="0" type="Int64" Name="types"/>

                </Cells>
        </Piece>
</UnstructuredGrid>
</VTKFile>""")
        
    else:

        # number of cells = number of interactions (i.e. entries in the dump file)
        ncells = len(forcedata.snaps[fileindex].atoms)

        # number of periodic interactions
        periodic = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names["periodic"]],dtype=bool)
        nperiodic = sum(periodic)

        # number of non-periodic interactions (which will be written out)
        nconnex = ncells - nperiodic

        # extract the IDs as an array of integers
        id1 = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names["id1"]],dtype=long)
        id2 = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names["id2"]],dtype=long)

        # and convert to lists
        id1 = id1.tolist()
        id2 = id2.tolist()

        # concatenate into a single list
        ids = []
        ids = id1[:]
        ids.extend(id2)

        # convert to a set and back to remove duplicates, then sort
        ids = list(set(ids))
        ids.sort()

        # number of points = number of unique IDs (particles)
        npoints = len(ids)

        # create empty arrays to hold x,y,z data
        x = np.zeros( npoints, dtype=np.float64)
        y = np.zeros( npoints, dtype=np.float64)
        z = np.zeros( npoints, dtype=np.float64)

        print 'Timestep:',str(timestep),'npoints=',str(npoints),'ncells=',str(ncells),'nperiodic=',nperiodic

        # Point data = location of each unique particle
        #
        # The order of this data is important since we use the position of each particle
        # in this list to reference particle connectivity! We will use the order of the 
        # sorted ids array to determine this.

        counter = 0   
        for id in ids:
            if id in id1:
                index = id1.index(id)
                xtemp,ytemp,ztemp = forcedata.snaps[fileindex].atoms[index,forcedata.names["x1"]], \
                        forcedata.snaps[fileindex].atoms[index,forcedata.names["y1"]], \
                        forcedata.snaps[fileindex].atoms[index,forcedata.names["z1"]]
            else:
                index = id2.index(id)
                xtemp,ytemp,ztemp = forcedata.snaps[fileindex].atoms[index,forcedata.names["x2"]], \
                        forcedata.snaps[fileindex].atoms[index,forcedata.names["y2"]], \
                        forcedata.snaps[fileindex].atoms[index,forcedata.names["z2"]]
            
            x[counter]=xtemp
            y[counter]=ytemp
            z[counter]=ztemp           
            counter += 1

        # Now create the connectivity list - this corresponds to pairs of IDs, but referencing
        # the order of the ids array, so now we loop through 0..ncells and have to connect 
        # id1 and id2, so I need to see where in ids these correspond to

        # If the periodic flag is set for a given interactions, DO NOT connect the points
        # (to avoid lines that cross the simulation domain)
            
        # Mask out periodic interactions from the cell (connectivity) array
        # newList = [word for (word, mask) in zip(s,b) if mask]
        id1_masked = [ident for (ident,mask) in zip(id1,np.invert(periodic)) if mask]
        id2_masked = [ident for (ident,mask) in zip(id2,np.invert(periodic)) if mask]

        # create an empty array to hold particle pairs
        connections = np.zeros( 2*nconnex, dtype=int )

        for pair in range(nconnex):
            connections[2*pair],connections[2*pair+1] = ids.index(id1_masked[pair]),ids.index(id2_masked[pair])
            
        # The offset array is simply generated from 2*(1..ncells)
        offset=(np.arange(nconnex,dtype=int)+1)*2

        # The type array is simply ncells x 3 (i.e. a VTKLine type)
        celltype = np.ones(nconnex,dtype=int)*3

        # Finally we need force data for each cell
        force = np.sqrt( np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names["fx"]],dtype=np.float64)**2 + \
                         np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names["fy"]],dtype=np.float64)**2 + \
                         np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names["fz"]],dtype=np.float64)**2 )

        # And, optionally, contact area and heat flux (using the same connectivity)
        # area = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names["area"]],dtype=np.float64)
        # heatflux = np.array(forcedata.snaps[fileindex].atoms[:,forcedata.names["heatflux"]],dtype=np.float64)

        # Now we have enough data to create the file:
        # Points - (x,y,z) (npoints)
        # Cells
        #   Connectivity - connections (nconnex,2)
        #   Offset - offset (nconnex)
        #   type - celltype (nconnex)
        # Celldata
        #   force    (nconnex)
        #   area     (nconnex)
        #   heatflux (nconnex)

        # create a VTK unstructured grid (.vtu) file
        vtufile = fileprefix+'_'+str(timestep)
        vtufile = os.path.join(outputdir,vtufile)
        w = VtkFile(vtufile, VtkUnstructuredGrid)
        vtufile += '.vtu'

        w.openGrid()
        w.openPiece(npoints=npoints, ncells=nconnex)

        # Set up Points (x,y,z) data XML
        w.openElement("Points")
        w.addData("points", (x,y,z) )
        w.closeElement("Points")

        # Set up Cell data
        w.openElement("Cells")
        w.addData("connectivity", connections )
        w.addData("offsets", offset)
        w.addData("types", celltype)
        w.closeElement("Cells")

        # Set up force data
        w.openData("Cell")
        w.addData("force", force)
        # w.addData("area", area)
        # w.addData("heatflux", heatflux)
        w.closeData("Cell")

        # and contact area
        # w.openData("Cell", scalars = "area")
        # w.addData("area", area)
        # w.closeData("Cell")

        # and heat flux
        # w.openData("Cell", scalars = "heatflux")
        # w.addData("heatflux", heatflux)
        # w.closeData("Cell")

        # Wrap up
        w.closePiece()
        w.closeGrid()

        # Append binary data
        w.appendData( (x,y,z) )
        w.appendData(connections).appendData(offset).appendData(celltype)
        # w.appendData(force).appendData(area).appendData(heatflux)
        w.appendData(force)
        w.save()

    # Add this file to the group of all timesteps
    groupfile.addFile(filepath = os.path.relpath(vtufile,inputdir), sim_time = timestep)

    fileindex += 1
    timestep = forcedata.next()

# end of main loop - close group file
groupfile.save()

