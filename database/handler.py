import mysql.connector
import setting
import json
class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(database=setting.DATABASE['basename'],
                                           user=setting.DATABASE['login'],
                                           host=setting.DATABASE['ip'],
                                           password=setting.DATABASE['password'])
        self.cursor = self.connection.cursor()

    def register(self, login, email, password, name, age, sex):
        try:
            sql = '''INSERT INTO users(id_user, login, email, password, name, age, sex) VALUES (?, ?, ?, ?, ?, ?, ?)'''
            self.cursor.execute(sql, (0, login, email, password, name, age, sex))
            self.connection.commit()
            sql2 = '''SELECT * FROM users WHERE login = ?'''
            self.cursor.execute(sql2, (login,))
            user_data = self.cursor.fetchone()
            user = {
                'id_user': user_data[0],
                'login': user_data[1],
                'email': user_data[2],
                'password': user_data[3],
                'name': user_data[4],
                'age': user_data[5],
                'sex': user_data[6]
            }
            return json.dumps(user)
        except:
            return json.dumps({'error': 'Failed to register user'})


    def login(self, login, password):
        sql = '''SELECT id_user, login, email, password, name, age, sex FROM users WHERE login=%s AND password=%s'''
        self.cursor.execute(sql, (login, password))
        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return 'Error, not data...'

