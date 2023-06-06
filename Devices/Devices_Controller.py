from flask import render_template
import socket
import threading
from Devices.Devices_Model import Device


def get_available_devices():
    devices = listen_for_devices()
    return devices


# def listen_for_devices():
#     wifi_name = 'FLOOR2'
#     wifi_password = 'Kk123456'
#     # Create a UDP socket
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     # Enable broadcasting mode
#     udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#
#     # Bind the socket to a specific IP and port
#     udp_socket.bind(('0.0.0.0', 12345))
#     available_devices_names = []
#
#     # Define a timeout function
#     def timeout_handler():
#         return []
#
#     # Start a timer thread for the timeout
#     timer = threading.Timer(10, timeout_handler)
#
#     timer.start()
#     try:
#         while True:
#             if len(available_devices_names) == 1:
#                 return available_devices_names
#             # Receive data from the socket with a timeout
#             udp_socket.settimeout(5)  # Set a timeout of 5 seconds
#             try:
#                 data, address = udp_socket.recvfrom(1024)
#             except socket.timeout:
#                 # Timeout occurred, check if the timer is still running
#                 if timer.is_alive():
#                     continue
#                 else:
#                     break
#
#             # Decode the received data
#             message = data.decode('utf-8')
#
#             # Check if the message contains the device name
#             if message.startswith('device_name:'):
#                 device_name = message.split(':')[1]
#                 if device_name not in available_devices_names:
#                     print(device_name, 111)
#                     d = Device(f"{device_name}", wifi_name, wifi_password, status=False)
#                     print(d.device_name)
#                     available_devices_names.append(d)
#                 print(f"Detected device: {device_name}")
#     except:
#         pass
#     return available_devices_names


def listen_for_devices():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_socket.bind(('0.0.0.0', 12345))
    available_devices = []

    def timeout_handler():
        return []

    timer = threading.Timer(10, timeout_handler)
    timer.start()

    try:
        while True:
            if len(available_devices) >= 1:  # Modify the condition to check for 2 devices
                return available_devices
            udp_socket.settimeout(5)

            try:
                data, address = udp_socket.recvfrom(1024)
            except socket.timeout:
                if timer.is_alive():
                    continue
                else:
                    break

            message = data.decode('utf-8')

            if message.startswith('device_name:'):
                device_name = message.split(':')[1].strip()
                if device_name not in [device[0] for device in available_devices]:
                    ip_address = address[0]
                    print(111, device_name)
                    print(222, ip_address)
                    d = Device(device_name=device_name, IP=ip_address, status=False)
                    available_devices.append(d)
                    print(f"Detected device: {device_name} at IP: {ip_address}")
    except:
        pass

    return available_devices
