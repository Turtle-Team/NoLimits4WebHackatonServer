from flask import Flask, request
from database.handler import DataBase
app = Flask(__name__)
db = DataBase()
@app.route('/register')
def register():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')
    return db.register(name, email, password)

@app.route('/login')
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    return db.login(email, password)

if __name__ == '__main__':
    app.run()
