from flask_sqlalchemy import SQLAlchemy
import bcrypt
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    face = db.Column(db.String)
    plate_number = db.Column(db.String)
    # isAdmin = db.Column(db.String, default='False')
    status = db.Column(db.Boolean, nullable=True)

    def __init__(self, username, password, face, plate_number, status):
        self.username = username
        self.password = password
        self.face = face
        self.plate_number = plate_number
        self.status = False


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


#
# user_schema = UserSchema()
# users_schema = UserSchema(many=True)


def db_add_user(username, password, face, plate_number, status=True):
    new_user = User(username=username, password=password, face=face, plate_number=plate_number, status=status)
    db.session.add(new_user)
    db.session.commit()


def db_delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()


def db_edit_user(user_id, username=None, password=None, face=None, plate_number=None):
    user = User.query.get(user_id)
    if username:
        user.username = username
    if password:
        user.password = password
    if face:
        user.face = face
    if plate_number:
        user.plate_number = plate_number
    # if isAdmin is not None:
    # user.isAdmin = isAdmin
    db.session.commit()


def db_get_user_by_id(user_id):
    return User.query.get(user_id)


def db_get_user_by_username(username):
    return User.query.filter_by(username=username).first()
