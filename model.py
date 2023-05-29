import base64

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


basedir = 'reporting_systems'

app = Flask(__name__)
app.secret_key = 'IM_THE_BEST'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + '../database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(50), unique=True, nullable=False)
    wifi_name = db.Column(db.String(50), nullable=False)
    wifi_password = db.Column(db.String(50), nullable=False)

    def __init__(self, device_name, wifi_name, wifi_password):
        self.device_name = device_name
        self.wifi_password = wifi_password
        self.wifi_name = wifi_name


class DeviceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Device
        include_relationships = True
        load_instance = True


device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    face = db.Column(db.LargeBinary)

    def __init__(self, username, password, face):
        self.username = username
        self.password = password
        self.face = face

    def save(self):
        db.session.add(self)
        db.session.commit()


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)