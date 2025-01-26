from flask import (
    Flask,
    render_template,
    redirect,
    request,
    flash,
    url_for,
    get_flashed_messages,
)
from my_first_website.repository import get_db, UsersRepository
from my_first_website.validator import validate_user
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
def users():
    users = repo.get_entities()
    messages = get_flashed_messages(with_categories=True)

    return render_template(
        'users/index.html',
        users=users,
        messages=messages,
        )


@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.form.to_dict()

    errors = validate_user(user_data)

    if not errors:
        user = user_data
        repo.save(user)
        flash('User has been created', 'success')
        return redirect(url_for('users'))

    return render_template(
        'users/new.html',
        user=user_data,
        errors=errors
        ), 422


@app.route('/users/new')
def users_new():
    user = {'name': '',
            'email': '',
            'password': ''
            }

    return render_template(
        'users/new.html',
        user=user,
        errors={}
    )
