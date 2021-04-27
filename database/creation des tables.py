import sqlite3 as sql

connection=sql.connect("student.sqlite")

cur=connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Auteur (Nauteur INTEGER,nomA VARCHAR(20),prenomA VARCHAR(20),nationaliteA VARCHAR(20),CONSTRAINT pk_Auteur PRIMARY KEY (Nauteur) )")


cur.execute("CREATE TABLE IF NOT EXISTS Livre (Nlivre INTEGER, num_ISBN INTEGER,titre VARCHAR(20),nbPages INTEGER,annéeS INTEGER,prix INTEGER, CONSTRAINT pk_Livre PRIMARY KEY (Nlivre))")


cur.execute("CREATE TABLE IF NOT EXISTS Possede (Nlivre INTEGER, Nauteur INTEGER,CONSTRAINT pk_Possede PRIMARY KEY (Nlivre), CONSTRAINT fk_Possede1 FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre), CONSTRAINT fk_Possede2 FOREIGN KEY(Nauteur) REFERENCES Auteur(Nauteur))")

cur.execute("CREATE TABLE IF NOT EXISTS Pret (Npret INTEGER, num_etu INTEGER,Nlivre INTEGER,datePret DATE,dateRetour DATE,DateRetourPrevue DATE,  CONSTRAINT pk_Pret PRIMARY KEY (Npret), CONSTRAINT fk_Pret1 FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu), CONSTRAINT fk_Pret2 FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre))")


cur.execute("CREATE TABLE IF NOT EXISTS Etudiant (num_etu INTEGER,nomE VARCHAR(20),prenomE VARCHAR(20),date_naissance Date, ville VARCHAR(10),dateInscripBU DATE, dateAbs DATE, numClasse VARCHAR(20), CONSTRAINT pk_Etudiant PRIMARY KEY (num_etu), CONSTRAINT fk_Etudiant1 FOREIGN KEY(numClasse) REFERENCES Class(numClass)) ")

cur.execute("CREATE TABLE IF NOT EXISTS Class (numClass VARCHAR(20), nomclass VARCHAR(20),CONSTRAINT pk_Class PRIMARY KEY (numClass) )")

cur.execute("CREATE TABLE IF NOT EXISTS Cours (num_cours INTEGER, nomC VARCHAR(20),nb_heures INTEGER, num_ens INTEGER,CONSTRAINT pk_Cours PRIMARY KEY (num_cours), CONSTRAINT fk_Cours1 FOREIGN KEY(num_ens) REFERENCES Enseignant(num_ens))")


cur.execute("CREATE TABLE IF NOT EXISTS Enseignant (num_ens INTEGER,nomP VARCHAR(20),prénomP VARCHAR(20),specialite VARCHAR(20),department VARCHAR(20), CONSTRAINT pk_Enseignant PRIMARY KEY (num_ens))")


cur.execute("CREATE TABLE IF NOT EXISTS Resultat (num_etu INTEGER, num_cours INTEGER, note Decimal(4,2), CONSTRAINT pk_Resultat PRIMARY KEY (num_etu), CONSTRAINT fk_Resultat1 FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu), CONSTRAINT fk_Resultat2 FOREIGN KEY(num_cours) REFERENCES cours(num_cours))")


cur.execute("CREATE TABLE IF NOT EXISTS Charge (num_cours INTEGER, num_ens INTEGER, nbH Time, CONSTRAINT pk_Charge PRIMARY KEY (num_cours), CONSTRAINT fk_Charge1 FOREIGN KEY(num_cours) REFERENCES Cours(num_cours), CONSTRAINT fk_Charge2 FOREIGN KEY(num_ens) REFERENCES Enseignant(num_ens))")


cur.execute("CREATE TABLE IF NOT EXISTS Inscrit (NumEtudiant INTEGER, num_cours INTEGER, dateInsC Date,  CONSTRAINT fk_Inscrit1 FOREIGN KEY(NumEtudiant) REFERENCES Etudiant(num_etu), CONSTRAINT fk_Inscrit2 FOREIGN KEY(num_cours) REFERENCES Cours(num_cours))")

connection.commit()
connection.close()
