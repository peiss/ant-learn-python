import flask

app = flask.Flask(__name__)

@app.route("/hello")
def hello():
    return "hello flask"

@app.route("/get_grades")
def get_grades():
    grades = []
    with open("input.txt") as fin:
        for line in fin:
            line = line.strip()
            fields = line.split("\t")
            grades.append(fields)
    import json
    return json.dumps(grades)

@app.route("/get_grade_byid/<sid>")
def get_grade_byid(sid):
    grades = []
    with open("input.txt") as fin:
        for line in fin:
            line = line.strip()
            fields = line.split("\t")
            if str(sid) == fields[0]:
                grades.append(fields)
    import json
    return json.dumps(grades)

app.run()