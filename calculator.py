#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = raw_input("Entrez un premier nombre : ")
b = raw_input("Entrez un second nombre : ")
z = raw_input("Choisissez une méthode de calcul (+, -, /, *) : ")
try:
	a = float(a)
	z = str(z)
	b = float(b)
except ValueError:
	print(a, ",", b, "ou", z,  "n'est pas un nombre valide")
	exit()
if z == "+":
	calcul = a + b
	print(calcul)
elif z == "-":
	calcul = a - b
	print(calcul)
elif z == "/":
	calcul = a / b
	print(calcul)
elif z == "*":
	calcul = a * b
	print(calcul)

