import mysql.connector
import setting
class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(database=setting.DATABASE['basename'],
                                           user=setting.DATABASE['login'],
                                           host=setting.DATABASE['ip'],
                                           password=setting.DATABASE['password'])
        self.cursor = self.connection.cursor()

    def login(self, email, password):
        try:
            sql = '''SELECT * FROM users_ac WHERE email=%s AND password=%s;'''
            self.cursor.execute(sql, (email, password))
            print(self.cursor.fetchone())
            return self.cursor.fetchone()
        except mysql.connector.Error as error:
            print("Failed to execute query: {}".format(error))

    def register(self, name, email, password):
        try:
            sql = '''INSERT INTO users_ac(id, name, email, password) VALUES (?, ?, ?, ?) RETURNING *'''
            result = self.cursor.execute(sql, (name, email, password))
            self.connection.commit()
            print(result)
            print(self.connection.commit())
            return result
        except mysql.connector.Error as error:
            print("Failed to execute query: {}".format(error))

    def pop(self, name):
        try:
            sql = '''INSERT INTO users_ac(id) VALUES (?)'''
            result = self.cursor.execute(sql, (name,))
            self.connection.commit()
            print(result)
            print(self.connection.commit())
            return result
        except mysql.connector.Error as error:
            print("Failed to execute query: {}".format(error))
