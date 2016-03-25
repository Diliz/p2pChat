import socket
import config
import base.text
import base.handler

def sendData(connection, message):
    connection.send(checkData(len(message)).encode(encoding='UTF-8'))
    connection.send(message.encode(encoding='UTF-8'))

def getData(connection):
    data = connection.recv(4)
    print(data)
    if data.decode(encoding='UTF-8')[0] == '-':
        base.handler.eventHandler(data.decode(encoding='UTF-8'), connection)
        return 1
    data = connection.recv(int(data.decode(encoding='UTF-8')))
    print(data)
    return data.decode(encoding='UTF-8')

def checkData(number):
    temp = str(number)
    while len(temp) < 4:
        temp = '0' + temp
    return temp
