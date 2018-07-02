import sqlite3
conn= sqlite3.connect('assign')
print("Opened database successfully")
#ques1:
conn.execute('''CREATE TABLE BOOKS
  (BOOK_ID INT PRIMARY KEY NOT NULL,
  TITLE_ID INT NOT NULL,
  LOCATION CHAR(50) NOT NULL,
  GENRE CHAR(50) NOT NULL)''')

print("books table created")

conn.execute('''CREATE TABLE TITLE
  (TITLE_ID INT PRIMARY KEY NOT NULL,
  TITLE CHAR(50) NOT NULL,
  ISBN CHAR(50) NOT NULL,
  PUBLISHER_ID INT NOT NULL,
  PUBLISHER_YEAR INT NOT NULL)''')

print("Titles table created")

conn.execute('''CREATE TABLE PUBLISHERS
  (PUBLISHER_ID INT PRIMARY KEY NOT NULL,
  NAME CHAR(50) NOT NULL,
  STREET_ADDRESS CHAR(50) NOT NULL,
  SUITE_NUMBER INT NOT NULL,
  ZIPCODE_ID INT NOT NULL)''')

print("Publisher table created")

conn.execute('''CREATE TABLE ZIPCODE
  (ZIP_ID INT PRIMARY KEY NOT NULL,
  CITY CHAR(30) NOT NULL,
  STATE CHAR(30) NOT NULL,
  ZIPCODE INT NOT NULL)''')

print("Zip table created")

conn.execute('''CREATE TABLE AUTHORS_TITLE
  (AU_ID INT PRIMARY KEY NOT NULL,
  AUHTOR_ID INT NOT NULL,
  TITLE_ID INT NOT NULL)''')

print("Author titles table created")

conn.execute('''CREATE TABLE AUTHOR
 (AUTHOR_ID INT PRIMARY KEY NOT NULL,
 FIRST_NAME CHAR(50) NOT NULL,
 MIDDLE_NAME CHAR(30) NOT NULL,
 LAST_NAME CHAR(30) NOT NULL)''')

print("Author table created")

#ques 2:

conn.execute("INSERT INTO BOOKS (BOOK_ID,TITLE_ID,LOCATION,GENRE) VALUES(1,1,'India','Adventure')")
conn.execute("INSERT INTO BOOKS (BOOK_ID,TITLE_ID,LOCATION,GENRE) VALUES(2,2,'India','Mystery')")

conn.execute("INSERT INTO TITLE (TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLISHER_YEAR) VALUES(1,1,1215,1,2016)")
conn.execute("INSERT INTO TITLE (TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLISHER_YEAR) VALUES(2,2,2153,2,2018)")

conn.execute("INSERT INTO PUBLISHERS (PUBLISHER_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIPCODE_ID) VALUES(1,'Abhay','UYGUYSGUYS',1,1)")
conn.execute("INSERT INTO PUBLISHERS (PUBLISHER_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIPCODE_ID) VALUES(2,'Vivek','SDUHFUISHF',2,2)")

conn.execute("INSERT INTO ZIPCODE (ZIP_ID,CITY,STATE,ZIPCODE) VALUES(1,'PUNJAB','BATHINDA',151001)")
conn.execute("INSERT INTO ZIPCODE (ZIP_ID,CITY,STATE,ZIPCODE) VALUES(2,'SDF','sFSDF',123548)")

conn.execute("INSERT INTO AUTHORS_TITLE (AU_ID,AUHTOR_ID,TITLE_ID) VALUES(1,1,1)")
conn.execute("INSERT INTO AUTHORS_TITLE (AU_ID,AUHTOR_ID,TITLE_ID) VALUES(2,2,2)")


conn.execute("INSERT INTO AUTHOR (AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME) VALUES(1,'NIRAVAN','DFSDF','KAPOOR')")
conn.execute("INSERT INTO AUTHOR (AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME) VALUES(2,'PHILIP','FCSDF','KAPOORANI')")
conn.commit()
print("records of books created successfully")


#ques 3:
conn.execute("UPDATE BOOKS set LOCATION = 'ADGSFCAF' where BOOK_ID = 2")
conn.commit()
print("Total nmber of rows updated:",conn.total_changes)
cursor = conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE from BOOKS where BOOK_ID = 2")
for row in cursor:
    print("BOOK ID =",row[0])
    print("TITLE ID =", row[1])
    print("LOCATTION =", row[2])
    print("GENRE =", row[3])

print("Operation done successfully")
