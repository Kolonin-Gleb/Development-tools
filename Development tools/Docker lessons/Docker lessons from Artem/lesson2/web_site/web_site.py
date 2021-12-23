from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Ok'


if __name__ == '__main__':
    app.run(host='localhost', port=8081)
