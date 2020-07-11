import re

def get_badges(line):
    """
    Gathers a list of all of the badges that a user has in the channel.
    Input: line (str) - current buffer line
    Returns: badges (list) - user's badges in the current chatroom
    """
    badgeInfo = line.split('badges=')[1].split(';')[0].split(',')
    badges = []
    for badge in badgeInfo:
        badges.append(badge.split('/')[0])
    return badges


def get_user(line):
    """
    Collects the username of the user who sent the last message.
    Input: line (str) - current buffer line
	Returns: user (str) - username
    """
    user = line.split('user-type=')[1].split(':')[1].split('!')[0]
    return user


def get_message(line):
    """
    Collects the last message sent to the chat.
    Input: line (str) - current buffer line
    Returns: msg (str) - most recent message
    """
    msg = line.split('PRIVMSG', 1)[1].split(':', 1)[1].split('\r')[0].split(' ')
    return msg


def bits_parse(line):
    temp = line.split(' :')
    try:
        return int((re.findall(r';bits=(.*?);', temp[0]))[0])
    except:
        return None


def gift_sub_parse(line):
    sender = re.findall(r'display-name=(.*?);', line)[0]
    recipient = re.findall(r'msg-param-recipient-display-name=(.*?);', line)[0]
    total_gift_subs = int(re.findall(r'msg-param-sender-count=(.*?);', line)[0])
    tier = re.findall(r'msg-param-sub-plan=(.*?);', line)[0]
    return (sender, recipient, total_gift_subs, tier)


def sub_parse(line):
    subscriber = re.findall(r'display-name=(.*?);', line)[0]
    tier = re.findall(r'msg-param-sub-plan=(.*?);', line)[0]
    return (subscriber, tier)


def resub_parse(line):
    subscriber = re.findall(r'display-name=(.*?);', line)[0]
    duration = int(re.findall(r'msg-param-months=(.*?);', line)[0])
    tier = re.findall(r'msg-param-sub-plan=(.*?);', line)[0]
    return (subscriber, duration, tier)


def parse_yt_link(line):
    url = re.findall(r'http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?', line)
    try:
        return url[0][0]
    except:
        return 'Could not parse YT link FeelsBadMan'
