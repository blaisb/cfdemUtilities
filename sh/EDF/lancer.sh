#DONNÉES UTILISATEUR

#Nombre de processeurs
name='SOD'
time='dte-8'
proc=4;




for e in 2 3 4  
do 
	if [ $e -eq 2 ]; then
		for n in 1 
		do
		./executeur.sh $name $time $proc $n $e
		done
	fi
	if [ $e -eq 3 ]; then
		for n in 1 
		do
		./executeur.sh $name $time $proc $n $e
		done
	fi
	if [ $e -eq 4 ]; then
		for n in  1 2 3
		do
		./executeur.sh $name $time $proc $n $e
		done
	fi
	if [ $e -eq 5 ]; then
		for n in 1
		do
		./executeur.sh $name $time $proc $n $e
		done
	fi


done





