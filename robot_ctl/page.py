import flask_login
from flask import request, make_response, render_template, url_for, Blueprint
from flask_restful import abort
from werkzeug.utils import redirect

from robot_ctl.api import ApiRequest
from robot_ctl.db_util import get_user_session, get_qq_page
from robot_ctl.logger import getLogger
from robot_ctl.login_manager import User
from backup.monitor_main import is_safe_url
from robot_ctl.model import QQ

logger = getLogger(__name__)

robot_blueprint = Blueprint('page', __name__, template_folder='templates')


@robot_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user_session(username)
        logger.debug('db user id is %s, detail is %s' % (username, user))
        if user is None:
            return abort(400)

        next_url = request.args.get("next")
        logger.debug('next is %s' % next_url)

        if password == user.password and username == user.username:
            # set login user
            user = User()
            user.id = username
            flask_login.login_user(user)

            resp = make_response(render_template('index.html', name=username))
            resp.set_cookie('username', username)
            if not is_safe_url(next_url):
                return abort(400)
            return redirect(next_url or url_for('page.robot'))
        else:
            # return redirect(url_for('error'))
            return abort(404)

    return render_template('login.html')


@robot_blueprint.route('/robot', methods=['GET'])
@robot_blueprint.route('/robot/index', methods=['GET'])
@flask_login.login_required
def robot():
    next_url = request.args.get("next")
    if not is_safe_url(next_url):
        return abort(400)
    index = 1
    size = 10
    qqs = get_qq_page(index, size)
    return render_template('robot/index.html', name=flask_login.current_user.id, qqs=qqs)


@robot_blueprint.route('/logout')
@flask_login.login_required
def logout():
    # remove the username from the session if it's there
    logger.debug("logout page")
    flask_login.logout_user()
    return redirect(url_for('page.login'))


@robot_blueprint.route('/', methods=['GET', 'POST'])
@robot_blueprint.route('/index', methods=['GET', 'POST'])
@robot_blueprint.route('/index/<int:qqpage>', methods=['GET', 'POST'])
@flask_login.login_required
def index(qqpage=1):
    s = request.args.get('size')
    print(str.format('{}:{}', qqpage, s))
    if s is None:
        s = 10
    qqs = get_qq_page(qqpage, s)
    qqlist = qqs[0]
    index = qqs[1]
    pages = qqs[2]
    # return render_template('home.html', qqlist=qqlist, pages=pages, page_num=index, size=s)
    return redirect(url_for('page.robot'))