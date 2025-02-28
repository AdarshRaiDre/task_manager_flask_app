from .models import db, User, Task

def init_app(app):
    db.init_app(app=app)
    return db