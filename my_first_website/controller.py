from flask import (
    Flask,
    render_template,
)
from repository import get_db, UsersRepository
import os


app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

repo = UsersRepository(get_db(app))


@app.errorhandler(404)
def not_found(error):
    return 'Oops!', 404


@app.route("/")
def home():
    return render_template('users/bar.html')


@app.route('/users')
def products():
    users = repo.get_entities()
    return render_template('users/index.html', users=users)
