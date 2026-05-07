
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

# Reads Data from an Excel file to put into the data base.
def readInData():

    # Initializes a List of Dictionaries to store the incoming data.
    sheets = []

    # Tests to see if the File input exists
    try:
        file = pd.ExcelFile("Gym_Database_Dataset.xlsx")
    except FileNotFoundError:
        print("Error: No File Found!")
        exit(1)
        
    # Iterates throughout the worksheets and adds them to the sheets List.
    for sheet in file.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet)
        
        sheets.append(dict(df))


    # If there were no sheets IE no data and the try Except fails return -1 in case of failure. 
    if (len(sheets) < 1):
        return -1
    
    file.close()
    return sheets


def entry():
    conn = connection()
    cursor = conn.cursor()

    
    query = "SELECT * FROM member;"
    cursor.execute(query)


    info = cursor.fetchall()

    print(info)
    
    conn.close()





readInData()