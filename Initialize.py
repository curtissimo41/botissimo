from Socket import send_message

def join_room(s):
    readbuffer = ''
    Loading = True

    while Loading:
        readbuffer = readbuffer + s.recv(1024).decode('utf-8')
        print(readbuffer)
        temp = readbuffer.split('\n')
        readbuffer = temp.pop()

        for line in temp:
            Loading = loadingComplete(line)

    send_message(s, 'We in there boiii (Botissimo, v. 1.0)')

def loadingComplete(line):
    if('End of /NAMES list' in line):
        return False
    else:
        return True