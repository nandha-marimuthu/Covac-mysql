import mysql.connector
import os
import time
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='vaccine')
myc=mydb.cursor()

def recan(name,aadhar):
  query6= 'select * from appoinment where patient_name=%s and aadhar=%s'
  val6=(name,aadhar)
  myc.execute(query6,val6)
  appoinment = myc.fetchall()
  os.system('cls')
  for row in appoinment:
    print('Appoinment Details')
    print("Appointment id:",row[0])
    print("Name: ", row[1])
    print("Age: ", row[2])
    print("Aadhar: ", row[3])
    print("Vaccination Date: ", row[5])
    print("Dosage: ",row[7])
    print("Center name: ",row[4])
    print("Center id: ",row[8])
    print("Status: ",row[6])
    a = int(input('1 For cancel\n2 For Reshedule\nEnter: '))
    if a == 1:
      print('bidbf')
      from cancel import cancel
      cancel(name,aadhar)

    elif a==2:
      from reshedule import reshedule
      reshedule(name,aadhar)
  