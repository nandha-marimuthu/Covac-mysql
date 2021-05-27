import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku')
mycursor=mydb.cursor()
mycursor.execute('use vaccine')

def admin_login():
  n = input('Staffname: ')
  p = input('Password: ')
  mycursor.execute('select * from web_admin where id = %s and pass = %s ',(n,p))
  data = mycursor.fetchall()
  if data:
    print('Add centers and staffs')
    add_center()
  else:
    print('Invalid Id or Password')

def add_center():
  name = input('Center name: ')
  region = input('Center region')
  pin = input('Pincode: ')
  avail = input('Availablity: ')
  q = 'insert into vcenter(name,region,pincode,availablity) values(%s,%s,%s,%s)'
  v = (name,region,pin,avail)
  mycursor.execute(q,v)
  mydb.commit()
  print('The Staff Details')
  q = 'select vcid from vcenter where name = %s'




