from src.config.db import DB

class SessionModel():

    def insertSession(self,subjectId, name, description, date, startTime, endTime):

        cursor = DB.cursor()
        cursor.execute('insert into sessions(subject_id, name, description, date, start_time, end_time) values(?, ?, ?, ?, ?, ?)',(subjectId, name, description, date, startTime, endTime,))

        cursor.close()

    def bringSession(self):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM sessions WHERE id = (SELECT MAX(id) FROM sessions)')
        session = cursor.fetchone()
        cursor.close()
        return session

    def bringSessions(self, subjectId):
        cursor = DB.cursor()
        cursor.execute('select * from sessions where subject_id = ?',(subjectId,))
        sessions = cursor.fetchall()
        cursor.close()
        return sessions

    def insertStudentSessions(self, studentId, sessionId):
        cursor = DB.cursor()
        cursor.execute('insert into student_sessions(student_id, session_id) values(?, ?)',(studentId, sessionId))
        cursor.close()

    def bringStudentsSession(self, sessionId):
        cursor = DB.cursor()
        cursor.execute('SELECT students.id, st_se.id, students.idn, students.name, students.surname, students.phone, students.email, students.semester, sessions.name,  st_se.check_attendance,st_se.id,sessions.id FROM students INNER JOIN student_sessions AS st_se ON students.id = st_se.student_id INNER JOIN sessions ON st_se.session_id = sessions.id WHERE sessions.id = ?',(sessionId,))
        students = cursor.fetchall()
        return students

    def updateAttendance(self, check,id):
        cursor = DB.cursor()
        cursor.execute('update student_sessions set check_attendance = ? where id = ?',(check,id))
        cursor.close()


     