# This program is a tentative to have automatic renumbering of .vtk file when there is an error related 
# their numbering. Since the error due to the renumbering does not give a definitive order, this script assumes that no VTK over 1000 is a valid VTK and --deletes-- the VTK with the unvalid names

# Usage : python deleteVTK.py  in the main folder of the simulation

# Author : Bruno Blais
# Last modified : 26-02-2014

#Python imports
#----------------
import os
import sys
import numpy
import re   # Ouhh regular expressions :)
#----------------

maxNum=1000

#Check existence of local VTK directory and enter:
if (os.path.exists("./VTK")) :os.chdir("./VTK")
else : raise Exception("VTK folder does not exist I believe!")

#Acquire list of .VTK
listFiles = os.listdir("./")

patternVariable = re.compile('_')
listNumAll=[]
listGood=[]
listBad=[]

#List of all file numbers
for i in listFiles :
    if patternVariable.search(i):
	#print i
	i_str=i.split("_")
	i_str=i_str[1].split(".")
	listNumAll.extend([int(i_str[0])]) #Append the number of the file to the list of files
	if (listNumAll[-1] < maxNum) : listGood.extend([listNumAll[-1]])
	else : 
	    listBad.extend([listNumAll[-1]])
	    os.remove("./"+i)

os.chdir("./lagrangian/particleCloud/")
print listBad

#Acquire list of .VTK
listFiles = os.listdir("./")

patternVariable = re.compile('_')
listNumAll=[]
listGood=[]
listBad=[]

#List of all file numbers
for i in listFiles :
    if patternVariable.search(i):
	#print i
	i_str=i.split("_")
	i_str=i_str[1].split(".")
	listNumAll.extend([int(i_str[0])]) #Append the number of the file to the list of files
	if (listNumAll[-1] < maxNum) : listGood.extend([listNumAll[-1]])
	else : 
	    listBad.extend([listNumAll[-1]])
	    os.remove("./"+i)

print listBad

#Go back to previous directory
os.chdir("../../..")
