import socket
import time

client3_ip = "92.10.10.25"
client3_mac = "AF:04:67:EF:19:DA"
router = ("localhost", 8200)
client3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(1)
client3.connect(router)
print('Waiting For The Messages From Server.........')
while True:
    received_message = client3.recv(1024)
    received_message = received_message.decode("utf-8")
    source_mac = received_message[0:17]
    destination_mac = received_message[17:34]
    source_ip = received_message[34:45]
    destination_ip = received_message[45:56]
    message = received_message[56:]
    print("\nMessage: " + message)