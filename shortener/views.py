
from flask import request, render_template, redirect, url_for, abort
from . import app, session
from .models import *
from .forms import *
from .additions import get_code, generate_code
from .config import HOST


@app.route('/admin')
def admin():
    abort(401)


@app.route('/signup')
def signup():
    # 
    return redirect(url_for('home'))


@app.route('/login')
def login():
    #
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    return redirect(url_for('home'))


@app.route('/<code>')
def redirection(code):
    query = session.query(Link).filter_by(code=code).first() 
    if query is not None:
        query.redirects += 1
        session.commit()
        return redirect(query.link)
    else:
        abort(404)


@app.route('/', methods = ['GET', 'POST'])
def home():
    form = MainForm(request.form)
    if '://' not in form.link.data:
        form.link.data = 'http://' + form.link.data
    if request.method == 'POST' and form.validate():
        link = form.link.data
        code = get_code(session, link)
        return render_template('home.html', form = form, code = code, host = HOST)
    return render_template('home.html', form = form)


@app.errorhandler(401)
def access_denied(error):
    return render_template('401.html'), 401


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

