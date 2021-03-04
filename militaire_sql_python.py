import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="KevinB", 
  password="ludo1703",
  database = "militaire"
)

print(mydb)

mycursor = mydb.cursor() # command who permit to enter a SQL code
mycursor.execute("CREATE DATABASE militaire;") # command to create a Database
mycursor.execute("SHOW DATABASES;") # show all databases for MySQL user
for database in mycursor :
  print(database)
# create tables for militaire database
mycursor.execute("CREATE TABLE soldat(id_soldat INT NOT NULL AUTO_INCREMENT, matricule INT NOT NULL , nom VARCHAR(20) NOT NULL, grade VARCHAR(30) NOT NULL , PRIMARY KEY(id_soldat));")
mycursor.execute("CREATE TABLE email(id_email INT NOT NULL AUTO_INCREMENT , adresse_email VARCHAR(50), id_soldat INT NOT NULL, PRIMARY KEY(id_email));")
mycursor.execute("ALTER TABLE email ADD FOREIGN KEY(id_soldat) REFERENCES soldat(id_soldat);") #
mycursor.execute("CREATE TABLE obstacle (id_obstacle INT NOT NULL AUTO_INCREMENT, nombre_obstacle INT NOT NULL, date_de_passage DATETIME, PRIMARY KEY(id_obstacle));) ")
mycursor.execute("ALTER TABLE obstacle ADD FOREIGN KEY(id_soldat) REFERENCES soldat(id_soldat);")
mycursor.execute("CREATE TABLE instructeur( id_instructeur INT NOT NULL AUTO_INCREMENT, temps_de_passage INT NOT NULL , id_soldat INT NOT NULL, matricule_instructeur INT NOT NULL, PRIMARY KEY(id_instructeur));")
mycursor.execute("ALTER TABLE instructeur ADD FOREIGN KEY(id_soldat) REFERENCES soldat(id_soldat);")
mycursor.execute("CREATE TABLE note(id_note INT NOT NULL AUTO_INCREMENT , bonus INT NOT NULL , id_instructeur INT NOT NULL , id_soldat INT NOT NULL , note_finale INT NOT NULL, PRIMARY KEY(id_note));")
mycursor.execute("ALTER TABLE note ADD FOREIGN KEY(id_soldat) REFERENCES soldat(id_soldat);")
mycursor.execute("ALTER TABLE note ADD FOREIGN KEY(id_instructeur) REFERENCES instructeur(id_instructeur);")

# insert data in table soldat

sql = "INSERT INTO soldat (matricule, nom, grade) VALUES(%s,%s, %s)"
values =[
(1043,'Dupont','Lieutenant')
(9874, 'Dufresne', 'colonel'),
(5786, 'Rochefort', 'Capitaine'),
(1234, 'Beaumont', 'Géneral'),
(4567, 'Dupond', 'Lieutenant-colonel')
]
mycursor.executemany(sql, values) # execute many SQL request
mydb.commit() # save request on table

# insert data in table email
sql = "INSERT INTO email (adresse_email , id_soldat) VALUES( %s, %s);" # %s is replace by values 
values = [
("albert.dupont@gmail.com", 3),
("pierre.dufresne@gmail.com",5),
("paul.rochefort@gmail.com",6),
("jacques.beaumont@gmail.com",7),
("ludovic.dupond@gmail.com",8)
        ]
mycursor.executemany(sql,values)
mydb.commit()

# insert data in table obstacle
sql = "INSERT INTO obstacle (nombre_obstacle , date_de_passage, id_soldat) VALUES( %s, %s, %s);"
values =[
(17, "2000-07-05", 7),
(23, "2019-03-19", 3),
(19, "2015-08-30", 6),
(25, "2017-01-27", 8),
(18, "2003-05-15", 7)
]
mycursor.executemany(sql, values)
mydb.commit()

# insert datas in talble instructeur

sql = "INSERT INTO instructeur (temps_de_passage, matricule_instructeur , id_soldat) VALUES(%s, %s, %s);"
values =[
(83, 6398, 7),
(97, 7894, 3),
(90, 1475, 6),
(98, 1236, 8),
(80, 7536, 7)
]
mycursor.executemany(sql, values)
mydb.commit()

# insert datas in table note
sql = "INSERT INTO note (bonus, id_instructeur, id_soldat, note_finale) VALUES (%s, %s, %s, %s);"
values = [
(1, 1, 7, 17),
(1, 2, 3, 28),
(1, 3, 6, 24),
(2, 4, 8, 38),
(2, 5, 7, 26)
]
mycursor.executemany(sql, values)
mydb.commit()

# delete a line from table soldat
mycursor.execute("DELETE FROM soldat WHERE id_soldat = 4;")
#mydb.commit()

# update a line from table email
mycursor.execute("UPDATE email SET adresse_email = 'charles.dupont@gmail.com', id_soldat = 8 WHERE id_email = 5;")
mydb.commit()


