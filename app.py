from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world!'


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0', debug=True)
