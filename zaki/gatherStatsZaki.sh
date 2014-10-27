# This program gathers the results of the specifies cases and launches the time averager
CASE="main_sedimentation"
N1=1000000		    # Initial timestep for average
N2=3000000		    # Final cut for average
RESULTS="output"	    # Folder must have been previously created
FINALFILE="caseZakiResults" #

rm $RESULTS/*
for i in 2 3 4 5 6 7 8 9
do
    python ./timeAvgZaki.py $CASE$i $i $N1 $N2
    cat $CASE$i"Avg" >> ../total
done
