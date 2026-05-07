# Title: Gym Database Entry
# Contributors: James A. Hall
# Date of creation: 05/06/2026


# Import connection function for DB
from psycopg2 import connect
import getpass
import pandas as pd 
import numpy as np
import sys


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
    elif (sys.argv[1] == "-a"):
        adminInput()

            
    # !! SET UP QUERY LIMITS/CONSTRAIN INCASE OF INJECTION !!
    query = "SELECT * FROM member;"
    cursor.execute(query)


    info = cursor.fetchall()

    print(data)
    
    conn.close()





entry()