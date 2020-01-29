#!/usr/bin/python -W ignore::DeprecationWarning


"""
prediction of NinetyGL90 eightbio
date: jan 2020
author: Christophe Desterke
christophe.desterke@gmail.com
python version 3.7.3
"""


#imports
import time



# obtaining time date
horloge= time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime())


#imports
import numpy as np
import tensorflow
import sklearn
from keras.models import load_model



# definition of the variable continuer for exit interaction
continuer = True

while continuer:

	print("	--------------- ")
	print("	Ninety GL90 prediction EightBio ")
	print("	--------------- ")
	print("\n")
	print(horloge)
	print("\n")



# load model
	eight = load_model('eightbio.h5')
# summarize model.
	eight.summary()	
# pass one line for results	
	print("\n")

#input data new patient
#print("INPUT variables :CreatinineJ1, CreatinineJ3, SGOTJ3, SGPTJ3, TPJ5, biliJ7, TPJ7, biliJ12")


# input ID
	print (" Please enter identifier: " , end =' ')
	identifier = input ()
	try:
		name = str (identifier)
	except ValueError:
		print('	Please enter an integrer number!')
		continue	



# input variables	
	print (" Please enter Creatinin Day1: " , end =" ")
	CreatinineJ1 = input ()
	try:
		CreatinineJ1 = float (CreatinineJ1)
	except ValueError:
		print('	Please enter a value!')
		continue

	print (" Please enter Creatinin Day3: " , end =" ")
	CreatinineJ3 = input ()
	try:
		CreatinineJ3 = float (CreatinineJ3)
	except ValueError:
		print('	Please enter a value!')
		continue

	print (" Please enter SGOT Day3: " , end =" ")
	SGOTJ3 = input ()
	try:
		SGOTJ3 = float (SGOTJ3)
	except ValueError:
		print('	Please enter a value!')
		continue

	print (" Please enter SGPT Day3: " , end =" ")
	SGPTJ3 = input ()
	try:
		SGPTJ3 = float (SGPTJ3)
	except ValueError:
		print('	Please enter a value!')
		continue

	print (" Please enter TP Day5: " , end =" ")
	TPJ5 = input ()
	try:
		TPJ5 = float (TPJ5)
	except ValueError:
		print('	Please enter a value!')
		continue

	print (" Please enter bilirubin Day7: " , end =" ")
	biliJ7 = input ()
	try:
		biliJ7 = float (biliJ7)
	except ValueError:
		print('	Please enter a value!')
		continue

	print (" Please enter TP Day7: " , end =" ")
	TPJ7 = input ()
	try:
		TPJ7 = float (TPJ7)
	except ValueError:
		print('	Please enter a value!')
		continue

	print (" Please enter bilirubin Day12: " , end =" ")
	biliJ12 = input ()
	try:
		biliJ12 = float (biliJ12)
	except ValueError:
		print('	Please enter a value!')
		continue


	X_test2 = np.array([[CreatinineJ1, CreatinineJ3, SGOTJ3, SGPTJ3, TPJ5, biliJ7, TPJ7, biliJ12]])

	y_pred2 = eight.predict(X_test2)

	print( "Prediction of probability NINETY GL for "+ str(name)+ ": " + str(y_pred2))


# print data in txt file my body
	add =  input('Do you want to add data in the file RESULTS (y/n)? ')
	if add == "y" or add == "Y":
# exit variable
	 name = str (name)
	CreatinineJ1 = str (CreatinineJ1)
	CreatinineJ3 = str (CreatinineJ3)
	SGOTJ3 = str (SGOTJ3)
	SGPTJ3 = str (SGPTJ3)
	TPJ5 = str (TPJ5)
	biliJ7 = str (biliJ7)
	TPJ7 = str (TPJ7)
	biliJ12 = str (biliJ12)
	y_pred2 = str (y_pred2)

	mon_fichier = open ("RESULTS.txt", "a")
	mon_fichier.write ("\n")
	mon_fichier.write ("#")
	mon_fichier.write ("\n")
	mon_fichier.write ("DATE: " + "\t" + horloge + "\n")
	mon_fichier.write ("NAME: " + "\t" + name + "\n")
	mon_fichier.write ("Creatinine Day1: " + "\t" + CreatinineJ1 + "\n")
	mon_fichier.write ("Creatinine Day3: " + "\t" + CreatinineJ3 + "\n")
	mon_fichier.write ("SGOT Day3: " + "\t" + SGOTJ3 + "\n")
	mon_fichier.write ("SGPT Day3: " + "\t" + SGPTJ3 + "\n")
	mon_fichier.write ("TP Day5: " + "\t" + TPJ5 + "\n")
	mon_fichier.write ("Bilirubin Day7: " + "\t" + biliJ7 + "\n")
	mon_fichier.write ("TP Day7: " + "\t" + TPJ7 + "\n")
	mon_fichier.write ("Bilirubin Day12: " + "\t" + biliJ12 + "\n")
	mon_fichier.write ("Prediction EIGHTBIO NINETYDAY GL for "+ name +": " + "\t" + y_pred2 + "\n")

 
# interaction with exit of the software	
	quitter =  input('Do you want to exit (y/n)? ')
	if quitter == "y" or quitter == "Y":
		continuer = False

