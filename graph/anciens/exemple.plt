# Commentaire

#################################
#COMMANDES POUR L'ENREGISTREMENT#
#################################
set terminal png size 2400,1500
set output 'test.png'

############
# SAMPLING #
############
#Creations de commande de sampling
#set samples 50
#set isosamples 50

#set hidden3d

#f(x)=sqrt(x)

###########
# OPENING #
###########


file = 'SOD_dte-7_1e4.dat'


########
# AXES #
########
set xrange [*:*]  
set yrange [*:1.1]
#set ticslevel(-2,0)
#Tiks
set xtics in
set mxtics 5
set ytics  in
set mytics 5
set grid xtics nomxtics ytics nomytics
# reverse met l'axe en sens inverse

set xlabel "x [m]"
set ylabel "rho [kg /m^3]"

###########
# LEGENDE #
###########
set key on inside right top box title 'Légende'


#Dessin d'un graphique
#plot  file using 1:2 with lines title  'rho_analytique', file using 1:6 with lines title 'rho_num'
# get into multiplot mode
set multiplot;                          # get into multiplot mode
set size 0.5,0.5;  
set origin 0.0,0.5; plot  file using 1:2 with lines title  'rho_analytique', file using 1:6 with lines title 'rho_num'
set yrange [*:*]
set xlabel "x [m]"
set ylabel "u [m/s]"
set key on inside left top box title 'Légende'
set origin 0.5,0.5; plot  file using 1:3 with lines title  'u_analytique', file using 1:7 with lines title 'u_num'
set yrange [*:*]
set xlabel "x [m]"
set ylabel "P [Pa]"
set key on inside left top box title 'Légende'
set origin 0.0,0.0; plot  file using 1:4 with lines title  'p_analytique', file using 1:8 with lines title 'p_num'

unset multiplot        



#Enregistrement

