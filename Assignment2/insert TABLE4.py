import mysql.connector
conn = mysql.connector.connect(host='localhost',password='NainaJha4@',user='root')
mycursor=conn.cursor()
mycursor.execute('insert into Assignment2.Faculty_Table values ();')
mycursor.execute('insert into Assignment2.Faculty_Table values ();')
mycursor.execute('insert into Assignment2.Faculty_Table values ();')
mycursor.execute('insert into Assignment2.Faculty_Table values ();')
mycursor.execute('insert into Assignment2.Faculty_Table values ();')
mycursor.execute('insert into Assignment2.Faculty_Table values ();')
mycursor.execute('insert into Assignment2.Faculty_Table values ();')
mycursor.execute('insert into Assignment2.Faculty_Table values ();')
conn.commit()