from flask import Flask
from flask_sqlalchemy improt SQLAlchemy

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello flask"


if __name__ == "__main__":
    app.run(host='127.0.0.1')
