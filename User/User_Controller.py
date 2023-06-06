from flask import request, render_template
from authentication import has_session
from User.User_Model import db_add_user

UPLOAD_FOLDER = 'images'

import os
import uuid


def get_full_file_path(filename):
    return os.path.abspath(os.path.join("images", filename))


def controller_add_user():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        image_file = request.files['image']

        # Check if an image file was uploaded
        if image_file.filename == '':
            msg = 'No image file selected'
        else:
            # Generate a unique filename for the image
            filename = str(uuid.uuid4()) + os.path.splitext(image_file.filename)[1]

            # Save the image file to the "images" directory
            image_path = get_full_file_path(filename)
            image_file.save(image_path)

            # Read the image file as binary data
            with open(image_path, 'rb') as f:
                face_image = f.read()

            # Add user to the database with the image
            db_add_user(username=username, password=password, face=face_image)

            msg = 'Account added successfully'

    return render_template('add_user.html', msg=msg)


def controller_edit_user():
    msg = ''
    if has_session():
        if request.method == 'POST':
            user_id = request.form.get('user_id')
            username = request.form.get('username')
            password = request.form.get('password')
            face = request.form.get('face')
            from User.User_Model import db_edit_user
            db_edit_user(user_id, username, password, face)
            msg = 'User information edited successfully'
        return render_template('edit_user.html', msg=msg)
    else:
        return 'Please sign in first go to "172.0.0.1:5000/login"'


def controller_delete_user():
    msg = ''
    if has_session():
        if request.method == 'POST':
            user_id = request.form.get('user_id')
            from User.User_Model import db_get_user_by_id
            user = db_get_user_by_id(user_id)
            if user:
                from User.User_Model import db_delete_user
                db_delete_user(user_id)
                msg = 'User deleted successfully'
            else:
                msg = 'User ID is incorrect'
        return render_template('delete_user.html', msg=msg)
    else:
        return 'Please sign in first go to "172.0.0.1:5000/login"'
