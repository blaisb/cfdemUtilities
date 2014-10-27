#################################
#COMMANDES POUR L'ENREGISTREMENT#
#################################
set terminal postscript eps enhanced solid "Helvetica" 20 size 5,3 # epslatex #size 1000,600set terminal postscript eps enhanced solid "Helvetica" 14
#set terminal epslatex
set termoption dash

###########
# OPENING #
###########
file = './2fplots/SOD_2p_implicite_CFL_05_err.dat'
sortie = 'SOD2f_implicite'

f3 ='uv-choc_rampe_2_CFL_05_ferr.dat'
l3='uv-choc_rampe_2_CFL_05_lerr.dat'

#######################
# Ordre des variables #
#######################

# x rho1 rho2 u1 u2 p1 p2 alpha

########
# AXES #
########


set xrange [*:*]  
set yrange [*:*]
set logscale xy

#set ticslevel(-2,0)
#Tiks
set xtics in
set mxtics 10
set ytics  in
set mytics 10
set grid xtics nomxtics ytics nomytics
# reverse met l'axe en sens inverse

set xlabel "dx [m^-1]"
set ylabel "erreur L1"
set samples 50
ref(x) = 10.**(-0.9)*sqrt(x)
# LEGENDE #
###########
set style line 1 linetype 1 pt 1 ps 1.3 lw 2 lc rgb "blue" 
set style line 2 linetype 1 pt 2 ps 1.3 lw 2 lc rgb "blue" 
set style line 3 linetype 1 pt 3 ps 1.3 lw 2 lc rgb "blue"
set style line 4 linetype 1 lw 3 lc rgb "black"
set style line 5 linetype 1 pt 1 ps 1.3 lw 2 lc rgb "red"
set style line 6 linetype 1 pt 2 ps 1.3 lw 2 lc rgb "red"
set style line 7 linetype 1 pt 3 ps 1.3 lw 2 lc rgb "red"
set style line 8 linetype 1 pt 4 ps 1.3 lw 2 lc rgb "blue"
set key on inside bottom right box 

set output sprintf('/netdata/H24872/rapport/graphiques/%s_l1.eps',sortie)

plot file using 1:2 with linespoints ls 1 title ' {/Symbol r}_1',\
	     file using 1:4 with linespoints ls 2 title 'u_1',\
	     file using 1:6 with linespoints ls 3 title 'P_1',\
	     ref(x) ls 4 with lines title 'pente = 1/2',\
	     file using 1:3 with linespoints ls 5 title ' {/Symbol r}_2',\
		 file using 1:5 with linespoints ls 6 title 'u_2',\
		 file using 1:7 with linespoints ls 7 title 'P_2'

