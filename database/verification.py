import sqlite3 as sql

connection=sql.connect("student.sqlite")

cur=connection.cursor()

cur.execute("SELECT name FROM sqlite_master where type ='table' AND name NOT LIKE 'sqliet_%';")

for k in cur:
    print(k)
print("les donnees de la table Enseignant")
cur.execute("SELECT * FROM Enseignant")
for k in cur:
    print(k)
    
print("les donnees de la table cours")
cur.execute("SELECT * FROM cours")
for k in cur:
    print(k)

print("les donnees de la table Charge")
cur.execute("SELECT * FROM Charge")
for k in cur:
    print(k)

print("les donnees de la table Class")
cur.execute("SELECT * FROM Class")
for k in cur:
    print(k)

print("les donnees de la table Auteur")
cur.execute("SELECT * FROM Auteur")
for k in cur:
    print(k)

print("les donnees de la table Livre")
cur.execute("SELECT * FROM Livre")
for k in cur:
    print(k)

print("les donnees de la table ETUDIANT")
cur.execute("SELECT * FROM ETUDIANT")
for k in cur:
    print(k)

print("les donnees de la table Resultat")
cur.execute("SELECT * FROM Resultat")
for k in cur:
    print(k)

print("les donnees de la table Inscrit")
cur.execute("SELECT * FROM Inscrit")
for k in cur:
    print(k)

print("les donnees de la table Pret")
cur.execute("SELECT * FROM Pret")
for k in cur:
    print(k)
