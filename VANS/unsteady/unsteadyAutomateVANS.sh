#This script runs the circle test case for different mesh refinement level in order to compute the evolution of the L2 norm error as a function of the mesh
BC_LINE_LENGTH=10

case="finalVANS"
#rm L2Error.dat

tref=5
#rm -r ./$case/*



for i in  120 140 160 180 
do
    t=`echo "$tref/$i" | bc  -l`
    echo Time step value is $t

    echo "Creating blockMeshDict with number of element: "$i

    cd CFD
    cat ./constant/polyMesh/blockMeshDict.master | sed 's/@/'$i'/' > ./constant/polyMesh/blockMeshDict
    blockMesh >../logBlock

    echo "Modifying runtime Dictionnary to adapt time step in order to keep constant CFL"
    cat ./system/controlDict.master | sed 's/@/'$t'/' > ./system/controlDict


    echo "Start simulation"
    cfdemSolverVANS > ../logSim
    
    echo "Reconstruct positions"
    writeCellCentres > ../cellWriter
        
    cd ..
    mkdir U
    python getVelocitiesFOAM.py
    python automateL2ErrorVANS.py U/U_9 $i >> L2Error.dat
    mv U $case/U_$i

done
