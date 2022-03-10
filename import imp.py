import pyfirmata
import mysql.connector
import datetime
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="elev",
    database="adafruit"
    )

board = pyfirmata.Arduino('COM4')
analog_input = board.get_pin ('a:0:i')
digital_output = board.get_pin ('d:12:o')

mycursor = mydb.cursor()
print("Connected..")

sql = "INSERT INTO sensor(verdi,tid) VALUES (%s,%s)"

verdi = analog_input.read()
tid = datetime.datetime.now()

val = (verdi, tid)

print("Executing...")



print("Done")




it =  pyfirmata.util.Iterator(board)
it.start()



while True:
    verdi = analog_input.read()
    print(verdi)
    time.sleep(1)
    val = (verdi, tid)
    mycursor.execute(sql, val)
    mydb.commit()
