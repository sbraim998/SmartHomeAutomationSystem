from model import User, db
import base64
from PIL import Image
from io import BytesIO


def get_user_face_image(user_id):
    user = User.query.get(user_id)
    if user is not None and user.face:
        # Decode the Base64-encoded image data
        image_data = base64.b64decode(user.face)
        # Create an in-memory file object
        image_file = BytesIO(image_data)
        # Open the image file using PIL
        image = Image.open(image_file)
        return image
    else:
        return None


def db_add_user(username, password, face):
    new_user = User(username=username, password=password, face=face)
    db.session.add(new_user)
    db.session.commit()


def db_delete_user(user_id):
    user = User.query.get(user_id)
    user.session.delete(user)
    user.session.commit()


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
    user.session.commit()


def db_get_user_by_id(user_id):
    return User.query.get(user_id)


def db_get_user_by_username(username):
    return User.query.filter_by(username=username).first()

