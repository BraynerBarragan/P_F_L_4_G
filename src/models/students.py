from src.config.db import DB

class StudentsModel():
    def getStudents(self):
        cursor = DB.cursor()
        cursor.execute('select * from students')
        students = cursor.fetchall()
        cursor.close()
        if students is not None:
            students = students
        return students

    def bringStudents(self, id):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM students INNER JOIN student_subjects AS s_s ON students.id = s_s.student_id INNER JOIN subjects ON s_s.subject_id = subjects.id WHERE subjects.id = ?',(id,))
        students = cursor.fetchall()
        cursor.close()
        return students

    def bringStudent(self, id):
        cursor = DB.cursor()
        cursor.execute('select * from students where idn = ?',(id,))
        student = cursor.fetchone()
        cursor.close()
        return student

    def getStudent(self, id):
        cursor = DB.cursor()
        cursor.execute('select * from students where id = ?',(id,))
        student = cursor.fetchone()
        cursor.close()
        return student

    def bringStudentSubjects(selef, studentId, subjectId):
        cursor = DB.cursor()
        cursor.execute('select * from student_subjects where student_id = ? and subject_id = ?',(studentId, subjectId,))
        studentSubjects = cursor.fetchone()
        cursor.close()
        return studentSubjects 

    def insertStudent(self, idn, name, surname, phone, email, semester):
        cursor = DB.cursor()
        cursor.execute('insert into students(idn, name, surname, phone, email, semester) values(?, ?, ?, ?, ?,?)',(idn, name, surname, phone, email, semester,))
        cursor.close()

    def insertStudentSubject(self, studentId, subjectId):
        cursor = DB.cursor()
        cursor.execute('insert into student_subjects(student_id, subject_id) values(?,?)',(studentId, subjectId,))
        cursor.close()

    def editStudent(self, idn, name, surname, phone, email, semester, id):
        cursor = DB.cursor()
        cursor.execute('update students set idn = ?, name = ?, surname = ?, phone = ?, email  = ?, semester = ? where id = ?',(idn, name, surname, phone, email, semester, id,))
        cursor.close()
    
    def deleteStudentSubject(self, idStu, idSub):
        cursor = DB.cursor()
        cursor.execute('delete from student_subjects where student_id = ? and subject_id = ?',(idStu, idSub,))
        cursor.close()

    def deleteStudentSessions(self, idStudent, idSession):
        cursor = DB.cursor()
        cursor.execute('delete from student_sessions where student_id = ? and session_id = ?',(idStudent,idSession,))
        cursor.close()

    def deleteStudent(self, id):
        cursor = DB.cursor()
        cursor.execute('delete from students where id = ?',(id,))
        cursor.close()

