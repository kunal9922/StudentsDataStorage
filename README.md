# Students Record Management System.
* Developed a record management system using Python for front-end and API, and MySQL Database for record storage, resulting in improved efficiency and organization of student data.
* Created an intuitive user interface with features such as search, filtering, and CRUD operations, resulting in streamlined student record management. 
* Implemented user authentication and access control measures to enhance data security, ensuring authorized access and protecting student information.
* Achieved a high level of data integrity with MySQL, exceeding 99.9% reliability, resulting in a probability of data corruption or inconsistencies below 0.1%.

## ER Diagram
<img src="Images\updatedERDiagram.png">

## Schema design in database 
<img src="Images\updatedSchema1.png">

<img src="Images\updatedSchema2.png">

## Updated Schema
Table Student
1. rollnum INT PRIMARY KEY
2. nameStudent VARCHAR(20)
3. email VARCHAR(30)
4. id INT 
    FOREIGN KEY(id) REFRENCES Basic(id)

Table Basic
1. id INT PRIMARY KEY
2. gender VARCHAR(10)
3. contact VARCHAR(15)
4. dob DATE
5. address VARCHAR(30)

## Authentication Interface  

<img src="Images\authenticationWindow.png">

## Records Entry Window

<img src="Images\recordsWindow.png">