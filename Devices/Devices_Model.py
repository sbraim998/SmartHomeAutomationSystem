from model import Device


def create_device(device_name, wifi_name, wifi_password):
    device = Device(device_name=device_name, wifi_name=wifi_name, wifi_password=wifi_password)
    device.session.add(device)
    device.session.commit()
    return device


def delete_device(device_name):
    device = Device.query.fillter_by(device_name=device_name)
    device.session.delete()
    device.session.commit()
