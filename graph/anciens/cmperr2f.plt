###########
# OPENING #
###########


#file = 'SOD_dte-7_err.dat'
#f3 ='SOD_dte-7_ferr.dat'
#l3='SOD_dte-7_lerr.dat'

#file = 'SOD_CFL_05_err.dat'
#f3 ='SOD_CFL_05_ferr.dat'
#l3='SOD_CFL_05_lerr.dat'

file = 'uv-choc_CFL_05_err.dat'
f3 ='uv-choc_rampe_2_CFL_05_ferr.dat'
l3='uv-choc_rampe_2_CFL_05_lerr.dat'

file2= 'uv-choc_rampe_2_CFL_05_err.dat'



#file = 'BI_SOD_div_CFL_05_err.dat'
#f3 ='BI_SOD_div_CFL_05_ferr.dat'
#l3='BI_SOD_div_CFL_05_lerr.dat'

#file = 'CD_dte-7_err.dat'
#f3 ='CD_dte-7_ferr.dat'
#l3='CD_dte-7_lerr.dat'

#file = 'dbl_exp_CFL_05_err.dat'
#f3 ='dbl_exp_CFL_05_ferr.dat'
#l3='dbl_exp_CFL_05_lerr.dat'

#######################
# Ordre des variables #
#######################

# x rho1 rho2 u1 u2 p1 p2 alpha

############
# SAMPLING #
############
#Creations de commande de sampling
set samples 50


########
# AXES #
########
set xrange [*:*]  
set yrange [*:*]
set logscale xy
#set ticslevel(-2,0)
#Tiks
set xtics in
set mxtics 5
set ytics  in
set mytics 5
set grid xtics nomxtics ytics nomytics
# reverse met l'axe en sens inverse

set xlabel "dx [m^-1]"
set ylabel "erreur L1"

# LEGENDE #
###########
set key on inside left top box title 'Légende'
ref(x) = 10.**(-0.9)*sqrt(x)

f(x)=af*x+bf

l(x)= al*x +bl
t(x) = at*log(x) + bt

#Pente des premiers points
fit f(x) f3 using 1:5 via af,bf
#Pente des derniers points
fit l(x) l3 using 1:5 via al,bl
#Pente de tout les points
fit t(x) file using 1:(log($5)) via at, bt

set style line 1 linetype 1 pt 1 ps 1.3 lc rgb "blue" 
set style line 2 linetype 1 pt 2 ps 1.3 lc rgb "blue" 
set style line 3 linetype 1 pt 3 ps 1.3 lc rgb "blue"
set style line 4 linetype 1 lc rgb "magenta"
set style line 5 linetype 1 pt 1 ps 1.3 lc rgb "red"
set style line 6 linetype 1 pt 2 ps 1.3 lc rgb "red"
set style line 7 linetype 1 pt 3 ps 1.3 lc rgb "red"
set style line 8 linetype 1 pt 4 ps 1.3 lc rgb "blue"

set style line 9 linetype 6 pt 1 ps 1.3 lc rgb "black" 
set style line 10 linetype 6 pt 2 ps 1.3 lc rgb "black" 
set style line 11 linetype 6 pt 3 ps 1.3 lc rgb "black"
set style line 12 linetype 6 pt 1 ps 1.3 lc rgb "green"
set style line 13 linetype 6 pt 2 ps 1.3 lc rgb "green"
set style line 14 linetype 6 pt 3 ps 1.3 lc rgb "green"
set style line 15 linetype 6 pt 4 ps 1.3 lc rgb "black"




plot file using 1:2 with linespoints ls 1 title 'rho1',\
	     file using 1:4 with linespoints ls 2 title 'u1',\
	     file using 1:6 with linespoints ls 3 title 'p1',\
	     ref(x) ls 4 with lines title 'pente = 1/2',\
	     file using 1:3 with linespoints ls 5 title 'rho2',\
     	     file using 1:5 with linespoints ls 6 title 'u2',\
			  file using 1:7 with linespoints ls 7 title 'p2',\
	     file using 1:8 with linespoints ls 8 title 'alpha',\
		 file2 using 1:2 with linespoints ls 9 title 'rho1',\
	     file2 using 1:4 with linespoints ls 10 title 'u1',\
	     file2 using 1:6 with linespoints ls 11 title 'p1',\
	     file2 using 1:3 with linespoints ls 12 title 'rho2',\
     	 file2 using 1:5 with linespoints ls 13 title 'u2',\
		 file2 using 1:7 with linespoints ls 14 title 'p2',\
	     file2 using 1:8 with linespoints ls 15 title 'alpha'




print 'Pente premiers points:'
print af
print 'Pente derniers points:'
print al
print 'Pente totale:'
print at

