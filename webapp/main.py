
from flask import Flask, Blueprint, render_template
import logging
import sys
import os
import secrets


home = Blueprint('home', __name__, url_prefix="/")
test = Blueprint('test', __name__, url_prefix="/test")


@home.route("/", methods=['GET'])
def index():
    return render_template("home.html")


@test.route("/", methods=['GET'])
def index():
    return render_template("test.html")


def create_app():

    app = Flask(__name__)
    #app.config['SERVER_NAME'] = os.getenv('SERVER_NAME', '192.168.178.20:8080')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_hex())

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(test, url_prefix='/test')
    
    return app


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger()
app = create_app()


if __name__ == "__main__": 
    log.info(f"Starting test webapp...")
    #from waitress import serve
    #serve(app, host='0.0.0.0')
    app.run(host='0.0.0.0', debug=True)