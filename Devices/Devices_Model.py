from model import Device


def create_device(device_name, IP):
    device = Device(device_name=device_name, IP=IP, status=True)
    device.session.add(device)
    device.session.commit()
    return device


def delete_device(device_name):
    device = Device.query.fillter_by(device_name=device_name)
    device.session.delete()
    device.session.commit()


def check_device_exists(device_name):
    device = Device.query.filter_by(device_name=device_name).first()
    if device:
        return True  # Device exists in the database
    else:
        return False  # Device does not exist in the database
