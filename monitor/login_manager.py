import flask_login
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'


def init_app(app):
    login_manager.init_app(app)


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    user = User()
    user.id = username
    return user
