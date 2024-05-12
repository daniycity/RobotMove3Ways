from sinric import SinricPro, SinricProConstants
import requests
import asyncio
import base64
import socket


APP_KEY=""
APP_SECRET=""
DEVICE_ID=""

def power_state(device_id, state):
    print(device_id, state)
    return True, state


def mode_value(device_id, mode_value, instance_id):
    if mode_value == "forward":
        import bluetooth

        # specify the MAC address of the device you want to connect to
        target_device = "98:d3:71:fd:45:d1"

        # establish a connection with the device
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((target_device, 1))

            # send a message over the Bluetooth socket
            sock.send("Forward")

            # close the Bluetooth socket
            sock.close()
        except bluetooth.btcommon.BluetoothError as e:
            print("Error:", e)
    print(device_id, mode_value, instance_id)
    return True, mode_value, instance_id


callbacks = {
    SinricProConstants.SET_POWER_STATE: power_state,
    SinricProConstants.SET_MODE: mode_value
}

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = SinricPro(APP_KEY, [DEVICE_ID], callbacks,
                       enable_log=True, restore_states=False, secret_key=APP_SECRET)
    loop.run_until_complete(client.connect())