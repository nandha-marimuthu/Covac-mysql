import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='vaccine')
myc=mydb.cursor()

def reshedule(name,aadhar):
  myc.execute('select date_add(curdate(),interval 2 day)')
  data = myc.fetchall()
  md = data[0][0]
  print('Your Resheduled date is: ',md)
  a = input('Reshedule confirmation(Press any key and enter): ')
  if a:
    myc.execute('update appoinment set date = %s , status = %s where patient_name = %s and aadhar = %s',(md,'Resheduled',name,aadhar))
    mydb.commit()
    print("Your vaccination appointment has been resheduled")
    print("Stay home stay safe")



