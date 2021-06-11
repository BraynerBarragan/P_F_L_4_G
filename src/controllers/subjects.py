from flask import  request, jsonify
from src import app
from src.models.subject import SubjectModel
subjectModel = SubjectModel()

@app.route('/subjects')
def getSubjects():
    
    subjects = subjectModel.bringSubjects()
    if len(subjects) == 0:
        return jsonify(message= 'No hay materias registradas...')

    arraySubjects= []
    for subject in subjects:
        arraySubjects.append({
            'id': subject[0],
            'name': subject[1],
            'semester': subject[2]
        })
    
    return jsonify(message= 'Materias registradas:', subjects= arraySubjects)



@app.route('/subjects', methods=['POST'])
def postSubject():

    name = request.json['name']
    semester = int(request.json['semester']) 

    try:
        subjectModel.insertSubject(name, semester)
    except:
        return jsonify(message= 'Error...')
    
    return jsonify(message= 'Guardado correctamente...')



