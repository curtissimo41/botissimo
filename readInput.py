def getUser(line):
	# Collects the username of the user who sent the last message.
	# Input: line - current buffer line
	# Returns: user - username
    separate = line.split(':', 2)
	user = separate[1].split('!', 1)[0]
	return user


def getMessage(line):
	# Collects the last message sent to the chat.
	# Input: line - current buffer line
	# Returns: msg - most recent message
	separate = line.split(':', 2)
	msg = separate[2]
	return msg
