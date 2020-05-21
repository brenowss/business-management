from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', static_url_path='/auth/static')


@auth.route('/kerdos/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')