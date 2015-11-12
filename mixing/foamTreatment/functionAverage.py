#------------------------------------------------------------------------------------------------------------
#
# This program contains function related to the post processing of OpenFOAM mixing results and other averaging for foam variables
# 
# Usage : Must be imported from another file
#
# Author : Bruno Blais
#
#-------------------------------------------------------------------------------------------------------------

# Python imports
#----------------
import numpy
import math
import re
#----------------

#Function variables
#-------------------
tol=1e-4
uLimit=10 #Limit for the velocities to prevent absurd results (sometime happens)
openFoamVersion="2.4"

#================================
#   FUNCTION
#================================

def getCoordFromLine(l):
    l_str = l.split(" ")
    a = [x for x in l_str if x != ""]
    y=[]
    for i,val in enumerate(a):
        if (i>=2):
            y.append(float(val))
    return numpy.array(y)

def getScalarFromLine(l):
    l_str = l.split(" ")
    a = [x for x in l_str if x != ""]
    y=[]
    for i,val in enumerate(a):
        if (i>=1):
            y.append(float(val))
    return numpy.array(y)

def getVectorFromLine(l):
    l=l.replace(")"," ")
    l=l.replace("("," ")
    
    l_str = l.split(" ")
    a = [x for x in l_str if x != ""]  

    u=[]
    v=[]
    w=[]

    for i in range(1,len(a)-1,3):
        u.append(float(a[i]))
        v.append(float(a[i+1]))
        w.append(float(a[i+2]))
        

    return numpy.array(u),numpy.array(v),numpy.array(w)


def scalarAverage(fname,impeller,impellerType):

    infile = open(fname,'r')


    if (openFoamVersion == "2.4"):
        print "Using openFoamVersion 2.4+ postprocessing" 
        readFile=True
        x=numpy.array([])
        y=numpy.array([])
        z=numpy.array([])
        while readFile:
            l=infile.readline()
            if (len(l) >1 and l[2]=="P"):
                        #print l
                        l_str=re.split(' |\(| |\)|',l)
                        x=numpy.append(x,float(l_str[-4]))
                        y=numpy.append(y,float(l_str[-3]))
                        z=numpy.append(z,float(l_str[-2]))
            else:
                readFile=False

        
    else:
    #Get the first three lines to get the x y z positions
        l=infile.readline()
        x=getCoordFromLine(l)
        l=infile.readline()
        y=getCoordFromLine(l)
        l=infile.readline()
        z=getCoordFromLine(l)

#Transform the x y z positions to r t z
    r = numpy.sqrt(x*x+y*y)
    theta = numpy.arctan2(y,x)

    #Remove useless buffer line
    l=infile.readline()

#Count number of different radiuses
    rr=-1
    nr=0
    rl=[]
    z0=z[0]
    for ind,i in enumerate(r) :
        if (abs(z[ind]-z0)>tol):break # Don't want to count nr * nz instead of nr
        if (abs(i-rr)>tol): 
            rr=i
            rl.append(rr)
            nr+=1
    rr=-1
    zl=[]
    nz=0
    for i in z :
        if (abs(i-rr)>tol): 
            rr=i
            nz+=1
            zl.append(rr)

    #Acquire the scalar vector associated with each position
    l=infile.readline()
    s=getScalarFromLine(l)

    #clean the scalar
    for i in range(1,len(s)):
       if (abs(s[i])>1e5): s[i]=s[i-1]

    #Averaging procedure
    acc=numpy.zeros([nz,nr])
    acc2=numpy.zeros([nz,nr])    
    j=0
    k=0
    count=0
    pR=r[0]
    pZ=z[0]
    temp=0
    temp2=0
    for i in range(0,len(z)):
        if (abs(r[i]-pR)>tol):
            count=max(count,1)
            acc[k,j]=temp/float(count)
            acc2[k,j]=temp2/float(count)            
            j+=1
            count=0
            pR=r[i]
            temp=0.
            temp2=0.

        if (abs(z[i]-pZ)>tol):
            pZ=z[i]
            j=0
            k+=1

        temp+=s[i]
        temp2+=s[i]*s[i]
        count+=1
        if (i ==(len(z)-1)):
            acc[k,j]=temp/count
            acc2[k,j]=temp2/float(count)
            
    var = acc2-acc**2
    dev = numpy.sqrt(var+1e-12)

    if (impeller):
        for i in range(0,len(rl)):
            for j in range(0,len(zl)):
                    rr=rl[i]
                    zz=zl[j]
                    if(impellerType=="pbtTs3"):
                        if (zz>0.1471):
                            if (rr<0.0127):
                                acc[j,i]=numpy.nan
                                dev[j,i]=numpy.nan
                        elif (zz>0.121667):
                            if (rr<0.0191):
                                acc[j,i]=numpy.nan
                                dev[j,i]=numpy.nan
                    if(impellerType=="pbtTs4"):
                        if (zz>0.1168):
                            if (rr<0.0127):
                                acc[j,i]=numpy.nan
                                dev[j,i]=numpy.nan
                        elif (zz>0.09125):
                            if (rr<0.0191):
                                acc[j,i]=numpy.nan
                                dev[j,i]=numpy.nan

    return rl,zl,acc,dev

def vectorAverage(fname,impeller,impellerType):

    infile = open(fname,'r')
   
    #Get the first three lines to get the x y z positions
    l=infile.readline()
    x=getCoordFromLine(l)
    l=infile.readline()
    y=getCoordFromLine(l)
    l=infile.readline()
    z=getCoordFromLine(l)

    #Transform the x y z positions to r t z
    r = numpy.sqrt(x*x+y*y)
    theta = numpy.arctan2(y,x)

    #Remove useless buffer line
    l=infile.readline()

    #Count number of different radiuses
    rr=-1
    nr=0
    rl=[]
    z0=z[0]
    for ind,i in enumerate(r) :
        if (abs(z[ind]-z0)>tol):break # Don't want to count nr * nz instead of nr
        if (abs(i-rr)>tol): 
            rr=i
            rl.append(rr)
            nr+=1
    rr=-1
    zl=[]
    nz=0
    for i in z :
        if (abs(i-rr)>tol): 
            rr=i
            nz+=1
            zl.append(rr)


    #Acquire the U V and W vector associated with each position
    l=infile.readline()
    u,v,w=getVectorFromLine(l)

    #clean the velocities
    for i in range(1,len(u)):
        if (abs(u[i])>uLimit): u[i]=u[i-1]
        if (abs(v[i])>uLimit): v[i]=v[i-1]
        if (abs(w[i])>uLimit): w[i]=w[i-1]

    ur =   numpy.cos(theta)*u + numpy.sin(theta)*v
    ut = - numpy.sin(theta)*u + numpy.cos(theta)*v

    #Averaging procedure
    acc=numpy.zeros([nz,nr,3])
    j=0
    k=0
    count=0
    pR=r[0]
    pZ=z[0]
    temp=numpy.array([0.,0.,0.])
    for i in range(0,len(z)):
        if (abs(r[i]-pR)>tol):
            count=max(count,1)
            acc[k,j]=temp/count
            j+=1
            count=0
            pR=r[i]
            temp=numpy.array([0.,0.,0.])

        if (abs(z[i]-pZ)>tol):
#            acc[j,k]=temp/count
            pZ=z[i]
            j=0
            k+=1

        temp[0]+=ur[i]
        temp[1]+=ut[i]
        temp[2]+=w[i]
        count+=1
        if (i ==(len(z)-1)): acc[k,j]=temp/count

    # Remove the swept volume of the impeller
    if (impeller):
        for i in range(0,len(rl)):
            for j in range(0,len(zl)):
                    rr=rl[i]
                    zz=zl[j]
                    if(impellerType=="pbtTs3"):
                        if (zz>0.1471):
                            if (rr<0.0127):
                                acc[j,i,:]=numpy.nan
                        elif (zz>0.121667):
                            if (rr<0.0191):
                                acc[j,i,:]=numpy.nan
                    if(impellerType=="pbtTs4"):
                        if (zz>0.1168):
                            if (rr<0.0127):
                                acc[j,i,:]=numpy.nan
                        elif (zz>0.09125):
                            if (rr<0.0191):
                                acc[j,i,:]=numpy.nan


    return rl,zl,acc
