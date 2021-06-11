
from flask import request
from flask.json import jsonify
from src import app
from src.models.subject import SubjectModel
from src.models.students import StudentsModel
from src.models.session import SessionModel
from src.controllers.students import Objects
subjectModel = SubjectModel()
sessionModel = SessionModel()
studentsModel = StudentsModel()
objects= Objects()

def objectSession(id, name, description, date, startTime, endTime):
    return {'id':id, 'name':name, 'description':description, 'date':date,'startTime':startTime, 'endTime':endTime}


@app.route('/subjects/<subId>/sessions')
def getSessions(subId):
    sessions = sessionModel.bringSessions(subId)
    subject = subjectModel.bringSubject(subId)

    if subject is None:
        return jsonify(message='No existe materia')
    
    #date = datetime.timedelta(sessions[0][6]) 
    arraySessions = []
    for session in sessions:
       
        #date = str(session[4].year)+'/'+str(session[4].month)+'/'+str(session[4].day)

        arraySessions.append(objectSession(session[0],session[2],session[3],session[4].strftime("%x"),str(session[5]),str(session[6])))
   # print(date)
    print(arraySessions)
    return jsonify(message='Sesiones registradas', sessions=arraySessions, subject=objects.subjectObject(subject[0],subject[1],subject[2]))
    #return jsonify(message='sessionnn')



@app.route('/subjects/<id>/sessions', methods=['POST'])
def postSession(id):


    name = request.json['name']
    subject = id
    description = request.json['description']
    date = request.json['date']
    startTime = request.json['startTime']
    endTime = request.json['endTime']
    print(name, subject, description, date, startTime, endTime)
    
  
    sessionModel.insertSession(subject, name, description, date, startTime, endTime)
    
    students = studentsModel.bringStudents(subject)
    session = sessionModel.bringSession()
    for student in students:
        sessionModel.insertStudentSessions(student[0],session[0])
    
    print(students)
    print(session)

    subject = subjectModel.bringSubject(id)
    return jsonify(message= 'Registrado correctamente', session= objectSession(session[0],name, description, date, startTime, endTime),subject=objects.subjectObject(subject[0],subject[1],subject[2]))
    
@app.route('/sessions/<id>/students')
def sessionAttendance(id):
    students = sessionModel.bringStudentsSession(id)
    #subject = subjectModel.bringSubject(subId)
    #print(students)
    arrayStudents = []
    for student in students:
        if student[9] == 2:
            attedance = 'http://127.0.0.1:5100/sessions/'+str(student[10])+'/confstudents'
        else:
            attedance = student[9]

        if attedance == 1:
            attedance = 'Asistencia confirmada'

        arrayStudents.append({'id':student[0],'iden':student[2],'name':student[3],'surname':student[4],'phone':student[5],'email':student[6],'semester':student[7], 'attendance':attedance})
    return jsonify(students = arrayStudents)


@app.route('/sessions/<id>/confstudents',methods=['PUT'])
def sessionStudentConfirm(id):
 
    sessionModel.updateAttendance(1,id)
    
    return jsonify(message="Asistencia confirmada")


