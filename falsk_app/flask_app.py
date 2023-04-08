from flask import Flask, request
import database.handler

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    id_user = request.args.get('id_user')
    login_u = request.args.get('login')
    email = request.args.get('email')
    password = request.args.get('password')
    name = request.args.get('name')
    age = request.args.get('age')
    sex = request.args.get('sex')
    return database.handler.DataBase().register(id_user=id_user, login=login_u, email=email, password=password, name=name, age=age, sex=sex)

@app.route('/login', methods=['GET'])
def login():
    login_u = request.args.get('login')
    password = request.args.get('password')
    return database.handler.DataBase().login(login=login_u, password=password)


