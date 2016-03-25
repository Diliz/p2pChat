import socket
import config
import base.text
import base.handler

def sendData(connection, message):
    connection.send(str(len(message)).encode(encoding='UTF-8'))
    connection.send(message.encode(encoding='UTF-8'))

def getData(connection):
    data = connection.recv(4)
    if data.decode(encoding='UTF-8')[0] == '-':
        base.handler.eventHandler(data.decode(encoding='UTF-8'), connection)
        return 1
    data = connection.recv(int(data.decode(encoding='UTF-8')))
    return data.decode(encoding='UTF-8')
