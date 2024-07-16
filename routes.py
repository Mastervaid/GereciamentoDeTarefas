from flask import Blueprint, jsonify, request
from models.task import Task

#create blueprint routes
tasks_bp = Blueprint('tasks', __name__)

#create new task
@tasks_bp.route("/task", methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(
        title=data['title'],
        description=data.get('description'),
        date=data.get('date'),
        status=data.get('status')
    )

    from main import db
    db.session.add(new_task)
    db.session.commit()
    return jsonify(
        {
            "mensage": "created task sucessful!",
            "title": new_task.title, 
            "description": new_task.description, 
            "date": new_task.date, 
            "status": new_task.status 
        }), 200


#return all tasks
@tasks_bp.route("/tasks", methods=['GET'])
def return_tasks():
    tasks = Task.query.all()
    return jsonify([{"title": task.title, "description": task.description, "date": task.date, "status": task.status} for task in tasks]) 



#delete task
@tasks_bp.route("/task/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        from main import db
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task delete with sucessfull!"})
    else:
        return jsonify({"message": "Not found task!"})

