import datetime
import time
import mysql.connector
# from tkinter import *
# from tkcalendar import Calendar
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='vaccine')
myc=mydb.cursor()
print("Welcome to the vaccination portal")
print()

class New_Patient:
    def __init__(self,name,aadhar,email,phone,age,gender,place,dosage):
        self.name=name
        self.aadhar=aadhar
        self.email=email
        self.phone=phone
        self.age=age
        self.gender=gender
        self.place=place
        self.dosage=dosage
    def user_info(self1):
        query1='insert into patient_details(name,aadhar,email,phone,age,gender,place,dosage) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        val=(self1.name,self1.aadhar,self1.email,self1.phone,self1.age,self1.gender,self1.place,self1.dosage)
        myc.execute(query1,val)
        mydb.commit()
        print("Please enter the following medical info")
        height=float(input("Enter height in metres:"))
        weight=int(input("Enter weight in kgs:"))
        bmi=weight/(height**2)
        print("Your BMI {0:.2f}".format(bmi))
        if bmi <18 or bmi>25:
            print("Please consult a doctor before vaccination")
            print("Do you want to continue ?")
            c=input().strip()
            if c=='no':
                exit()
        print("Do you have any medical records ?")
        print("Do you have BP or diabetes or a heart patient or undergone any major surgery? yes or no")
        medical=input().strip()
        if medical=='yes':
            print("Sorry ! You cannot be vaccinated . Please consult a doctor")
            exit()
        if self1.gender=="Female":
            print("Are you a pregnant woman ?")
            preg=input().strip()
            if preg=='yes':
                print("Sorry ! You cannot be vaccinated . Please consult a doctor")
                exit()
        print()
        print("You can choose your vaccination center by city/pincode")
        print("Available regions in Tamil Nadu")
        print("********************************")
        print("1.Chennai\n2.Trichy\n3.Madurai\n4.Coimbatore\n5.Salem")
        print("********************************")
        pref_region=input("Enter preferred region:")
        query2="""select * from vcenter where region=%s"""
        val2=(pref_region,)
        myc.execute(query2,val2)
        vcenter = myc.fetchall()
        for row in vcenter:
                print("vcid: ", row[0])
                print("Name: ", row[1])
                print("region: ", row[2])
                print("pincode: ", row[3])
                print("\n")
        print("Select the vaccine center by choosing the vcid")
        vcid=int(input("Enter preferred vaccine center id:"))
        hosp_name=input("Enter the center name:")
        status="Scheduled"
        myc.execute('select date_add(curdate(),interval 2 day)')
        data = myc.fetchall()
        md = data[0][0]


        query3='insert into appoinment(patient_name,age,aadhar,center,date,status,dosage,center_id) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        val3=(self1.name,self1.age,self1.aadhar,hosp_name,md,status,self1.dosage,vcid)
        myc.execute(query3,val3)
        mydb.commit()
        print()
        print("Processing your details")
        print("Your final Booking Details for vaccination")
        query5="select * from appoinment where aadhar=%s"
        val5=(self1.aadhar,)
        myc.execute(query5,val5)
        appoinment = myc.fetchall()
        print()
        #to b printed as well as mailed
        for row in appoinment:
                print("Appointment id:",row[0])
                print("Name: ", row[1])
                print("Age: ", row[2])
                print("Aadhar: ", row[3])
                print("Vaccination Date: ", row[5])
                print("Dosage: ",row[7])
                print("Center name: ",row[4])
                print("Center id: ",row[8])
                print("Status: ",row[6])
                print()
        print("Your vaccination has been booked. Please be available on the date")
        print("Stay home stay safe")
        

            




    
    

