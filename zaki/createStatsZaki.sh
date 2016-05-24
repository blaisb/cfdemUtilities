# This programs launches the Python script for all the cases
# Specify the case-name and the particle numbers (i in ...) and launch the program. This is parallel
CASE=main_sedimentation


for i in 2 3 4 5 6 7 8 9
do
    cd $CASE$i
    cp ../statsZaki.py ./
    python ./statsZaki.py $CASE$i &
    cd ..
done
