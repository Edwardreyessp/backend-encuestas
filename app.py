from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from questions import questions

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
# Obtención de preguntas
@app.route("/questions", methods=['GET'])
def getQuestion():
    return jsonify(questions)

# Request de tipo de gráficas
@app.route("/questions", methods=['POST'])
def getURL():
    a = request.json
    return "https://www.fundacion-affinity.org/sites/default/files/los-10-sonidos-principales-del-perro.jpg"

# Aviso de subida de archivos a Firebase
@app.route("/files", methods=['POST'])
def addFile():
    fileNames = request.json
    return fileNames

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