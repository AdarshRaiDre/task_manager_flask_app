from flask import render_template, redirect, url_for, flash, make_response, jsonify
from flask.views import MethodView
from flask.blueprints import Blueprint
from .forms import RegistrationForm
from task_manager import db, User

registration_manager_bp = Blueprint("registration_manager",__name__)

class RegistrationView(MethodView):
    def get(self):
        form = RegistrationForm()
        return render_template('registration.html', form=form)

    def post(self):
        form = RegistrationForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.username.data
            if User.query.filter_by(username=username).first():
                return make_response("User already exits!", 200)
            db.session.add(User(username=username, password=password))
            db.session.commit()
            return make_response("Registration Successful!")
        return render_template('registration.html', form=form)

registration_manager_bp.add_url_rule('/register', view_func=RegistrationView.as_view('register'))