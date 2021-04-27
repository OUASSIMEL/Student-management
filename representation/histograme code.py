#il faut importer matplotlib pour la representation et sqlite pour la connexion a la base de donnees 
import matplotlib.pyplot as plt
import sqlite3 as sql
#etablir la connexion
connection=sql.connect("student.sqlite")
cur=connection.cursor()
#recuperer les valeurs de les notes 
cur.execute("select note from Resultat")
#mettre ces valeurs dans une liste 
notes=list(cur)
#calculer sa taille
n=len(notes)
#declarer une liste vide 
L=[]
#pour  eviter le probleme du tuple on mis les valeurs directement dans la liste L
for i in range(n):
    L.append(notes[i][0])
#append les notes sans reptition a la liste
X=list(set(L))
#declarer une autre liste vide
hauteur_barres = []
#parcourir L et compter la concurrance d'une valeur et metttre cette valeur dans la liste vide 
for i in range(len(X)):
    s=L.count(X[i])
    hauteur_barres.append(s)
#fixer la largeur des barres 
largeur_barres = 0.1
#tracer les barres
plt.bar(X, hauteur_barres, largeur_barres)
#nommer les axes
plt.xlabel("Les notes")
plt.ylabel("Nombre d'eleves")
#enregister ss forme d'une image PNG 
plt.savefig('Diag01.png')
#afficher la representation
plt.show()
