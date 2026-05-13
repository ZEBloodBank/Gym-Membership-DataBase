# Gym Management Database (School)
A rough blue-print into a bare-bones Gym DB with two python programs.

EXCLAIMER -- THIS IS NOT A REAL DATABASE NOR IS IT A TESTER 

## Schema
- member(member_id, first_name, last_name, plan_id)
- email(member_id, email) -- Multivariate attribute of the Member entity
- membership_plan(plan_id, plan_name, price, plan_duration)
- equipment(equipment_id, equipment_name, type, status)
- workout_session(session_id, date, session_duration, member_id, trainer_id)
- trainer(trainer_id, first_name, last_name, specialty)

## Required Imports
- psycopg2
- getpass
- pandas
- numpy

## Rundown
Simple Python programs that use and alter a school
created database handling Insertions as well as,
data alteration.

## Important
The Dataset provided is obviously a test set
no real names and/or people were used to test data 
inserstion or DB managment.

## DB_ENTRY
This program is intended to take a formatted Excel file and read it into
the database, while also handling Name Splitting the Member and Trainer files
given that in the database it is required that the names is split into First and Last
as practice
