#This script runs the circle test case for different mesh refinement level in order to compute the evolution of the L2 norm error as a function of the mesh

case="nonFreeDiv"
#rm L2Error.dat

#rm -r ./$case/*

for i in 20 24 30 40 50 60 70 80 100 # 120 140 160 180 
do

    echo "Creating blockMeshDict with number of element: "$i

    cd CFD
    cat ./constant/polyMesh/blockMeshDict.master | sed 's/@/'$i'/' > ./constant/polyMesh/blockMeshDict
    blockMesh >../logBlock

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
