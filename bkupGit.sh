LIGGGHTS="/home/bruno/LIGGGHTS3/LIGGGHTS-PUBLIC"
CFDEM="/home/bruno/CFDEM/CFDEM-2.6-OF-2.2.1"


#echo "Tar of LIGGGHTS git"
#tar czf /home/bruno/gitTemp/LIGGGHTS.tar.gz $LIGGGHTS/.git 

#echo "Tar of CFDEM git"
#tar czf /home/bruno/gitTemp/CFDEM.tar.gz $CFDEM/.git 

echo "Tar backup of my Phd Folder"
tar czf /home/bruno/gitTemp/doctorat.tar.gz /media/bruno/DATA/Doctorat/

echo "Tar backup of utilities"
tar czf /home/bruno/gitTemp/utilities.tar.gz $HOME/utilities 

bsendf.sh /home/bruno/gitTemp

