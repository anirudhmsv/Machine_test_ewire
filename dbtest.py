import mysql.connector

def dbconnection_qrlogin():
    mydb = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,
            user="",
            password="",
            database=""
        )
    cur = mydb.cursor()
    return cur
  

# try:
#     cur, mydb = dbconnection_qrlogin()  


#     if cur is not None:
#         cur.execute("SELECT * FROM users WHERE custid = '75859501000422'")
#         rows = cur.fetchall()
#         print("ROWS " + str(rows))
#         cur.close()
#     if mydb is not None:
#         mydb.close()  # Close the database connection
# except Exception as error:
#     print(f"error:::::::::::::::::::: {error}")


try:
    cur, mydb = dbconnection_qrlogin()
    # Unpack both cursor and connection
    cur.execute("SELECT * FROM users WHERE custid = '75859501000422'")
    rows = cur.fetchall()
    print("ROWS " + str(rows))
except Exception as error:
    if 'cur' in locals() and type(cur) is not str:
        cur.close()
    print(f" error::::::::::: {error}")
finally:
    if 'mydb' in locals():
        mydb.close()


    # exception handling in connection  I added the mydb variable to the return statement of dbconnection_qrlogin and adjusted the assignment accordingly.
    #  i added a try-except block to handle such exceptions.
    # i added a finally block to ensure that the database connection is closed... even if an exception occurs.


