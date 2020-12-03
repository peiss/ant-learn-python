import flask
import json
import random

app = flask.Flask(__name__)

data = {
    "001": {"sno": "001", "sname": "小明", "sage": 20},
    "002": {"sno": "002", "sname": "小李", "sage": 22},
    "003": {"sno": "003", "sname": "小王", "sage": 21},
    "004": {"sno": "004", "sname": "小光", "sage": 19},
    "005": {"sno": "005", "sname": "小刚", "sage": 18},
    "006": {"sno": "006", "sname": "小马", "sage": 16},
    "007": {"sno": "007", "sname": "小黄", "sage": 20},
    "008": {"sno": "008", "sname": "小蛋", "sage": 22},
    "009": {"sno": "009", "sname": "小哈", "sage": 20},
}


@app.route("/student/info/<sid>")
def index(sid):
    return json.dumps(data[sid])


app.run()
