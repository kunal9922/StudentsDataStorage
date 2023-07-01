# StudentDataStorage
this is a python based and sql database project to manage and stores students data

GUI look like.

1. have RollNumber field which have length to DB is 12 of type INTEGER and PRIMARY FIELD.
2. Name field varchar(30). name of student.
3. Contact  varchar(10). store contact number.
4. Email varchar(40). to store valid email address
5. .Gender is drop list. but in DB store varchar(10).
6. DOB varchar(10).
7. Address varchar(80).



## Schema design in database 

<img src="Images\schemaDesign.png">

## Updated Schema
Table Student
1. Rollnum INT PRIMARY KEY
2. Name VARCHAR(20)
3. Class VARCHAR(10)
4. Ids INT 
    FOREIGN KEY(Ids) REFRENCES Basic(Id)

Table Basic
1. Ids INT PRIMARY KEY
2. Address VARCHAR(20)
3. Gender VARCHAR(10)
4. Contact VARCHAR(13)
5. DOB DATE

## ER Diagram
<img src="Images\ER_studentRecords.png">

## First user interaction 

<img src="Images\firstUserUI.png">

## Main Frame of Student Data Record

<img src="Images\StudentRecord_Frame.png">