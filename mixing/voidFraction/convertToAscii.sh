utils=$HOME/utils/cfdemUtilities/

cp $utils/foam/controlDictToAscii ./system/controlDict

foamFormatConvert
writeCellCentres
writeCellVolumes
