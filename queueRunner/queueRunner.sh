#******************************************************************************
#
#       Program : pbsRunner
#
#       Author  : Bruno Blais
#
#       Description : This program monitors the pbs queue and restarts
#                       a submission once it is over to keep the task running
#
#                       #Queue properties must be put in the following order
#                           CFD timestep
#                           CFD endTime
#                           CFD writeTime 
#                           DEM timestep
#                           DEM writeTimeStep
#
#
#
#******************************************************************************

#Control variables
sTime=1


#Print process identification
echo "********************************************************"
echo "Starting process monitor"
echo "Processus PID : " $$
echo "********************************************************"

#Begin time looping
while true 
do

    #Read list of test to handle
    IFS=$'\r\n' GLOBIGNORE='*' :
    watchList=($(cat queueList))
    propertiesList=($(cat queueProperties))
    timeStepCFD=(${propertiesList[0]})
    endCFD=(${propertiesList[1]})
    writeCFD=(${propertiesList[2]})
    timeStepDEM=(${propertiesList[3]})
    writeDEM=(${propertiesList[4]})

    #Loop through all tasks
    for i in ${watchList[@]}
    do
        printf "\t Task: %s\n" $i
        qstat -f $i | grep "Walltime.Remaining" 
    done

    sleep $sTime
done
