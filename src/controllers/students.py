from flask import request,jsonify
from src import app
from src.models.subject import SubjectModel
from src.models.students import StudentsModel
from src.models.session import SessionModel
subjectModel = SubjectModel()
studentsModel = StudentsModel()
sessionModel = SessionModel()
class Objects():
    def studentObject(self,id,iden,name,surname,phone,email,semester):
        return {'id':id,'iden':iden,'name':name,'surname':surname,'phone':phone,'email':email,'semester':semester}

    def subjectObject(self,id,name,semester):
        return {'id':id, 'name':name, 'semester':semester}

  

objects = Objects()


@app.route('/students')
def getStudents():

    students = studentsModel.getStudents()
    arrayStudents = []
    
    for student in students:
        arrayStudents.append(objects.studentObject(student[0],student[1],student[2],student[3],student[4],student[5],student[6]))

    return jsonify(message = 'Estudiantes registrados', students = arrayStudents)



@app.route('/students', methods=['POST'])
def postStudent():

    iden = request.json['iden']
    name = request.json['name']
    surname = request.json['surname']
    phone = request.json['phone']
    email = request.json['email']
    semester = request.json['semester']
    try:
        studentsModel.insertStudent(iden,name,surname, phone,email,semester)
    except:
        return jsonify(message= 'Error')
   # print(iden, name,surname, phone,email, semester)
    student= studentsModel.bringStudent(iden) 

    return jsonify(message='Registrado correctamente', student=objects.studentObject(student[0],student[1],student[2],student[3],student[4],student[5],student[6]))
 



@app.route('/students/<id>',methods=['PUT'])
def putStudent(id):
    student = studentsModel.getStudent(id)
    
    if student is None:
        return jsonify(message='error')   
        
    iden = request.json['iden']
    name = request.json['name']
    surname = request.json['surname']
    phone = request.json['phone']
    email = request.json['email']
    semester = int(request.json['semester']) 

    if iden == '':
        iden = student[1]

    if name == '':
        name = student[2]

    if surname == '':
        surname = student[3]

    if phone == '':
        phone = student[4]

    if email == '':
        email = student[5]

    if semester == '':
        semester = student[6]




    studentsModel.editStudent(iden, name, surname, phone, email, semester, id)
    
    return jsonify(message = 'Editado correctamente', student= objects.studentObject(id,iden, name, surname, phone, email, semester))


@app.route('/students/<id>',methods=['DELETE'])
def deleteStudent(id):

    try:
        studentsModel.deleteStudent(id)
    except:
        return jsonify(message = 'Error')
    return jsonify(message='Eliminado correctamente')



@app.route('/subjects/<id>/students')
def getStudentsSubject(id):
    #subject = subjectModel.bringSubject(id)
    students = studentsModel.bringStudents(id)
    if len(students) == 0:
        return jsonify(message= 'No hay estudiantes matriculados en esta materia...') 

    arrayStudents = []
    for student in students:
        arrayStudents.append(objects.studentObject(student[0],student[1],student[2],student[3],student[4],student[5],student[6]))
    #print(students)
    
    return jsonify(message='Estudiantes registrados',subject=objects.subjectObject(students[0][10],students[0][11],students[0][12]),
    students=arrayStudents)

@app.route('/subjects/<id>/students', methods=['POST'])
def postStudentSubject(id):
    
    subject = subjectModel.bringSubject(id)
    if subject==None:
        return jsonify(message='No existe materia')
    iden = request.json['iden']

    student = studentsModel.bringStudent(iden)
    if student is None:
        return jsonify(message= 'No existe el estudiante')

    studentSubject=studentsModel.bringStudentSubjects(student[0], id)
    if studentSubject is not None:
        return jsonify(message='El estudiante ya esta registrado', student=objects.studentObject(student[0],student[1],student[2],student[3],student[4],student[5],student[6]), subject=objects.subjectObject(subject[0],subject[1],subject[2]))

    studentsModel.insertStudentSubject(student[0], id)
    sessions = sessionModel.bringSessions(id)
    
    for session in sessions:
        sessionModel.insertStudentSessions(student[0],session[0])

    return jsonify(message= 'Estudiante matriculado correctamente', student=objects.studentObject(student[0],student[1],student[2],student[3],student[4],student[5],student[6]), subject=objects.subjectObject(subject[0],subject[1],subject[2]))
    

@app.route('/subjects/<idSub>/students/<int:idStu>', methods=['DELETE'])
def deleteStudentSubjects(idSub,idStu):
    #print(id)   
    print(idSub)  

    studentsModel.deleteStudentSubject(idStu,idSub)

    sessions = sessionModel.bringSessions(idSub)
    
    for session in sessions:
       studentsModel.deleteStudentSessions(idStu,session[0])
       print(session)
    
    return jsonify(message= 'Estudiante eliminado correctamente')
