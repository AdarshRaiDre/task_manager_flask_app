from flask import render_template, make_response, jsonify
from flask.views import MethodView
from flask.blueprints import Blueprint
from .auth import token_required
from flask import request
from task_manager import Task, db

task_manager_bp = Blueprint("task_manager", __name__, url_prefix='/')


class TasksView(MethodView):
    @token_required
    def get(self, current_user):
        tasks = Task.query.filter_by(username=current_user).all()
        if tasks is None:
            return make_response(jsonify({"Message": "No tasks found!"}), 400)
        return render_template("tasks_list.html", tasks=tasks)

    @token_required
    def post(self, current_user):
        request_payload = request.json
        title = request_payload.get("task_title")
        description = request_payload.get("task_description")
        priority = request_payload.get("task_priority")
        status = request_payload.get("task_status")
        task_id = request_payload.get("task_id")

        if not title or not description or not priority or not status:
            return make_response({"Message": "Missing required fields"}, 400)

        task = Task(
            title=title,
            description=description,
            username=current_user,
            priority=priority,
            status=status,
            task_id=task_id
        )
        db.session.add(task)
        db.session.commit()

        return make_response(jsonify({"Message": "Task created succcessfully!"}), 200)

    @token_required
    def patch(self, current_user):
        request_payload = request.json
        task_id = request_payload.get("task_id")
        task_title = request_payload.get("task_title")
        task_description = request_payload.get("task_description")
        task_priority = request_payload.get("task_priority")
        task_status = request_payload.get("task_status")
        username = current_user

        if not task_id or not task_description or not task_priority or not task_status:
            return make_response(jsonify({"message": "Missig required fields"}), 400)

        Task.query.filter_by(id=task_id).update(
            {
                "title": task_title,
                "description": task_description,
                "priority": task_priority,
                "status": task_status,
                "username": username,
            }
        )
        db.session.commit()
        return make_response(jsonify({"message": "Task updated successfully"}), 200)

    @token_required
    def delete(self, current_user):
        request_payload = request.json
        task_id = request_payload.get("task_id")
        if not task_id:
            return make_response(jsonify({"message": "Missing required fields"}), 200)
        task = Task.query.filter_by(id=task_id, username=current_user).first()
        db.session.delete(task)
        db.session.commit()
        return make_response(jsonify({"message": "Task deleted successfully!"}), 200)


task_manager_bp.add_url_rule("tasks", view_func=TasksView.as_view("tasks"))
