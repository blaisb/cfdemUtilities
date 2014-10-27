grep $1 log | cut -c 18- > $1
python ./plotVariable.py $1

