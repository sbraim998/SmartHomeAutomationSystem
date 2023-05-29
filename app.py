from flask import render_template, redirect, request
import Devices
import rgbLight_routes
from model import app, db


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


# Route for displaying devices
@app.route('/devices')
def show_devices():
    from Devices.Devices_Controller import get_paired_devices
    from Devices.Devices_Model import Device
    paired_devices = get_paired_devices()
    print(paired_devices)
    if paired_devices:
        return render_template('devices.html', devices=paired_devices)
    else:
        return render_template('devices.html', devices=Devices.Devices_Model.Device('No Devices available', '0', '0'))


@app.route('/hardware/<device_name>')
def hardware_controller(device_name):
    print(device_name)
    if device_name == 'RGBLight':
        return render_template('control_rgb.html', device_name=device_name, message=None)


@app.route('/control/<device_name>/turn_on')
def turn_on(device_name):
    if request.method == 'GET':
        if device_name == 'RGBLight':
            response = rgbLight_routes.turn_on_light()
            if response:
                message = 'Turned ON Successfully'
            else:
                message = 'Error occurred'
            return render_template('control_rgb.html', device_name=device_name, message=message)


@app.route('/control/<device_name>/turn_off')
def turn_off_light(device_name):
    if request.method == 'GET':
        if device_name == 'RGBLight':
            response = rgbLight_routes.turn_off_light()
            if response:
                message = 'Turned OFF Successfully'
            else:
                message = 'Error occurred'
            return render_template('control_rgb.html', device_name=device_name, message=message)


# @app.route('/pair_new_device')
# def show_devices():
#     from Devices.Devices_Controller import get_paired_devices
#     around_devices = Devices.Devices_Controller.discover_devices()
#     print(around_devices)
#     return render_template('pair_device.html', around_devices=around_devices)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
