#------------------------------------------------------------------------------
#
#       This program concatenates files obtained via the force analysis of
#           Openfoam
#       
#
#       Usage : concatPostForces.sh $ROOTFOLDER
#
#
#       Author : Bruno Blais
#
#
#
#------------------------------------------------------------------------------

folder=$1
first=true

for i in $(ls $folder)
do
    if $first
    then
        first=false
        cat $folder/$i/forces.dat > $folder/forces.dat        
    else
        tail -n+4 $folder/$i/forces.dat >> $folder/forces.dat
    fi
    echo $i
done
