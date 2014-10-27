root=$1

for D in $(find ./ -mindepth 1 -maxdepth 1 -type d) ; do
    echo $D ;

    #========================
    #	DEM
    #========================
    echo "DEM"

    str=DEM/in.liggghts_resume
    cp $root/$str $D/$str

    #========================
    #	CFD
    #========================

    echo "CFD"

    echo "Dict"
    #System dictionnaries
    str=CFD/system/controlDict
    cp $root/$str $D/$str

    str=CFD/system/decomposeParDict
    cp $root/$str $D/$str

    str=CFD/system/fvSchemes
    cp $root/$str $D/$str

    str=CFD/system/fvSolution
    cp $root/$str $D/$str

    
    echo "Init"
   #Initial conditions
    str=CFD/0/k
    cp $root/$str $D/$str

    str=CFD/0/Ksl
    cp $root/$str $D/$str

    str=CFD/0/nuSgs
    cp $root/$str $D/$str
    
    str=CFD/0/p
    cp $root/$str $D/$str
    
    str=CFD/0/rho
    cp $root/$str $D/$str
    
    str=CFD/0/U
    cp $root/$str $D/$str
    
    str=CFD/0/Us
    cp $root/$str $D/$str
    
    str=CFD/0/voidfraction
    cp $root/$str $D/$str

    echo "Transport"
   #Transport and coupling properties
    str=CFD/constant/couplingProperties
    cp $root/$str $D/$str

    str=CFD/constant/g
    cp $root/$str $D/$str

    str=CFD/constant/LESProperties
    cp $root/$str $D/$str

    str=CFD/constant/particleTrackProperties
    cp $root/$str $D/$str

    str=CFD/constant/RASProperties
    cp $root/$str $D/$str

    str=CFD/constant/transportProperties
    cp $root/$str $D/$str

    str=CFD/constant/turbulenceProperties
    cp $root/$str $D/$str

done
