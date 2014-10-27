name=$1
time=$2
proc=$3
n=$4
e=$5


echo $name
echo $time
echo $n
echo $e
echo ----------------------------------- 
echo Starting $name'_'$time'_'$n'e'$e
echo -----------------------------------

echo Using Mesh : L4_M$n'e'$e.des 
#MESH Make
/netdata/neptune/NEPTUNE_CFD/neptcfd-1.2.1/arch/calibre7/libexec/code_saturne/cs_preprocess --log --out mesh_input /netdata/blais/WORK/toto/MESH/L4_M$n'e'$e.des 

echo Mesh is made
echo Using $proc processors
mpiexec.openmpi -n $proc ./nc_solver --param tube.xml --mpi  
grep Elapsed listing 
grep Elapsed listing > time

echo Saving transient data
cp ./postprocessing/* /home/blais/resu/$name/$time/$n'e'$e/data/
cp ./time /home/blais/resu/$name/$time/$n'e'$e/

echo Saving CFL data
grep "Courant max" listing > Courant
grep "Cou_Fou max" listing > Cou_Fou
cp ./Courant /home/blais/resu/$name/$time/$n'e'$e/
cp ./Cou_Fou /home/blais/resu/$name/$time/$n'e'$e/



cp -r ./checkpoint ./restart		     
echo Restart sim for data with 1 processor
mpiexec.openmpi -n 1 ./nc_solver --param tubefin.xml --mpi  
echo Sim over $name'_'$time'_'$n'e'$e
rm -r ./restart

echo Saving results
grep 'Write' listing > output
grep 'xorg->' listing | cut -c 8- >> output
cp ./output /home/blais/resu/listrun/$name'_'$time'_'$n'e'$e'.dat'

echo Finished $name'_'$time'_'$n'e'$e


