case=$1

python $HOME/LIGGGHTS3/mylpp/src/lpp.py $case/DEM/post/couetteC* -o $case/DEM/post/couette_

rm $case/DEM/post/*bound*

cp couette_1000.stl $case/DEM/post/
cp ~/utilities/paraview/couetteParticles.py $case/DEM/

