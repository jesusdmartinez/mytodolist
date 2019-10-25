from flask import Blueprint, jsonify, request

from . import db
from .models import Mytasks

MytasksApi = Blueprint('mytask_api', __name__)


@MytasksApi.route('/create', methods=['POST'])
def create_mytasks():

    try:
        task = Mytasks.from_dict(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    db.session.add(task)
    db.session.commit()
    return jsonify(), 200


@MytasksApi.route('/<id>', methods=['GET'])
def get_mytask(id):
    task = Mytasks.query.filter(Mytasks.id == id).first()
    if task is None:
        return 'task not found', 404
    return jsonify(task.to_dict()), 200


@MytasksApi.route('/<id>', methods=['DELETE'])
def delete_mytask(id):
    task = Mytasks.query.filter(Mytasks.id == id).first()
    if task is None:
        return 'task not found', 404

    db.session.delete(task)
    db.session.commit()
    return 'Deleted', 200


@MytasksApi.route('/<id>', methods=['PUT'])
def update_mytasks(id):
    try:
        todo = Mytasks.from_dict(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400

    oldtodoitem = Mytasks.query.filter(Mytasks.id == id).first()
    oldtodoitem.task_name = todo.task_name
    oldtodoitem.due_date = todo.due_date
    db.session.commit()
    return jsonify(), 200