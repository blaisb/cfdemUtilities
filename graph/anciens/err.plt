###########
# OPENING #
###########


#file = 'SOD_dte-7_err.dat'
#f3 ='SOD_dte-7_ferr.dat'
#l3='SOD_dte-7_lerr.dat'

#file = 'SOD_CFL_05_err.dat'
#f3 ='SOD_CFL_05_ferr.dat'
#l3='SOD_CFL_05_lerr.dat'

#file = 'CD_biphas_CFL_05_err.dat'
#f3 ='CD_biphas_CFL_05_ferr.dat'
#l3='CD_biphas_CFL_05_lerr.dat'

file = 'CD_dte-7_err.dat'
f3 ='CD_dte-7_ferr.dat'
l3='CD_dte-7_lerr.dat'

#file = 'dbl_exp_CFL_05_err.dat'
#f3 ='dbl_exp_CFL_05_ferr.dat'
#l3='dbl_exp_CFL_05_lerr.dat'

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
fit f(x) f3 using 1:2 via af,bf
fit l(x) l3 using 1:2 via al,bl
fit t(x) file using 1:(log($2)) via at, bt

plot file using 1:2 with linespoints title 'rho', file using 1:3 with linespoints title 'u', file using 1:4 with linespoints title 'p', ref(x) title 'pente = 1/2'

print 'Pente premiers points:'
print af
print 'Pente derniers points:'
print al
print 'Pente totale:'
print at

