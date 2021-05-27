import mysql.connector
import os
import time
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='vaccine')
myc=mydb.cursor()
def cancel(name,aadhar):
  a = input('Cancelling the  confirmation(Press any key and enter): ')
  if a:
    myc.execute('delete from appoinment  where patient_name = %s and aadhar = %s',(name,aadhar))
    mydb.commit()
    print("Your vaccination appointment has been cancelled")
    print("Stay home stay safe")
