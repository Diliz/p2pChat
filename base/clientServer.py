import threading
import socket

import config
import base.text
import base.net
import base.handler

class Server(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.running = 1

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', self.port))

        if len(config.sendArr) == 0:
            base.text.echoScreen("Socket is good, waiting for connections on port: " + str(self.port), "System")
        s.listen(1)

        while self.running:
            connection, addr = s.accept()
            if check(connection, config.sendArr):
                config.sendArr.append(connection)
            else:
                connection.close()
                continue

            base.text.echoScreen("Connected by " + str(addr[0]), "System")
            connection.send(str(len(config.username)).encode(encoding='UTF-8'))
            connection.send(config.username.encode(encoding='UTF-8'))
            data = connection.recv(4)
            data = connection.recv(int(data.decode(encoding='UTF-8')))
            if data.decode(encoding='UTF-8') != "Me":
                config.usernames[connection] = data.decode(encoding='UTF-8')
            else:
                config.usernames[connection] = addr[0]
            base.handler.sendFriends(connection)
            if addr[0] not in config.ips:
                config.ips.append(addr[0])
                Client(addr[0], config.port).start()
            else:
                continue

class Client(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.running = 1

    def run(self):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((self.host, self.port))
        if check(connection, config.getArr):
            config.getArr.append(connection)
            base.text.echoScreen("Connected to: " + self.host + " on port: " + str(self.port), "System")
            config.ips.append(self.host)

            connection.send(str(len(config.username)).encode(encoding='UTF-8'))
            connection.send(config.username.encode(encoding='UTF-8'))

            data = connection.recv(4)
            data = connection.recv(int(data.decode(encoding='UTF-8')))
            if data.decode(encoding='UTF-8') != "Me":
                config.usernames[connection] = data.decode(encoding='UTF-8')
            else:
                config.usernames[connection] = self.host
            threading.Thread(target=runner, args=(connection,)).start()
        else:
            connection.close()

def runner(connection):
    while 1:
        data = base.net.getData(connection)
        if data != 1:
            base.text.echoScreen(data, config.usernames[connection])

def check(connection, array):
    for i in array:
        if connection.getpeername()[0] == i.getpeername()[0]:
            return False
    return True
