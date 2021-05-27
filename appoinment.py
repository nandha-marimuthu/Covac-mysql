import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='vaccine')
myc=mydb.cursor()

name=input("Please enter your name:")
aadhar=int(input("Enter your 12 digit adhaar number:"))
myc.execute('select * from appoinment where patient_name=%s and aadhar=%s',(name,aadhar))
data = myc.fetchall()
if data:
  from recan import recan
  recan(name,aadhar)
else:
  email=input("Enter your email id:").strip()
  phone=int(input("Enter your mobile number:"))
  age=int(input("Enter your age:"))
  if age <=18:
      print("You must be above 18 years to get vaccinated")
      exit()
  gender=input("Enter gender:")
  place=input("Enter address:").strip()
  dosage=int(input("Enter 1 for 1st dose and 2 for 2nd dose:"))
  from user_details import New_Patient
  a=New_Patient(name,aadhar,email,phone,age,gender,place,dosage)
  a.user_info()
