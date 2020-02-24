import atexit

from flask import Flask

from controllers.message import message
from jobs import init_sms_worker, terminate_worker


def create_app():
    worker = init_sms_worker()
    atexit.register(terminate_worker, worker)
    return Flask(__name__)


app = create_app()


@app.route('/')
def home():
    return '<h1>Messaging platform</h1>'


app.register_blueprint(message, url_prefix='/message')

if __name__ == '__main__':
    app.run()
