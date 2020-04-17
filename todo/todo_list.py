from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from todo import db
from todo.models import Todo

bp = Blueprint('todo', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Todo name is required.')
        else:
            db.session.add(Todo(name=name))
            db.session.commit()

    todos = Todo.query.all()
    return render_template('todo/index.html', todos=todos)


@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    todo = Todo.query.get(id)
    if todo is not None:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('todo.index'))
