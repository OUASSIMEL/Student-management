import sqlite3 as sql
#etablir la connection
connection=sql.connect("student.sqlite")
#etablir le cursor
cur=connection.cursor()

#========================================================================#
#augmenter la taille de la colonne nom de la table Etudiant

#il faut d'abord creer une table avec les modifications souhitees 
cur.execute("CREATE TABLE copy_table_name (num_etu INTEGER,nomE VARCHAR(24),prenomE VARCHAR(20),date_naissance Date, ville VARCHAR(10),dateInscripBU DATE, dateAbs DATE, numClasse VARCHAR(20), CONSTRAINT pk_Etudiant PRIMARY KEY (num_etu), CONSTRAINT fk_Etudiant1 FOREIGN KEY(numClasse) REFERENCES Class(numClass)) ")
#copier data a la nouvelle table
cur.execute("INSERT INTO copy_table_name SELECT * FROM Etudiant")
#supprimer la table ancienne
cur.execute("DROP TABLE ETudiant")
#renommer la table 
cur.execute("ALTER TABLE copy_table_name RENAME TO Etudiant")
connection.commit()
#========================================================================#
#Ajouter le champ email à la table étudiant

cur.execute("ALTER TABLE Etudiant ADD COLUMN email varchar (20)")
connection.commit() 
#========================================================================#
#Ajouter la colonne adresse à la table adresse.

cur.execute("ALTER TABLE Etudiant ADD COLUMN adresse varchar (20)")
connection.commit()
#========================================================================#
#Supprimer les contraintes de la table pret

#il faut d'abord creer une table sans contraintes  
cur.execute("CREATE TABLE IF NOT EXISTS copy_table_name (Npret INTEGER, num_etu INTEGER,Nlivre INTEGER,datePret DATE,dateRetour DATE,DateRetourPrevue DATE)")
#copier data a la nouvelle table
cur.execute("INSERT INTO copy_table_name SELECT * FROM Pret")
#supprimer la table ancienne
cur.execute("DROP TABLE Pret")
#renommer la table 
cur.execute("ALTER TABLE copy_table_name RENAME TO Pret")
connection.commit()
#========================================================================#
#Supprimer les contraintes de la table pret

#il faut d'abord creer une table avec une cle primaire  
cur.execute("CREATE TABLE IF NOT EXISTS copy_table_name (Npret INTEGER, num_etu INTEGER,Nlivre INTEGER,datePret DATE,dateRetour DATE,DateRetourPrevue DATE,CONSTRAINT pk_Pret PRIMARY KEY (Npret))")
#copier data a la nouvelle table
cur.execute("INSERT INTO copy_table_name SELECT * FROM Pret")
#supprimer la table ancienne
cur.execute("DROP TABLE Pret")
#renommer la table 
cur.execute("ALTER TABLE copy_table_name RENAME TO Pret")
connection.commit()
#========================================================================#
#Supprimer les contraintes de la table pret

#il faut d'abord creer une table avec la cle primaire et la premaire cle etrangaire  
cur.execute("CREATE TABLE IF NOT EXISTS copy_table_name (Npret INTEGER, num_etu INTEGER,Nlivre INTEGER,datePret DATE,dateRetour DATE,DateRetourPrevue DATE,CONSTRAINT pk_Pret PRIMARY KEY (Npret),CONSTRAINT fk_Pret1 FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu))")
#copier data a la nouvelle table
cur.execute("INSERT INTO copy_table_name SELECT * FROM Pret")
#supprimer la table ancienne
cur.execute("DROP TABLE Pret")
#renommer la table 
cur.execute("ALTER TABLE copy_table_name RENAME TO Pret")
connection.commit()
#========================================================================#
#Supprimer les contraintes de la table pret

#il faut d'abord creer une table avec la cle primaire et les deux cles etrangaires   
cur.execute("CREATE TABLE IF NOT EXISTS copy_table_name (Npret INTEGER, num_etu INTEGER,Nlivre INTEGER,datePret DATE,dateRetour DATE,DateRetourPrevue DATE,CONSTRAINT pk_Pret PRIMARY KEY (Npret),CONSTRAINT fk_Pret1 FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu),CONSTRAINT fk_Pret2 FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre))")
#copier data a la nouvelle table
cur.execute("INSERT INTO copy_table_name SELECT * FROM Pret")
#supprimer la table ancienne
cur.execute("DROP TABLE Pret")
#renommer la table 
cur.execute("ALTER TABLE copy_table_name RENAME TO Pret")
connection.commit()
#========================================================================#
#Modifier la table livre en y ajoutant la colonne Nauteur

#il faut ajouter la colonne Nauteur a la table Livre  
cur.execute("ALTER TABLE Livre ADD COLUMN Nauteur INTEGER")
#il faut d'abord creer une table avec la colonne Nauteur et la contrainte de reference  
cur.execute("CREATE TABLE IF NOT EXISTS copy_table_name (Nlivre INTEGER,Nauteur INTEGER, num_ISBN INTEGER,titre VARCHAR(20),nbPages INTEGER,annéeS INTEGER,prix INTEGER, CONSTRAINT pk_Livre PRIMARY KEY (Nlivre),CONSTRAINT fk_Livre FOREIGN KEY(Nauteur) REFERENCES Auteur(Nauteur))")
#copier data a la nouvelle table
cur.execute("INSERT INTO copy_table_name SELECT * FROM Livre")
#supprimer la table ancienne
cur.execute("DROP TABLE Livre")
#renommer la table 
cur.execute("ALTER TABLE copy_table_name RENAME TO Livre")
connection.commit()
#========================================================================#
#supprimer la table Possede

cur.execute("DROP TABLE Possede")
connection.commit()
#========================================================================#
#Ajouter une contrainte à la table livre qui assure que titre de livre est une valeur unique

#il faut d'abord creer une table    
cur.execute("CREATE TABLE IF NOT EXISTS copy_table_name (Nlivre INTEGER,Nauteur INTEGER, num_ISBN INTEGER,titre VARCHAR(20),nbPages INTEGER,annéeS INTEGER,prix INTEGER, CONSTRAINT pk_Livre PRIMARY KEY (Nlivre),CONSTRAINT fk_Livre FOREIGN KEY(Nauteur) REFERENCES Auteur(Nauteur),CONSTRAINT titre_unique UNIQUE (titre))")
#copier data a la nouvelle table
cur.execute("INSERT INTO copy_table_name SELECT * FROM Livre")
#supprimer la table ancienne
cur.execute("DROP TABLE Livre")
#renommer la table 
cur.execute("ALTER TABLE copy_table_name RENAME TO Livre")
connection.commit()
#========================================================================#
#Ajouter la colonne langue et la colonne NbreExemplaires à la table adresse

cur.execute("ALTER TABLE Livre ADD COLUMN langue varchar (20)")
cur.execute("ALTER TABLE Livre ADD COLUMN NbreExemplaires INTEGER")
connection.commit()
#========================================================================#
#Ajouter la contrainte qui assure l’unicité du numISBN

#il faut d'abord creer une table    
cur.execute("CREATE TABLE IF NOT EXISTS copy_table_name (Nlivre INTEGER,Nauteur INTEGER, num_ISBN INTEGER,titre VARCHAR(20),nbPages INTEGER,annéeS INTEGER,prix INTEGER,langue varchar (20),NbreExemplaires INTEGER, CONSTRAINT pk_Livre PRIMARY KEY (Nlivre),CONSTRAINT fk_Livre FOREIGN KEY(Nauteur) REFERENCES Auteur(Nauteur),CONSTRAINT titre_unique UNIQUE (titre),CONSTRAINT uniquenumISBN UNIQUE(num_ISBN))")
#copier data a la nouvelle table
cur.execute("INSERT INTO copy_table_name SELECT * FROM Livre")
#supprimer la table ancienne
cur.execute("DROP TABLE Livre")
#renommer la table 
cur.execute("ALTER TABLE copy_table_name RENAME TO Livre")
connection.commit()
#========================================================================#
#Ajouter la contrainte qui spécifie que date_retour est >= date_pret

#il faut d'abord creer une table   
cur.execute("CREATE TABLE IF NOT EXISTS copy_table_name (Npret INTEGER, num_etu INTEGER,Nlivre INTEGER,datePret DATE,dateRetour DATE,DateRetourPrevue DATE,CONSTRAINT pk_Pret PRIMARY KEY (Npret),CONSTRAINT fk_Pret1 FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu),CONSTRAINT fk_Pret2 FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre),CONSTRAINT check_dateretour CHECK(dateRetour >= datePret))")
#copier data a la nouvelle table
cur.execute("INSERT INTO copy_table_name SELECT * FROM Pret")
#supprimer la table ancienne
cur.execute("DROP TABLE Pret")
#renommer la table 
cur.execute("ALTER TABLE copy_table_name RENAME TO Pret")
connection.commit()
connection.close()
#========================================================================#











