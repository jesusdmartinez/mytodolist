from flask import current_app as app
from flask import render_template

from .hello import HelloApi
from .books import BookApi
from .mytasks import MytasksApi

from .models import Mytasks
from flask import Blueprint, jsonify, request

app.register_blueprint(HelloApi, url_prefix='/hello')
app.register_blueprint(BookApi, url_prefix='/books')
app.register_blueprint(MytasksApi, url_prefix='/mytasks')

# homepage
@app.route('/')
def hello():
    return render_template('hello.html')

# about me
@app.route('/about')
def about():
    return render_template('about.html')

# tasks
@app.route('/mytasks')
def mytasks():
    # posts = [{'stock': 'netflix', 'rating': 'buy'}]
    posts = Mytasks.query.all()
    # posts = jsonify(task.to_dict())
    return render_template('mytasks.html', posts=posts)

