# Students Record Management System.
•	Developed a student record management system using Python for front-end and API, and MySQL Database for record storage.
•	Created an intuitive user interface for adding, editing, and deleting student records. Implemented features such as search and filtering to make it easy to find specific records.
•	Improved data security by implementing user authentication and access control.


## ER Diagram
<img src="Images\updatedERDiagram.png">

## Schema design in database 
<img src="Images\UpdatedSchema1.png">
<img src="Images\UpdatedSchema2.png">

## Updated Schema
Table Student
1. rollnum INT PRIMARY KEY
2. nameStudent VARCHAR(20)
3. email VARCHAR(30)
4. id INT 
    FOREIGN KEY(id) REFRENCES Basic(id)

Table Basic
1. id INT PRIMARY KEY
2. gender VARCHAR(20)
3. contact VARCHAR(15)
4. dob DATE
5. address VARCHAR(30)

## First user interaction 

<img src="Images\firstUserUI.png">

## Main Frame of Student Data Record

<img src="Images\StudentRecord_Frame.png">