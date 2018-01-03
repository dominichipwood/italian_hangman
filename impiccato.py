# coding=utf-8
from random import randrange
parole=["fiori", "albero", "albergo", "ragazzo", "uomo", "funghi", "bicchiere", "occhiali", "braccia", "carta", "casa", "ferroviaria", "piatto", "libro", "cuscino", "telefono", "donna", "scarpe"]

# currently created word list by hand. Want to find a list of 1000+ words online and use python change into a useable format

N=len(parole)
i=randrange(N)
parola=parole[i]
parola1="_"*len(parola)
lettere1=["_"]*len(parola)    # letters of guessed word. slow unvealed
lettere=[l for l in parola]
vite=7
	
def rivela_let(let):    # reveal the letter
	for i in range(len(parola)):
		if let==parola[i]:
			lettere1[i]=parola[i]
	return "".join(lettere1)
	
print("La parola: {}.".format("".join(lettere1)))

while "_" in lettere1 and vite>0:   # in game play 
	if vite>1:
		print("Hai {} vite rimaste.".format(str(vite)) )
	else:
		print("Hai 1 vita rimasta, stai attento.")
		
	lettera=raw_input("Indovina una lettera: ")
	
	if len(lettera)!=1:
		print("Solo una lettera! Prova ancora.")
		continue
	elif lettera in parola:
		print(rivela_let(lettera) )
	else:
		print("«{}» non c'è. Perdi una vita!".format(lettera) )
		vite=vite-1
	
if vite==0:
	print("L'uomo è stato impiccato. Hai fallito!")
else: 
	print("Bravo! Hai salvato l'uomo")


		
		
		
		
		
