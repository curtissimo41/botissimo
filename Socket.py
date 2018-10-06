import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL


def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(bytes('PASS ' + PASS + '\r\n', 'utf-8'))
    s.send(bytes('NICK ' + IDENT + '\r\n', 'utf-8'))
    s.send(bytes('JOIN #' + CHANNEL + '\r\n', 'utf-8'))
    return s


def sendMessage(s, message):
    messageTemp = bytes(('PRIVMSG #' + CHANNEL + ' :' + message), 'utf-8')
    s.send(messageTemp + b'\r\n')
    print('Sent: ' + messageTemp.decode('utf-8'))
