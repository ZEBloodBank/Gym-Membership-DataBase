
# Import connection function for DB
from psycopg2 import connect
import getpass


# Logs admin into database
def connection():
    user = getpass.getuser()
    password = getpass.getpass()

    strConn = "host=csdept dbname=cs236proj user=%s password=%s options='-c search_path=group10,public'" % (user, password)
    

    conn = connect(strConn)
    return conn


def entry():
    conn = connection()
    cursor = conn.cursor()

    query = "SELECT * FROM member;"
    cursor.execute(query)
    
    info = cursor.fetchall()

    print(info)
    
    conn.close()





entry()