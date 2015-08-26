for i in $(ls | grep processor); do
    cd $i
    foamToVTK
    cd ..
done
