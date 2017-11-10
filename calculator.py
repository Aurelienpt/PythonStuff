a = input("Entrez un premier nombre : ")
b = input("Entrez un second nombre : ")
z = input("Choisissez une méthode de calcul (+, -, /, *) : ")
try:
	a = float(a)
	b = float(b)
except ValueError:
	print(a, "ou", b,  "n'est pas un nombre valide")
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