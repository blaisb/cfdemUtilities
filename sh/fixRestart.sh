destime=6


for i in 0 1 2 3 4 5 6 7 8 9 10 11
do
	echo "cp processor$i/0/Ksl processor$i/$destime/"
	cp processor$i/0/Ksl processor$i/$destime/
	echo "cp processor$i/0/rho processor$i/$destime/"
        cp processor$i/0/rho processor$i/$destime/

done
