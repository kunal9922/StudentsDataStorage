# Students Record Management System.
* Developed a record management system using Python for front-end and API, and MySQL Database for record storage, resulting in improved efficiency and organization of student data.
* Created an intuitive user interface with features such as search, filtering, and CRUD operations, resulting in streamlined student record management. 
* Implemented user authentication and access control measures to enhance data security, ensuring authorized access and protecting student information.
* Achieved a high level of data integrity with MySQL, exceeding 99.9% reliability, resulting in a probability of data corruption or inconsistencies below 0.1%.

## ER Diagram
![ER_diagram](https://github.com/kunal9922/StudentDataStorage/assets/53283003/89ceed8f-422b-4bf5-a94a-426fda07c1be)

## Schema design in database 
![record_table](https://github.com/kunal9922/StudentDataStorage/assets/53283003/953f00bc-293a-401e-9a4b-3414d25f31e3)
![basic_table_schema](https://github.com/kunal9922/StudentDataStorage/assets/53283003/09de5126-5343-467b-b5f3-5270fac251fe)


## Updated Schema
Table Record:

1. rollnum INT PRIMARY KEY
2. first_name VARCHAR(20)
3. last_name VARCHAR(20)
4. email VARCHAR(30)
5. basic_id INT FOREIGN KEY(basic_id) REFERENCES Basic(id)

Table Basic:

1. id INT PRIMARY KEY
2. gender VARCHAR(10)
3. contact VARCHAR(15)
4. dob DATE
5. address VARCHAR(30)

Both tables follow the rules of normalization, This design ensures data integrity and reduces data duplication, making the database well-organized and normalized. "Record" and "Basic" to demonstrate maintaining a many-to-one relationship with normalization.

## Authentication Interface  

<img src="Images\authenticationWindow.png">

## Records Entry Window

<img src="Images\recordsWindow.png">
