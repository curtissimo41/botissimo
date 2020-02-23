from Socket import send_message

import time


moduleStartTime = int(time.time())
cmdsOnCooldown = {}

def runTBM(s):
    while True:
        try:
            for cmd in cmdsOnCooldown:
                if int(time.time()) > cmdsOnCooldown[cmd]:
                    cmdsOnCooldown.pop(cmd, None)
        except:
            pass
        if (int(time.time()) - moduleStartTime) % 1800 == 0:
            send_message(s, "If you're enjoying the stream, consider hitting the follow button to see when I go live "
                            "in the future! Kappu")
        time.sleep(1)
