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
#                           Time for a full turn
#
#
#                       #Queue list must contain the PID of each process that
#                           is being monitored dynamically
#
#
#******************************************************************************

#Control variables
sTime=125 #Time of each sleep run
cTime=30 #Time below which a change can take place in seconds / 10
pbs=restartCfdem.pbs
nNode=1
nHours=24

#Print process identification
echo "********************************************************"
echo "Starting process monitor"
echo "Processus PID : " $$
echo "********************************************************"

#Begin time looping
while true 
do

    newID=()

    #Read list of test to handle
    IFS=$'\r\n' GLOBIGNORE='*' :
    watchList=($(cat queueList))
   
    #Read list of variables that are needed for the update of dictionnaries
    propertiesList=($(cat queueProperties))
    timeStepCFD=(${propertiesList[0]})
    endCFD=(${propertiesList[1]})
    writeCFD=(${propertiesList[2]})
    timeStepDEM=(${propertiesList[3]})
    writeDEM=(${propertiesList[4]})
    timeTurn=(${propertiesList[5]})

    #Loop through all tasks
    for i in ${watchList[@]}
    do
        printf "\t Task: %s\n" $i
        #Check how much time is left to task
        tLeft=$(qstat -f $i | grep "Walltime.Remaining" | cut -c 26- )
        if (($tLeft>0))
        then
            printf "\t \t TimeLeft: %i\n" $tLeft
            if (($tLeft<$cTime))
            then
                 
                #Extract name of the case
                caseName=$(qstat -f $i | grep "Job_Name" | cut -c  16-)
                printf "\t \t Job Name: %s\n" $caseName

                #Extract the time step
                ls $caseName/CFD/processor0/ > temp   
                timeList=($(cat temp))
                maxTime=0
                for j in ${timeList[@]}
                do
                    timeMod=$(echo '('$j'%'$timeTurn") >0" | bc )
                    isLarger=$(echo '('$j'>'$maxTime')' | bc )

                    if (($timeMod==0))
                    then
                        if (($isLarger==1))
                        then
                            maxTime=$j
                        fi
                    fi
                done

                startCFD=$maxTime

            

                printf "\t \t Selected Time: %s\n" $maxTime
                
                # Change CFD Dict
                bash changeControlDict.sh $caseName/CFD/system $startCFD $endCFD $timeStepCFD $writeCFD

                IFS=$'_ ' GLOBINGORE='*' read -a lArg <<< "$caseName"
               
                speedL=$(echo 'scale=10; 60./' ${lArg[5]} | bc)


                liggghtsTime=$(echo "scale=6; time="$maxTime"/1 ; if (time < 1) { print \"0\"}; print time" | bc ) 
                
                liggghtsRestart=$(echo "liggghts.restartCFDEM_"$liggghtsTime)
                bash changeLIGGGHTS.sh $caseName/DEM $liggghtsRestart $timeStepDEM ${lArg[2]} ${lArg[3]} "1.0" "0.25" ${lArg[1]} $speedL $writeDEM



                printf "\t \t Sending the case\n" 
                #Modify number of nodes
                cat ./$pbs | sed 's/±/'$nNode'/' > $caseName/CFD/temp.pbs 
                                   
                cd $caseName/CFD
                #Modify allocated hours
                cat temp.pbs | sed 's/£££/'$nHours'/' >  temp2.pbs
                                                                        
                #Modify name of the job
                cat temp2.pbs | sed 's/¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦/'$caseName'/' > launch.pbs
                newTask=$(qsub launch.pbs)
                newID+=($newTask)
                printf "\t \t New Task started : %s\n" $newID
                cd ../../
            
            #Case if the task can be conitnued
            else
                printf "\t \t Task continues\n"
                newID+=($i)
            fi
        else
                printf "\t \t Task continues\n"
                newID+=($i)
        fi
        
    done
    echo "--------------------------------------------------------------"
    
    # Regenerate the queue list
    rm queueList
    touch queueList
    for i in ${newID[@]}
    do
       echo $i >> queueList
    done

    sleep $sTime
done
