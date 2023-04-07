import mysql.connector
import setting
class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(database=setting.DATABASE['basename'],
                                           user=setting.DATABASE['login'],
                                           password=setting.DATABASE['password'],
                                           port=5432)
        self.cursor = self.connection.cursor()

    def login(self, email, password):
        try:
            sql = '''SELECT * FROM users_ac WHERE email=%s AND password=%s;'''
            self.cursor.execute(sql, (email, password))
            return bool(self.cursor.fetchone())
        except mysql.connector.Error as error:
            print("Failed to execute query: {}".format(error))

    def register(self, name, email, password):
        try:
            sql = '''INSERT INTO users_ac(id, name, email, password) VALUES (?, ?, ?, ?) RETURNING *'''
            self.cursor.execute(sql, (name, email, password))
            return self.connection.commit()
        except mysql.connector.Error as error:
            print("Failed to execute query: {}".format(error))

    def pop(self, name):
        try:
            sql = '''INSERT INTO users_ac(id) VALUES (?)'''
            self.cursor.execute(sql, (name,))
            return self.connection.commit()
        except mysql.connector.Error as error:
            print("Failed to execute query: {}".format(error))
