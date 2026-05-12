# Title: Gym Database Entry
# Contributors: James A. Hall
# Date of creation: 05/06/2026


# Import connection function for DB
from psycopg2 import connect
from psycopg2 import sql
import getpass
import pandas as pd 
import numpy as np
import sys
import time


# Logs admin into database
def connection():
    # Hides the user Password when asking for it from the user.
    user = getpass.getuser()
    password = getpass.getpass()

    # Writing of the connection request string. 
    strConn = "host=csdept dbname=cs236proj user=%s password=%s options='-c search_path=group10,public'" % (user, password)
    

    conn = connect(strConn)
    return conn

# Reads Data from an Excel file to put into the data base. Return a dictionary of all the worksheets in the Excel file. 
def readInData():

    # Handles incoming data by reading them from a provided Excel file.
    # can iterate through worksheets. Right now will iterate through worksheets
    # though has two checks for data FileNF error, and checking for lack of data.

    # Initializes a List of Dictionaries to store the incoming data.
    sheets = {}

    # Tests to see if the File input exists if not Error.
    # Then grabs the Excel File to iterate through.
    try:
        file = pd.ExcelFile("Gym_Database_Dataset.xlsx")
    except FileNotFoundError:
        print("Error: No File Found!")
        exit(1)
        
    # Iterates throughout the worksheets and adds them to the sheets dictionary.
    for sheet in file.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet)
        
        sheets[sheet] =  df


    # If there were no sheets IE no data and the try Except fails return -1 in case of Lacking Data. 
    if (len(sheets) < 1):
        return -1
    
    file.close()
    return sheets

def adminInput():
    
    # Create a INPUT system that allows and prints
    # prompts for an Admin to add individual data
    # to provided table via the Admin. Again data
    # should be authenticated in the DB. 
    
    return -1


# Handles the Insertion of the Data into the Database !! NEED TO CHECK AND SEE IF THEY ALREADY EXIST IF THEY DO, DO NOT ADD !!
def entry():
    
    try:
        conn = connection()
        cursor = conn.cursor()
    except:
        print("Error: Verification Failed")
        exit(-1)

    if (len(sys.argv) < 2):
        print("Error: Not Enough arguments")
        exit(1)
    elif (len(sys.argv) > 4):
        print("Error: Too many arguments")
        exit(1)
    
    if(sys.argv[1] == "-r"):
        data = readInData()
        test = list(data)
        start_time = time.perf_counter()
    
        for sheet in data:
            attributes = list(data[sheet])
            currData = list(map(lambda x: tuple(x), np.array(data[sheet])))
            
            if sheet.lower() == 'member' or sheet.lower() == 'trainer':
                names = list(map(lambda x: x[1].split(), currData))
                for i in range(len(currData)):
                    temp = list(currData[i])
                    temp[1:2] = names[i]
                    currData[i] = tuple(temp)
                    print(currData[i])

            

        end_time = time.perf_counter()

    elif (sys.argv[1] == "-a"):
        data =  adminInput()




    print(f"Elpased time: {end_time - start_time:.4f} seconds")
    # !! SET UP QUERY LIMITS/CONSTRAIN INCASE OF INJECTION !!
    query = "SELECT * FROM member;"
    cursor.execute(query)


    info = cursor.fetchall()

    #print(data)
    
    conn.close()

def queryFormat(sheetName):
    
    if sheetName.lower() == 'member': query = "INSERT INTO member (member_id, first_name, last_name, email, plan_id) VALUES (%s, %s, %s, %s, %s)"
    if sheetName.lower() == 'trainer': query = "INSERT INTO trainer (trainer_id, first_name, last_name, specialty) VALUES (%s, %s, %s, %s)"
    if sheetName.lower() == 'workoutsession': query = "INSERT INTO workout_session (session_id, date, session_duration, member_id, trainer_id) VALUES (%s, %s, %s, %s, %s)"
    if sheetName.lower() == 'membership': query = "INSERT INTO membership_plan (plan_id, plan_name, price, plan_duration) VALUES (%s, %s, %s, %s)"
    if sheetName.lower() == 'equipment': query = "INSERT INTO equipment (equipment_id, equipment_name, type, status) VALUES (%s, %s, %s, %s)"
    

    
    return query



entry()