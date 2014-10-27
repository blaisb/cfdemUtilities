
#template directory
TEMPLATE="main_sedimentation" #directory of the template file
WORKDIR="sent/sedimentation" #directory of the workers
INIT_FILE="in.liggghts_init" #initialisation file for LIGGGHTS, where we change number of particles

#1000 10000 19000 3800 76500 95000 190000 382000 573000 764000 955000
for np in 1000 22222  # put the numbers of particles here manually
do
	#Names of sub-folder 
	NEW_WORK=$WORKDIR"_"$np
	
	#shoutout
	echo "Creating new working directory for "$np
    
	#create new working folder
	mkdir $NEW_WORK
	cp -r $TEMPLATE/* $NEW_WORK/
	

	echo "Modifying number of particles in " $INIT_FILE
        cat $NEW_WORK/DEM/$INIT_FILE | sed 's/??????????/'$np'/' > $NEW_WORK/DEM/temp #change number of particles
	cp $NEW_WORK/DEM/temp $NEW_WORK/DEM/$INIT_FILE #replace original file
done
