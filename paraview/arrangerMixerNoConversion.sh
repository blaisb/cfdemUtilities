case=$1

#python $HOME/LIGGGHTS3/mylpp/src/lpp.py $case/DEM/post/mixerC* -o $case/DEM/post/mixer_

rm $case/DEM/post/VTK/*bound*

cp ~/utils/cfdemUtilities/paraview/mixerParticles.py $case/DEM/

