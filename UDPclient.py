from socket import *

serverIP = "10.10.10.253"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Siapa Nama Anda: ")
message = message.encode()
clientSocket.sendto(message,(serverIP, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()


