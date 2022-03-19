import mysql.connector

conn = mysql.connector.connect(user='root', password='Adarsh@231096', host='localhost', database='Adarsh', port=3306)
try:
    if conn.is_connected():
        print('server connected')
except:
    print('unable to connect')

# sql='CREATE TABLE emp (id int AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),fees FLOAT)'
sql = 'insert into emp(id,name,fees) values(%s,%s,%s)'
idd = int(input('id'))
nm = input('enter name :')
fe = float(input('enter fees :'))
para = (idd, nm, fe)
mycur = conn.cursor()
mycur.execute(sql, para)
conn.commit()

mycur.close()
conn.close()
