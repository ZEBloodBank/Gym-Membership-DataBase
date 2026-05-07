# Title: Gym Database Entry
# Contributors: James A. Hall
# Date of creation: 5/6/2026


# Import connection function for DB
from psycopg2 import connect
import getpass
import pandas as pd 
import numpy as np


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
    # can iterate through worksheets. Rightnow will iterate through worksheets
    # though has two checks for data FileNF error, and checking for lack of data.

    # Initializes a List of Dictionaries to store the incoming data.
    sheets = {}

    # Tests to see if the File input exists
    try:
        file = pd.ExcelFile("Gym_Database_Dataset.xlsx")
    except FileNotFoundError:
        print("Error: No File Found!")
        exit(1)
        
    # Iterates throughout the worksheets and adds them to the sheets dictionary.
    for sheet in file.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet)
        
        sheets[sheet] =  df


    # If there were no sheets IE no data and the try Except fails return -1 in case of failure. 
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
    conn = connection()
    cursor = conn.cursor()

    # !! SET UP QUERY LIMITS/CONSTRAIN INCASE OF INJECTION !!
    query = "SELECT * FROM member;"
    cursor.execute(query)


    info = cursor.fetchall()

    print(info)
    
    conn.close()





readInData()