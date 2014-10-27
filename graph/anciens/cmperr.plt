###########
# OPENING #
###########

set terminal postscript eps enhanced color solid "Helvetica" 20 size 5,3.0
file = './plots/dbl_exp_nodifvit_CFL_05_err.dat'
f3 ='./plots/dbl_exp_CFL_05_ferr.dat'
l3='./plots/dbl_exp_CFL_05_lerr.dat'
file2='./plots/dbl_exp_CFL_05_err.dat'
#file = 'SOD_dte-7_err.dat'
#f3 ='SOD_dte-7_ferr.dat'
#l3='SOD_dte-7_lerr.dat'
#file2='SOD_dte-8_err.dat'

#file = 'SOD_dte-7_err.dat'
#f3 ='SOD_dte-7_ferr.dat'
#l3='SOD_dte-7_lerr.dat'
#file2='SOD_CFL_01_err.dat'


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

set xlabel "dx [m^{-1}]"
set ylabel "erreur L1"

# LEGENDE #
###########
set key on inside right bottom box 
ref(x) = 10.**(-0.9)*sqrt(x)

f(x)=af*x+bf

l(x)= al*x +bl
t(x) = at*log(x) + bt
fit f(x) f3 using 1:2 via af,bf
fit l(x) l3 using 1:2 via al,bl
fit t(x) file using 1:(log($2)) via at, bt

set style line 1 linetype 1 pt 1 ps 1.5 lw 2 lc  rgb "blue" 
set style line 2 linetype 1 pt 2 ps 1.5 lw 2 lc  rgb "blue" 
set style line 3 linetype 1 pt 3 ps 1.5 lw 2 lc rgb "blue"
set style line 4 linetype 1 lw 2 lc rgb "magenta "
set style line 5 linetype 1 pt 1 ps 1.5 lw 2 lc rgb "#DC143C"
set style line 6 linetype 1 pt 2 ps 1.5 lw 2 lc rgb "#DC143C"
set style line 7 linetype 1 pt 3 ps 1.5 lw 2 lc rgb "#DC143C"

set output '/netdata/H24872/rapport/graphiques/dbl_exp_convergence.eps'

plot file using 1:2 with linespoints ls 1 title '{/Symbol r}  - NC',\
		 file using 1:3 with linespoints ls 2 title 'u - NC',\
		 file using 1:4 with linespoints ls 3 title 'p - NC',\
		 ref(x) ls 4 with lines title 'pente 1/2',\
		 file2 using 1:2 with linespoints ls 5 title '{/Symbol r}  - A1',\
		 file2 using 1:3 with linespoints ls 6 title 'u - A1',\
		 file2 using 1:4 with linespoints ls 7 title 'p - A1'


print 'Pente premiers points:'
print af
print 'Pente derniers points:'
print al
print 'Pente totale:'
print at

