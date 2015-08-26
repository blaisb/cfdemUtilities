#******************************************************************************
#
# Bash script to launch the rdf analysis of multiple files
#
# Author : Bruno Blais
#
#******************************************************************************

bin=200
utils=$HOME/utils/cfdemUtilities/dem/rdfAnalysis
script=launchRDF.sh

if [ "$#" != "1" ]; then
    echo "This script takes a folder argument, it will now crash..."
fi

folder=$1
cd $folder

for i in $(ls *000)
do
    echo $i
    bash $utils/$script $i . $bin 
done

cd ..

