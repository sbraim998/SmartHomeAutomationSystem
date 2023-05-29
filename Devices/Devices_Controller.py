from flask import render_template

from Devices.Devices_Model import Device

def control_devices(device_name):
    if device_name == 'RGBLight':
        # Display the control page for the RGB light
        return render_template('control_rgb.html', device=device_name)


def get_paired_devices():
    devices = listen_for_devices()
    return devices


def listen_for_devices():
    import socket
    wifi_name = 'FLOOR2'
    wifi_password = 'Kk123456'
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Enable broadcasting mode
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Bind the socket to a specific IP and port
    udp_socket.bind(('0.0.0.0', 12345))
    available_devices_names = []
    while True:
        # Receive data from the socket
        if len(available_devices_names) == 1:
            return available_devices_names
        data, address = udp_socket.recvfrom(1024)

        # Decode the received data
        message = data.decode('utf-8')

        # Check if the message contains the device name
        if message.startswith('device_name:'):
            device_name = message.split(':')[1]
            if device_name not in available_devices_names:
                print(device_name, 111)
                d = Device(f"{device_name}", wifi_name, wifi_password)
                print(d.device_name)
                available_devices_names.append(d)
            print(f"Detected device: {device_name}")



