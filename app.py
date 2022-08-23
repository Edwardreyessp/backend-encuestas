from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)

from questions import questions
url = ''

# Config
# app.config["UPLOAD_FOLDER"] = "static/files"
# ALLOWED_EXTENSIONS = set(["jpg", "docx", "csv", "xlsx"])

# def allowed_file(file):
#     file = file.split('.')
#     if file[1] in ALLOWED_EXTENSIONS:
#         return True
#     else:
#         return False

# Routes
# Aviso de subida de archivos a Firebase
@cross_origin
@app.route("/files", methods=['POST'])
def addFile():
    url = request.json
    return url['word']

# Obtención de preguntas
@cross_origin
@app.route("/questions", methods=['GET'])
def getQuestion():
    print(url)
    return jsonify(questions)

# Request de tipo de gráficas
@cross_origin
@app.route("/questions", methods=['POST'])
def getURL():
    a = request.json
    return "https://www.fundacion-affinity.org/sites/default/files/los-10-sonidos-principales-del-perro.jpg"

# Descontinuado
# @app.route("/questions/<string:question_name>", methods=['PUT'])
# def updateQuestion(question_name):
#     question_name = question_name.split('-')
#     for clave in questions:
#         if clave == question_name[0]:
#             questions[clave]['respuestas'][question_name[1]]['respuesta'] = request.json['respuesta']
#             questions[clave]['respuestas'][question_name[1]]['color'] = request.json['color']
#             return jsonify(questions)
#     return 'Question not found'

if __name__ == "__main__":
    app.run(debug = False, port=4000)