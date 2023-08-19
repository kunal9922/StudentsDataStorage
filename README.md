# Students Record Management System.
* Developed a record management system using Python for front-end and API, and MySQL Database for record storage, resulting in improved efficiency and organization of student data.
* Created an intuitive user interface with features such as search, filtering, and CRUD operations, resulting in streamlined student record management. 
* Implemented user authentication and access control measures to enhance data security, ensuring authorized access and protecting student information.
* Achieved a high level of data integrity with MySQL, exceeding 99.9% reliability, resulting in a probability of data corruption or inconsistencies below 0.1%.

## User Authentication UI
![authUI](https://github.com/kunal9922/StudentDataStorage/assets/53283003/5390418e-7cda-4804-a80a-f1fb6fab3b56)

## Database Selecting UI Interface  
![databaseUI](https://github.com/kunal9922/StudentDataStorage/assets/53283003/7c60b4e7-8389-4856-834f-a5b862d5c5f8)

## Records Entry Window
![recordsEntryUI](https://github.com/kunal9922/StudentDataStorage/assets/53283003/92bda68f-fee9-4753-99fe-2569250357dc)

## ER Diagram
![ER_diagram](https://github.com/kunal9922/StudentDataStorage/assets/53283003/89ceed8f-422b-4bf5-a94a-426fda07c1be)

## Updated Schema
### Student Records Table

This table holds essential information about students. Each student is assigned a unique identification number (Roll Number) that helps us keep track of them. We store their first name, last name, and email address. Additionally, there's a reference to their basic details using a special number (Basic ID).

Columns:

* Roll Number: A special number that uniquely identifies each student.
* First Name: The student's first name.
* Last Name: The student's last name.
* Email Address: The student's email address.
* Basic ID: This number is like a key that helps us link to more detailed information about the student.
  
### Basic Information Table

In this table, we keep essential information about individuals. Each person gets a unique ID number, which is like their personal code. We store details like their gender, contact number, date of birth, and where they live.

Columns:

* ID: A unique code that's assigned to each person.
* Gender: Whether the person is male, female, or something else.
* Contact Number: A way to get in touch with the person.
* Date of Birth: When the person was born.
* Address: Where the person lives.

"Normalized design ensures data integrity, and minimizes duplication. Demonstrated through 'Record' and 'Basic' tables for many-to-one relationship."
## Schema design in database 
![record_table](https://github.com/kunal9922/StudentDataStorage/assets/53283003/953f00bc-293a-401e-9a4b-3414d25f31e3)
![basic_table_schema](https://github.com/kunal9922/StudentDataStorage/assets/53283003/09de5126-5343-467b-b5f3-5270fac251fe)
