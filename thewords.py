#convert doulingowords.txt to useable format

# coding=utf-8
import re
doc=open("parole.txt")
PAROLE=[]
c=0
for riga in doc:
    nome=re.search("Noun", riga)
    Nome=re.search("Proper noun", riga)
    if nome:
        i=nome.start()  # 
        parola=riga[:i-1] #i-1 to get rid of a space. Want the word before space + noun
        PAROLE.append(parola)
    elif Nome:
        i=Nome.start()  
        parola=riga[:i-1] 
        PAROLE.append(parola)
PAROLE=list(map(lambda parola: parola.lower(), PAROLE)) # make sure everthing is lowercase

