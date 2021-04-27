#il faut importer matplotlib pour la representation et sqlite pour la connexion a la base de donnees 
import matplotlib.pyplot as plt
import sqlite3 as sql
#etablir la connexion
connection=sql.connect("student.sqlite")
cur=connection.cursor()
#donner les noms a chaque groupe ou section
labels = 'nb eleve note<8', 'nb eleve 8<note<10', 'nb eleve 10<note<12', 'nb eleve 12<note<14', 'nb eleve 14<note'
#declarer les couleurs qu'on doit utiliser 
colors= ['m','c','r','b','g']
#declarer une liste vide
notesPer = []
#recuperer les valeurs de les notes 
cur.execute('select note from Resultat')
#mettre ces valeurs dans une liste 
notes=list(cur)
#calculer sa taille
n=len(notes)
#declarer une liste vide 
temp=[]
#pour  eviter le probleme du tuple on mis les valeurs directement dans la liste L
for i in range(n):
    temp.append(notes[i][0])
#initaliser des variables qu'on doit utiliser pour compter les nombres des etudiants qui valide une condition
h=0
d=0
dz=0
qt=0
sq=0
#parcourir la liste et counter le nombre des etudiants qui valide une condition
for i in range(n):
    if temp[i]<8 or temp[i]==8:
        h=h+1
    elif (8<temp[i] and temp[i]<10) or temp[i]==10:
        d=d+1
    elif (10<temp[i] and temp[i]<12) or temp[i]==12:
        dz=dz+1
    elif (12<temp[i] and temp[i]<14) or temp[i]==14:
        qt=qt+1
    else :
        sq=sq+1
#apres le parcour on ajoute les nombres des etudiants qui on valider la meme condition 
notesPer.append(h)
notesPer.append(d)
notesPer.append(dz)
notesPer.append(qt)
notesPer.append(sq)
#tracer le camembert par pie de python
plt.pie(notesPer, labels=labels, colors=colors, shadow=True, startangle=90)
#pour tracer un camembert circulaire (meme diametres)
plt.axis('equal')
#enregister ss forme d'une image
plt.savefig('PieChart01.png')
#afficher le camembert
plt.show()







