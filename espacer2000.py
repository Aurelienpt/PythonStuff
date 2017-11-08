input = input("Input : ")
liste = list(input)
finalText = ""
for i in range(1, len(liste)):
	finalText += liste[i] + " "
print(finalText)