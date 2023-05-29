from flask import request, render_template

from authentication import has_session


def controller_add_user():
    msg = ''
    if has_session():
        if request.method == 'POST':
            if request.form.get('username') or request.form.get('password') is None:
                # Return an error if any required fields are missing
                msg = 'Missing required fields', 400
            else:
                username = request.form.get('username')
                password = request.form.get('password')
                face_path = request.files['face']
                if face_path.filename == '':
                    msg = 'No face file selected'
                    return render_template('add_user.html', msg=msg), 400

                from User.User_Model import db_add_user
                db_add_user(username, password, face_path)
                msg = 'Account added successfully'
        return render_template('add_user.html', msg=msg)
    else:
        return 'Please sign in first go to "172.0.0.1:5000/login"'


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


