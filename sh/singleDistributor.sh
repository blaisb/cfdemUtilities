root=$1
fname=$2

for D in $(find ./ -mindepth 1 -maxdepth 1 -type d) ; do
    echo $D ;
    cp $root/$fname $D/$fname
done
