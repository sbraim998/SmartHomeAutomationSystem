from flask import request, redirect, render_template

from model import Room, Device


def add_room():
    if request.method == 'POST':
        room_name = request.form['room_name']
        new_room = Room(room_name=room_name)
        new_room.save()
        return redirect('/rooms')
    return render_template('add_room.html')


def get_available_rooms():
    return Room.query.all()


def get_devices_in_room(room_id):
    room = Room.query.get(room_id)  # Retrieve the room object by room_id

    if room:
        return room.devices  # Return the devices associated with the room

    return []  # Return an empty list if the room is not found


def check_device_exists_in_room(room_id, device_name):
    room = Room.query.get(room_id)  # Retrieve the room object by room_id
    if room:
        devices = room.devices
        for device in devices:
            device_obj = Device.query.get(device.id)  # Retrieve the device object by device ID
            if device_obj.device_name == device_name:
                return True  # Device exists in the room
    return False  # Device does not exist in the room or room does not exist
