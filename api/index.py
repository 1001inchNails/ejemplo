from flask import Flask,jsonify,request

app = Flask(__name__)

listausers=[
    {"id":1,"nombre":"nombre1"},
    {"id":2,"nombre":"nombre2"},
    {"id":3,"nombre":"nombre3"},
    {"id":4,"nombre":"nombre4"}
]


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/about')
def about():
    return 'About'

@app.route('/api/users',methods=["GET"])
def users():
    return jsonify(listausers)

@app.route('/api/users',methods=["POST"])
def new_users():
    nuevo_user=request.get_json()
    listausers.append(nuevo_user)
    return jsonify(nuevo_user), 201

app.run()