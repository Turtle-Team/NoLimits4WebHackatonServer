import psycopg2
import setting
class DataBase:
    def __init__(self):
        self.connection = psycopg2.connect(database=setting.DATABASE['basename'],
                                           user=setting.DATABASE['login'],
                                           password=setting.DATABASE['password'],
                                           port=5432)
        self.cursor = self.connection.cursor()
    def login(self, email, password):
        sql = '''SELECT * FROM users_ac WHERE email=%s AND password=%s;'''
        self.cursor.execute(sql, (email, password))
        return bool(self.cursor.fetchone())


    def register(self, name, email, password):
        sql = '''INSERT INTO users_ac(id, name, email, password) VALUES (?, ?, ?, ?) RETURNING *'''
        self.cursor.execute(sql, (name, email, password))
        return self.connection.commit()

