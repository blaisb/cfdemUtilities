case=$1
baffles=false
convert=false

# Loop through all of the shell's arguments
for var in "$@"
do
    if [ "$var" == "baffles" ];
    then
        baffles=true
    fi
    if [ "$var" == "convert" ];
    then
        convert=true
    fi
done

if $convert;
then
    python $HOME/liggghts/lpp/src/lpp.py $case/DEM/post/mixerC* -o $case/DEM/post/mixer_
fi

rm $case/DEM/post/*bound*
mkdir $case/DEM/post/VTK
mv $case/DEM/post/*.vtk $case/DEM/post/VTK/
cp $case/DEM/post/*.stl $case/DEM/post/VTK/

if $baffles;
then
    cp ~/cfdem/cfdemUtilities/paraview/mixerParticlesBaffles.py $case/DEM/
else
    cp ~/cfdem/cfdemUtilities/paraview/mixerParticles.py $case/DEM/
fi

