from falsk_app import flask_app
import setting


if __name__ == '__main__':
    flask_app.app.run(host=setting.FLASK_IP, debug=False, port=setting.FLASK_PORT)
