import flask_app
import setting

if __name__ == '__main__':
    flask_app.app.run(host=settings.FLASK_IP, debug=False, port=settings.FLASK_PORT)
