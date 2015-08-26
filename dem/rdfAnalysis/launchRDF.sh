#******************************************************************************
#
# Bash script to launch the single rdf analysis of a particle
#
# Author : Bruno Blais
#
#******************************************************************************


liggghts="/usr/bin/liggghts3"
utils=$HOME/utils/cfdemUtilities/dem/rdfAnalysis
script=in.restartMeasureRDF


if [ "$#" != "3" ]; then
    echo "This script takes a single file argumentand an output folder argument, it will now crash..."
fi

file=$1
outputFolder=$2
outputFile=${outputFolder}/${file}"_rdf"
bin=$3

#Modify the data file 
cat $utils/$script | sed 's|@@|'$file'|' | sed 's|££|'$outputFile'|' | sed 's|¢¢|'$bin'|' > ./in.temp

mpirun -np 4 $liggghts < ./in.temp  > logLIGGGHTS

rm ./in.temp

