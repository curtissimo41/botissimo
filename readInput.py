def get_badges(line):
    """
    Gathers a list of all of the badges that a user has in the channel.
    Input: line (str) - current buffer line
    Returns: badges (list) - user's badges in the current chatroom
    """
    badgeInfo = line.split(':', 2)[0].split(';')[1].split('=')[1].split(',')
    badges = []
    for badge in badgeInfo:
        badges.append(badge.split(',')[0].split('/')[0])
    return badges


def get_user(line):
    """
    Collects the username of the user who sent the last message.
    Input: line (str) - current buffer line
	Returns: user (str) - username
    """
    separate = line.split(':', 2)
    user = separate[1].split('!', 1)[0]
    return user


def get_message(line):
    """
    Collects the last message sent to the chat.
    Input: line (str) - current buffer line
    Returns: msg (str) - most recent message
    """
    separate = line.split(':')
    for item in separate:
        print(item + '\n')
    msg = separate[2].replace('\r', ' ').split(' ')
    return msg
