from flask import Flask, render_template, redirect
from User.User_Model import db, db_get_user_by_username
from authentication import has_session

app = Flask(__name__)
app.config['SECRET_KEY'] = '\x8afmI\xc5\x17Rh\x11\xd96Z\xa0\xf1\xfdm\xc0\xfc/\xce\xb4\x9d\xed/'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    return redirect('login')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/add_user', methods=['GET', 'POST'])
def view_add_user():
    from User.User_Controller import controller_add_user
    return controller_add_user()


@app.route('/edit_user', methods=['GET', 'POST'])
def view_edit_user():
    from User.User_Controller import controller_edit_user
    return controller_edit_user()


@app.route('/delete_user', methods=['GET', 'POST'])
def view_delete_user():
    from User.User_Controller import controller_delete_user
    return controller_delete_user()


@app.route('/login', methods=['GET', 'POST'])
def view_authenticate_login():
    from authentication import controller_authenticate_user
    return controller_authenticate_user()


@app.route('/logout', methods=['GET', 'POST'])
def view_authenticate_logout():
    from authentication import controller_logout
    return controller_logout()


@app.route('/control_light')
def view_control_light():
    return render_template('template.html')


@app.route('/turn_on')
def tigger_turn_on_relay():
    from lights import turn_on_relay
    turn_on_relay()
    return render_template('template.html', msg="light is on")


@app.route('/turn_off')
def trigger_turn_off_relay():
    from lights import turn_off_relay
    msg = turn_off_relay()
    return render_template('template.html', msg=msg)


with app.app_context():
    db.create_all()
