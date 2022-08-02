from flask import Flask, jsonify, request

app = Flask(__name__)

from questions import questions

# Config
app.config["UPLOAD_FOLDER"] = "static/files"
ALLOWED_EXTENSIONS = set(["jpg", "docx", "csv", "xlsx"])

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

@app.route("/questions", methods=['POST'])
def getURL():
    return "https://firebasestorage.googleapis.com/v0/b/encuestas-d19ab.appspot.com/o/data_encuestas.csv?alt=media&token=0e0618a2-685b-4c3b-a882-0c3ace622a9c"

@app.route("/files", methods=['POST'])
def addFile():
    fileNames = request.json
    return fileNames

@app.route("/questions/<string:question_name>", methods=['PUT'])
def updateQuestion(question_name):
    question_name = question_name.split('-')
    for clave in questions:
        if clave == question_name[0]:
            questions[clave]['respuestas'][question_name[1]]['respuesta'] = request.json['respuesta']
            questions[clave]['respuestas'][question_name[1]]['color'] = request.json['color']
            return jsonify(questions[clave])
    return 'Question not found'

@app.route("/colors/<string:question_name>", methods=['PUT'])
def updateColor(question_name):
    question_name = question_name.split('-')
    for clave in questions:
        if clave == question_name[0]:
            questions[clave]['respuestas'][question_name[1]]['color'] = request.json['color']
            return jsonify(questions[clave])
    return 'Question not found'

if __name__ == "__main__":
    app.run(debug = False, port=4000)