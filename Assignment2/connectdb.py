import mysql.connector
conn = mysql.connector.connect(host='localhost',password='NainaJha4@',user='root')
if conn.is_connected():
   print("connection successful...")