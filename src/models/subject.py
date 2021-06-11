from src.config.db import DB

class SubjectModel():

    def bringSubjects(self):
        cursor = DB.cursor()
        cursor.execute('select * from subjects')
        subjects = cursor.fetchall()
        cursor.close()
        return subjects

    def bringSubject(self,id):
        cursor = DB.cursor()
        cursor.execute('select * from subjects where id = ?',(id,))
        subject = cursor.fetchone()
        cursor.close()
        
        if subject is not None:
            subject = subject
        return subject

    def insertSubject(self, name, semester):
        cursor = DB.cursor()
        cursor.execute('insert into subjects(name, semester) values(?, ?)',(name, semester))
        cursor.close()
        
