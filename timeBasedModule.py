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
        if (int(time.time()) - moduleStartTime) % 3600 == 0 and int(time.time()) != moduleStartTime:
            send_message(s, "If you're enjoying the stream, be sure to hit the follow button to know when I'll be live "
                            "next! Feel free to join our Discord as well to hangout offline -> "
                            "https://discordapp.com/invite/T7Bhj9z FeelsOkayMan")
            time.sleep(0.5)
        time.sleep(0.5)
