import mysql.connector
import os

mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku')
mycursor=mydb.cursor()
mycursor.execute('use vaccine')

#login for staff
def staff_login():
  s = input('Staffname: ')
  p = input('Password: ')
  mycursor.execute('select vcid from vac_staff where name = %s and pass = %s ',(s,p))
  data = mycursor.fetchall()
  if data:
    vaccinate(s)
  else:
    print('Invalid Id or Password')

#staff entering the patients details to register them as vaccinated
def vaccinate():
  os.system('cls')
  n = input('Patientname: ')
  v = int(input('Vaccination Id: '))
  mycursor.execute('select age from appoinment where aid = %s and patient_name = %s ',(v,n))
  data = mycursor.fetchall()
  if data:
    age = data[0][0]
    s = input('Proceed to vacinate(y/n): ')
    if(s == 'y'):
      mycursor.execute('select curdate()')
      date1 =  mycursor.fetchall()
      date = date1[0][0]
      a = 'insert into vaccinated(aid,patient_name,age,staff,date) values(%s,%s,%s,%s,%s)'
      mycursor.execute(a,(v,n,age,n,date))
      mydb.commit()
      mycursor.execute('delete from appoinment where aid = %s and patient_name = %s',(v,n))
      mydb.commit()
      print('Vacination sucessful !')


staff_login()