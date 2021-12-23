from flask import Flask, render_template
from settings import User, HOST, PORT

app = Flask(__name__)
app.template_folder = 'static'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add/<name>', methods=['GET'])
def add(name):
    user, status = User.get_or_create(name=name)
    if status:
        return render_template('added.html', name=name)
    user.count += 1
    user.save()
    return render_template('already.html', name=name, count=user.count)


@app.route('/show', methods=['GET'])
def show():
    users = User.select()
    users_list = []
    for u in users:
        users_list.append(f'{u.name} : {u.count}')
    return render_template('show.html', show=' ; '.join(users_list))


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
