import mysql.connector
conn = mysql.connector.connect(host='localhost',password='NainaJha4@',user='root')
mycursor=conn.cursor()
mycursor.execute("create table if not exists Assignment2.ExamRegistration_Table(RegistrationID INT PRIMARY KEY,Student_id INT,Exam_id INT,FOREIGN KEY (Student_id) REFERENCES student_Table(Student_id),FOREIGN KEY (Exam_id) REFERENCES Exam_Table(Exam_id),RegistrationDate DATE);")
conn.close()