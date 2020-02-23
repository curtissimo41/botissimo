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
