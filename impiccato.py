# coding=utf-8
import unicodedata      #needed to deal with accents
import leparole         #where word list is made
from random import randrange    # needed to pick random word

parole=leparole.PAROLE     # words from doulingo

def deaccent(word): # can guess e for é
	word=str(unicodedata.normalize('NFKD',word).encode("ascii", "ignore"))
	word=word[2:-1]
	return word

#make word
N=len(parole)
i=randrange(N)
parola=parole[i]

# technically stuff
parola1="_"*len(parola)
lettere1=["_"]*len(parola)    # letters of guessed word. slowly unvealed
daparola=deaccent(parola)       #word without accents

#lives
vite=7
	
def rivela_let(let):    # reveal the letter
	for i in range(len(parola)):
		if let==daparola[i]:   # no accents
			lettere1[i]=parola[i]
	return "".join(lettere1)
	
print("La parola: {0}. Ha {1} lettere.".format("".join(lettere1), len(parola)))
 
while "_" in lettere1 and vite>0:   # in game play 
        # 1st elif sets up
	if vite>1:
		print("Hai {} vite rimaste.".format(str(vite)) )
	else:
		print("Hai 1 vita rimasta, stai attento.")

	#user guesses a letter, ignore captials and accents
	lettera=input("Indovina una lettera: ")
	lettera=deaccent(lettera)
	lettera=lettera.lower()
	

	# check input of correct format
	if len(lettera)!=1:
		print("Solo una lettera! Prova ancora.")
		continue
	elif lettera in daparola:       #in de accented word
		print(rivela_let(lettera) )
	else:
		print("«{}» non c'è. Perdi una vita!".format(lettera) )
		vite=vite-1

#end game	
if vite==0:
	print("L'uomo è stato impiccato. Hai fallito! La paorla era \"{}\".".format(parola))
else: 
	print("Bravo! Hai salvato l'uomo")
