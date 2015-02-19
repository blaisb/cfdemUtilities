
label="caa"
directory="pressureLogs"
briaree=true
colosse=false


if [ -d "$directory" ]; then
    echo "Logs directory is already present, cleaning it now"
    rm $directory/*
else
    echo "Directory does not exist already"
    mkdir $directory
fi


declare -a arr=(\
$label"_1_1e7_0.05_164440_50" \
$label"_1_1e7_0.05_164440_100" \
$label"_1_1e7_0.05_164440_150" \
$label"_1_1e7_0.05_164440_200" \
$label"_1_1e7_0.05_164440_250" \
$label"_1_1e7_0.05_164440_300" \
$label"_1_1e7_0.05_164440_350" \
$label"_1_1e7_0.05_164440_400" \
$label"_1_1e7_0.05_164440_450" \
$label"_1_1e7_0.05_164440_500" \
)

declare -a arr=(\
"caa_1_1e7_0.05_164440_50" \
"caa_1_1e7_0.05_164440_100" \
"caa_1_1e7_0.05_164440_150" \
"caa_1_1e7_0.05_164440_200" \
"daa_1_1e7_0.05_164440_250" \
"caa_1_1e7_0.05_164440_300" \
"daa_1_1e7_0.05_164440_350" \
"caa_1_1e7_0.05_164440_400" \
"daa_1_1e7_0.05_164440_450" \
"daa_1_1e7_0.05_164440_500" \
)


## Loop through the briaree array
if $briaree
then
    for i in "${arr[@]}"
    do
        echo "$i"
        bgetf.sh /RQusagers/blaisbru/work/runs/mixing/cfdemPbt/$i/CFD/postProcessing/pressureBottom $directory/$i
    done

    mv $directory/daa_1_1e7_0.05_164440_250 $directory/caa_1_1e7_0.05_164440_250
    mv $directory/daa_1_1e7_0.05_164440_350 $directory/caa_1_1e7_0.05_164440_350
    mv $directory/daa_1_1e7_0.05_164440_450 $directory/caa_1_1e7_0.05_164440_450
    mv $directory/daa_1_1e7_0.05_164440_500 $directory/caa_1_1e7_0.05_164440_500

fi



#mkdir $case
#mv results/* $case/

