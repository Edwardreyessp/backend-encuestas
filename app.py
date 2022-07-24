from fileinput import filename
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

from questions import questions

# Config
app.config["UPLOAD_FOLDER"] = "static/files"
ALLOWED_EXTENSIONS = set(["docx", "csv", "xlsx"])

def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

# Routes
@app.route("/questions", methods=['GET'])
def getQuestion():
    return jsonify(questions)

@app.route("/files", methods=['POST'])
def addFile():
    file = request.files["uploadFile"]
    filename = secure_filename(file.filename)
    if file and allowed_file(filename):
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return "File(s) were upload"
    return "FIle not supporting"

@app.route("/questions/<string:question_name>", methods=['PUT'])
def updateQuestion(question_name):
    question_name = question_name.split('-')
    for clave in questions:
        if clave == question_name[0]:
            questions[clave]['respuestas'][question_name[1]] = request.json['respuesta']
            return jsonify(questions[clave])
    return 'Question not found'

if __name__ == "__main__":
    app.run(debug = True, port=4000)