from flask import Flask, request
import database.handler

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')
    return database.handler.DataBase().register(name, email, password)

@app.route('/login', methods=['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    return database.handler.DataBase().login(email, password)


@app.route('/pop', methods=['POST'])
def pop():
    return database.handler.DataBase().pop(request.args.get('id'))

