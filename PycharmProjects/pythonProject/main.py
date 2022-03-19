import mysql.connector

sql='Insert into customers(name,address) values(%s,%s)'
mycursor = conn.cursor()
nm=input('enter name')
ad=input('enter address')
para=(nm,ad)
try:
    mycursor.execute(sql,para)
    conn.commit()
    '''row=mycursor.fetchone()
    while row is not None:
        print(row)
        row=myc.fetchone()'''
    print(mycursor.rowcount, 'Row inserted')
except:
    conn.rollback()
    print('Unable to show data')
mycursor.close()
conn.close()




