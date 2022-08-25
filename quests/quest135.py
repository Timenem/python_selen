"""

Create an SQLite3 database /tmp/movies.db

Your database should have a table named MOVIES that contains the following data:
Name 	Year 	Rating
Rise of the Planet of the Apes 	2011 	77
Dawn of the Planet of the Apes 	2014 	91
Alien 	1979 	97
Aliens 	1986 	98
Mad Max 	1979 	95
Mad Max 2: The Road Warrior 	1981 	100

In Haskell, both of the persistent and esqueleto modules are available...
"""


import sqlite3
connection = sqlite3.connect("/tmp/movies.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE MOVIES (name VARCHAR(250),YEAR INTEGER, RATING INTEGER)")
records = [('Rise of the Planet of the Apes', 2011, 77), ('Alien', 1979, 97), ('Mad Max 2: The Road Warrior', 1981, 100),('Mad Max', 1979, 95), ('Dawn of the Planet of the Apes', 2014, 91), ('Aliens', 1986, 98)]
cursor.executemany("insert into movies(name,year,rating) values(?,?,?)",records)


connection.commit()
connection.close()
