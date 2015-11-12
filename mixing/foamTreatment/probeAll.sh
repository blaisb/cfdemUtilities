#******************************************************************************
#
#  This programes carries out the probeLocation analysis for all the files
#   with the same prefix case
#
#   Usage : bash probeAll rootName
#
#   Author : Bruno Blais
#
#******************************************************************************
if [ $# -ne 1 ]
then
        echo "A case argument need to be entered"
fi
case=$1
subPath="CFD/resultsCFD"
origin=$(pwd)
cfdemUtilities="$HOME/cfdem/cfdemUtilities/"

for i in $(ls | grep $case)
do
    
    cd ./$i/$subPath
    pwd
    python $cfdemUtilities/mixing/foamTreatment/createProbePoints.py ./system/probesDict
    probeLocations -latestTime
    cd $origin
done
