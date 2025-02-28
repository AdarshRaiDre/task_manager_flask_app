from flask import render_template, flash, make_response, jsonify, session
from flask.views import MethodView
from flask.blueprints import Blueprint
from datetime import datetime, timedelta
import jwt.utils
import jwt
from .config import SECRET_KEY
from flask import request
from .forms import LoginForm
from .models import User

login_manager_bp = Blueprint("login_manager",__name__)


class LoginView(MethodView):
    def get(self):
        form = LoginForm()
        return render_template("login.html", form=form)

    def post(self):
        username = None
        password = None
        token = None
        form = LoginForm()

        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
        else:
            request_data = request.json
            username = request_data.get('username')
            password = request_data.get('password')
    
        if not username or not password:
            return make_response(
                "Could not verify. Please provide username and password", 401
            )

        if "username" in session:
            flash("You are alrady logged in!")
            return make_response("You are already logged in!", 200)

        user = User.query.filter_by(username=username).first_or_404(description="User not found!")

        if user.username == username and user.password == password:
            token = jwt.encode(
                payload={
                    "username": username,
                    "password": password,
                    'exp': datetime.now()+timedelta(minutes=30)
                },
                algorithm="HS256",
                key=SECRET_KEY,
            )

            if token is not None:
                return make_response({"token": token})
            else:
                return make_response("Invalid username or paSSWORD", 401)


login_manager_bp.add_url_rule("/login", view_func=LoginView.as_view("login"))
