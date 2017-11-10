phrase = input("Entrez une phrase a renverser : ")
liste = list(phrase)
phraseFin = ""
for i, lettre in enumerate(liste):
	phraseFin = liste[i] + phraseFin
print(phraseFin)