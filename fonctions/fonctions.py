import sqlite3 as sql

connection=sql.connect("student.sqlite")

cur=connection.cursor()

def empLiv(Nlivre):
        #recuperer les etudiants qui ont prent le livre du numero Nlivre
        cur.execute('select nomE,dateRetour,Nlivre from Etudiant E, Pret  p where E.num_etu=P.num_etu and Nlivre=?',(Nlivre,))
        prets=cur.fetchall()
        #calculer la taille de la liste prets
        n=len(prets)
        #affichage des etudiant
        for k in range(n):
                print (prets[k])

def insBU(nomE):
        #recuperer la date d'inscription du l'etudiant nomE stocke dans la base de donnes
	cur.execute('select nomE ,dateInscripBU from Etudiant where nomE=?',(nomE,))
	#recuper le tuple (nomE,date)
	noms=cur.fetchone()
	#verifier est ce que le tuple est vide au cas au le nomE n'existe pas dans la base de donnees
	if noms == None:
		print("L'etudiant n'est pas inscrit dans la bibl")
	#si il existe afficher la date d'inscription
	else:
		if nomE == noms[0]:
			print ("La date d'inscription est :")
			print(noms[1])
def insCour(num_cours):
    #recuperer tous les etudiants inscrit dans le cours num_cours
    cur.execute("select nomE,prenomE from Etudiant E,Inscrit I where E.num_etu=I.NumEtudiant and I.num_cours=? ",(num_cours,))
    #vider le cursor et mettre tous les donnees dans num
    num=cur.fetchall()
    #afficher tous les donnees de num
    for k in num:
	    print(k)

def insr():
    #recuperer tous les noms des étudiants inscrits dans tous les modules
    cur.execute("select nomE,prenomE,count(nomC) 'nombre de cours' from Etudiant E, Inscrit I, Cours C where E.num_etu=I.NumEtudiant and I.num_cours= C.num_cours group by nomE having count(nomC)= (select count(nomC) from Cours)")
    #mettre les resultats dans une liste par la fct fetchall()
    ins=cur.fetchall()
    #parcourir la liste puis afficher les noms
    for k in ins:
            print(k)
def noEmp():
        #recuperer tous les noms des livres empruntés par personne
        cur.execute("SELECT titre, nomE From Etudiant E, Pret P, Livre L WHERE E.num_etu=P.num_etu AND P.Nlivre=L.Nlivre")
        #mettre les resultats dans une liste par fetchall()
        per=cur.fetchall()
        #affichage 
        for k in per:
                print(k)


def ResuEtu(num_etu):
    #recuperer tous les informations de l'etudiant qui a le numero num_etu
    cur.execute("select nomE, prenomE, note ,nomC, AVG(note),Max(note),MIN(note) from Etudiant E, Cours  C, Resultat R where E.num_etu=R.num_etu and R.num_cours=C.num_cours  and E.num_etu=? group by nomC",(num_etu,))
    #mettre tous les donnees dans la liste etu
    etu=list(cur)
    #initaliser la moyenne par 0
    moyenne=0;
    #calculer la taille de la liste etu
    n=len(etu)
    #afficher tous les donnees de etu
    for k in range(n):
            #la somme de notes des modules
            moyenne = moyenne + etu[k][2]
            #affichage des info de l'etudiant 
            print(etu[k])
    print("La moyenne generale est :")
    #calclue et affichage de la note 
    print(moyenne/n)

def resultEchec():
    #recuperer tous les informations de les etudiant qui n'a pas reussient
    cur.execute("select nomE,prenomE,note,AVG(note) from Etudiant E, Cours  C, Resultat R where E.num_etu=R.num_etu and R.num_cours=C.num_cours and note <10 group by nomC ")
    ech=cur.fetchall()
    #calculer la taille de la liste ech
    n=len(ech)
    #affichage des etudiant 
    for k in range (n):
        print(ech[k])

def ResultTot():
        #recuperer le nom de la classe et la moyenne des notes obtenues par cours
        cur.execute("select nomclass,nomC, AVG(note) from Class C, Cours Cs, Resultat R ,Etudiant E where C.numClass=E.numClasse and E.num_etu=R.num_etu and R.num_cours=Cs.num_cours Group by nomC")
        #mettre les resultats dans une liste 
        res=list(cur)
        #calculer la taille de la liste
        n=len(res)
        #affichage 
        for k in range(n):
            print (res[k])

def retard():
        #recuperer tous les etudiants n’ayant pas encore rendus au moins un livre
        cur.execute("select nomE,dateRetour,DateRetourPrevue,Nlivre from Etudiant E, Pret p  where E.num_etu=P.num_etu  and dateRetour IS NULL")
        #mettre les resultats dans une liste 
        ret=cur.fetchall()
        #calculer la taille de la liste ret 
        n=len(ret)
        #affichage des etudiants
        for k in range(n):
                print (ret[k])
#recuperer les noms des profs pr module 
cur.execute("select nomP,prénomP,nomC from Enseignant E,Charge C, Cours Cs where E.num_ens=C.num_ens AND C.num_cours=Cs.num_cours")
#parcourir le cursor puis affichage
for k in cur:
        print(k)

def changer_le_nom(num_cours):
        #donner a l'utilisateur le droit d'ecrire le nom de cours
        nomCours = input("Entrer le nom :")
        #affichage des noms des cours avant le changement 
        print("=========Avant==========")
        cur.execute("select nomC from Cours")
        for k in cur:
                print(k)
        #changement du nom de cours 
        cur.execute("UPDATE Cours SET nomC =? WHERE num_cours=?",(nomCours,num_cours))
        #affichage des noms des cours apres le changement 
        print("=========Apres==========")
        cur.execute("select nomC from Cours")
        for k in cur:
                print(k)

def supprimer_le_cours(num_cours):
        #affichage des noms des cours avant la suppression 
        print("=========Avant==========")
        cur.execute("select nomC from Cours")
        for k in cur:
                print(k)
        #supprission du cours souhaite
        cur.execute("DELETE FROM Cours WHERE num_cours=?",(num_cours,))
        #affichage des noms des cours apres la suppression 
        print("=========Apres==========")
        cur.execute("select nomC from Cours")
        for k in cur:
                print(k)

                
connection.commit()


