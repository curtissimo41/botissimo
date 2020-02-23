import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL


def open_socket():
    """
    Function to open the connection for the bot to the specified channel.
    Return: s - socket connection
    """
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(bytes('PASS ' + PASS + '\r\n', 'utf-8'))
    s.send(bytes('NICK ' + IDENT + '\r\n', 'utf-8'))

    s.send(bytes('CAP REQ :twitch.tv/tags\r\n', 'utf-8'))

    s.send(bytes('JOIN #' + CHANNEL + '\r\n', 'utf-8'))
    return s


def send_message(s, message):
    """
    Sends a provided message to the chat through the socket connection
    Returns: None
    """
    messageTemp = bytes(('PRIVMSG #' + CHANNEL + ' :' + message), 'utf-8')
    s.send(messageTemp + b'\r\n')
