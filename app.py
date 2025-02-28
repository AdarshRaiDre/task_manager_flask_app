from task_manager.LoginView import login_manager_bp
from task_manager.RegistrationView import registration_manager_bp
from task_manager.TasksView import task_manager_bp
from flask.blueprints import Blueprint
from task_manager.config import  SECRET_KEY
from flask import Flask
from task_manager import init_app

app_bp = Blueprint("app",__name__, url_prefix="/taskmanager")
app_bp.register_blueprint(task_manager_bp)
app_bp.register_blueprint(login_manager_bp)
app_bp.register_blueprint(registration_manager_bp)


app = Flask(__name__)

app.register_blueprint(app_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///taskmanager.db"
app.config['SECRET_KEY'] = SECRET_KEY

if __name__ == '__main__':
    print('Starting the app...')
    with app.app_context():
        print('Creating app context...')
        db = init_app(app)
        print("Initializing DB...")
        db.drop_all()
        db.create_all()
        print("Creating all tables...")
        print(app.url_map)
        app.run(host="0.0.0.0", debug=False, port=8004)




