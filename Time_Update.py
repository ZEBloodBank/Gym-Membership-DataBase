from psycopg2 import connect
import getpass

# Handles Connection to the database
def connection():
    user = getpass.getuser()
    password = getpass.getpass()

    strConn = "host=csdept dbname=cs236proj user=%s password=%s options='-c search_path=group10,public'" % (user,password)
    
    conn = connect(strConn)
    return conn




def main():
    try:
        conn = connection()
        cursor = conn.cursor()
    except:
        print("Err: Verification Failed")
        exit(-1)


    queryData = handleInput()
    

    cursor.execute(queryData[0], queryData[1])
    conn.commit()
    conn.close()

# Handles Input and returns a List containg both the query and values to be sent via paramatized execution
def handleInput():

    prompt = input("Would you like to change a Class time or a Workout session date?: " )
    Date = ""
    id = ""
    
    # Class prompt
    if prompt.replace(" ", "").lower() == "class":
        query = "UPDATE class SET schedule_time=%s WHERE class_id=%s;"
        Date = input("Give new Schedule time Ex.(2026-06-10 08:00:00): ")
        id = input("What is the Class Id?: ")

    # Workout Session prompt
    if prompt.replace(" ", "").lower() == "workoutsession":
        query = "UPDATE workout_session SET date=%s WHERE session_id=%s;"
        Date = input("Give new Date Ex.(2026-06-10): ")
        id = input("What is the Session Id?: ")
    
    values = (Date, id)

    return [query, values]


main()