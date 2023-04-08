import mysql.connector
import setting
class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(database=setting.DATABASE['basename'],
                                           user=setting.DATABASE['login'],
                                           host=setting.DATABASE['ip'],
                                           password=setting.DATABASE['password'])
        self.cursor = self.connection.cursor()

    def register(self, id_user, login, email, password, name, age, sex):
        sql = '''INSERT INTO users(id_user, login, email, password, name, age, sex) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        self.cursor.execute(sql, (id_user, login, email, password, name, age, sex))
        if self.connection.commit():
            return (id_user, login, email, password, name, age, sex)
        else:
            return 'Error, not data...'

    def login(self, login, password):
        sql = '''SELECT id_user, login, email, password, name, age, sex FROM users WHERE login=%s'''
        self.cursor.execute(sql, (login, ))
        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return 'Error, not data...'

