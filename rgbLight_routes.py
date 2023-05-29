import requests

arduino_ip = "172.20.10.3"


def turn_on_light():
    return change_color_red()


def turn_off_light():
    url = f"http://{arduino_ip}/rgpLight/off"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        print("Failed to turn off the light")


def change_color(red, green, blue):
    url = f"http://{arduino_ip}/rgpLight/color?red={red}&green={green}&blue={blue}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        print("Failed to change the color")


def change_color_blue():
    url = f"http://{arduino_ip}/rgpLight/color?red={255}&green={0}&blue={0}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        print("Failed to change the color")


def change_color_red():
    url = f"http://{arduino_ip}/rgpLight/color?red={0}&green={0}&blue={255}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        print("Failed to change the color")


def change_color_pink():
    url = f"http://{arduino_ip}/rgpLight/color?red={255}&green={0}&blue={255}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        print("Failed to change the color")


def change_color_purple():
    url = f"http://{arduino_ip}/rgpLight/color?red={255}&green={50}&blue={150}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        print("Failed to change the color")
