from ppadb.client import Client as AdbClient
import time
import os
# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
time.sleep(1)
phone=["8871991181"]
for  i in phone:
    client.devices()[0].shell(f'am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone=+918871991181"')
    time.sleep(1)
    client.devices()[0].shell('input text "Hello"')
    client.devices()[0].shell('input keyevent 22')
    client.devices()[0].shell('input keyevent 22')
    client.devices()[0].shell('input keyevent 22')
    client.devices()[0].shell('input keyevent 22')
    client.devices()[0].shell('input keyevent 66')
    time.sleep(1)
