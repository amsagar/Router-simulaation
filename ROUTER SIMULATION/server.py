import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen(2)
server_ip = "92.10.10.10"
server_mac = "00:00:0A:BB:28:FC"
router_mac = "05:10:0A:CB:24:EF"
while True:
    print('Waiting For Router Connection!!!!')
    routerConnection, address = server.accept()
    if (routerConnection != None):
        print('Router Connected Succesfully....!')
        break
while True:
    ethernet_header = ""
    IP_header = ""
    message = input("\nEnter the text message to send: ")
    cli = int(input('1.Client1(92.10.10.15)\n2.Client2(92.10.10.20)\n3.Client3(92.10.10.25)\nEnter Your Choice:'))
    if cli == 1:
        destination_ip = "92.10.10.15"
    elif cli == 2:
        destination_ip = "92.10.10.20"
    elif cli == 3:
        destination_ip = "92.10.10.25"
    else:
        print('Invalid Choice For CLient!!!!')
    source_ip = server_ip
    IP_header = IP_header + source_ip + destination_ip
    source_mac = server_mac
    destination_mac = router_mac
    ethernet_header = ethernet_header + source_mac + destination_mac
    packet = ethernet_header + IP_header + message
    routerConnection.send(bytes(packet, "utf-8"))
