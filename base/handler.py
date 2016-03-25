import config
import base.net
import base.clientServer
import base.text

def eventHandler(number, conn=None):
    num = int(number[1:])
    if num == 1:
        if connection is None:
            base.text.echoScreen("Disconnected.", "System")
            for i in config.sendArr:
                i.send("-001".encode())
            config.sendArr.clear()
            config.getArr.clear()
            config.ips.clear()
        else:
            base.text.echoScreen(connection.getpeername()[0] + " disconnected.", "System")
            for i in config.sendArr:
                if i.getpeername()[0] == connection.getpeername()[0]:
                    config.sendArr.remove(i)
                    break
            config.getArr.remove(connection)
            config.ips.remove(connection.getpeername()[0])
    elif num == 4:
        data = connection.recv(4)
        data = connection.recv(int(data.decode(encoding='UTF-8')))
        base.clientServer.Client(data.decode(encoding='UTF-8'), int(config.contact_array[conn.getpeername()[0]][0])).start()

def sendFriends(connection):
    for one in config.sendArr:
        if connection.getpeername()[0] != one.getpeername()[0]:
            connection.send("-004".encode(encoding='UTF-8'))
            connection.send(str(len(one.getpeername()[0])).encode(encoding='UTF-8'))
            connection.send(one.getpeername()[0].encode(encoding='UTF-8'))
