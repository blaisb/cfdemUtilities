# Commentaire

#################################
#COMMANDES POUR L'ENREGISTREMENT#
#################################
set terminal postscript eps enhanced solid "Helvetica" 18 size 5,3.5 # epslatex #size 1000,600set terminal postscript eps enhanced solid "Helvetica" 14
#set terminal epslatex

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


file = 'SOD_CFL_05_1e4.dat'


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

########
# FONTS #
#########
#set xtics font "Times-Roman, 20"
#set ytics font "Times-Roman, 20"
#set title font "Times-Roman, 20"
#set ylabel font "Times-Roman, 20"
#set xlabel font "Times-Roman, 20"
#set key font "Times-Roman, 20"
###########
# LEGENDE #
###########
set key on inside right top box 

set output 'rho.eps'
#Dessin d'un graphique
#plot  file using 1:2 with lines title  'rho_analytique', file using 1:6 with lines title 'rho_num'
# get into multiplot mode
set style line 1 linetype 1 lw 2 lc rgb "blue" 
set style line 2 linetype 1 lw 2 lc rgb "red"
plot  file using 1:2 with lines ls 1  title  'rho-analytique', file using 1:6 with lines ls 2 title 'rho-simulation'

set output 'u.eps'
 set yrange [*:*]
set xlabel "x [m]"
set ylabel "u [m/s]"
set key on inside left top box 
plot  file using 1:3 with lines ls 1 title  'u-analytique', file using 1:7 with lines ls 2 title 'u-numerique'

set output 'p.eps'
set yrange [*:*]
set xlabel "x [m]"
set ylabel "P [Pa]"
set key on inside right top box 
 plot  file using 1:4 with lines ls 1 title  'p-analytique', file using 1:8 with lines ls 2 title 'p-numerique'


#Enregistrement

