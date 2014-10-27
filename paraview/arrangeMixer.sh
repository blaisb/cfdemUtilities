case=$1

python $HOME/LIGGGHTS3/mylpp/src/lpp.py $case/DEM/post/mixerC* -o $case/DEM/post/mixer_

rm $case/DEM/post/*bound*

cp ~/utilities/paraview/mixerParticles.py $case/DEM/

