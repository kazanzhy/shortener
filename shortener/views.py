
from flask import request, render_template, redirect, url_for, abort
from . import app, session
from .models import *
from .forms import *
from .additions import get_code, generate_code
from .config import HOST

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = MainForm(request.form)
    if request.method == 'POST' and form.validate():
        link = form.link.data
        code = get_code(session, link)
        return render_template('home.html', form = form, code = code, host = HOST)
    return render_template('home.html', form = form)


@app.route('/admin')
def admin():
    abort(401)


@app.route('/<code>')
def redirection(code):
    query = session.query(Link).filter_by(code=code).first() 
    if query is not None:
        if '://' not in query.link:
            query.link = 'http://' + query.link
        return redirect(query.link)
    else:
        abort(404)


@app.errorhandler(401)
def access_denied(error):
    return render_template('401.html'), 401


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

