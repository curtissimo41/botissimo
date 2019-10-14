# ------------------------------------------------------------------------------
# -----------------------------------Imports------------------------------------
# ------------------------------------------------------------------------------
from bs4 import BeautifulSoup
from commandsQuote import addquote, editquote, quote, remquote
from Initialize import join_room
from readInput import get_user, get_message, get_badges
from Settings import CHANNEL, BANNEDTERMS
from Socket import open_socket, send_message

import helpers
import json
import requests


# ------------------------------------------------------------------------------
# ----------------------------------Bot Class-----------------------------------
# ------------------------------------------------------------------------------
class Botissimo:
	# updated on per-message basis
	user = ''
	msg = ''
	badges = []

	# obtained at the very beginning
	bttvEmotes = helpers.get_bttv_emotes()
	ffzEmotes = helpers.get_ffz_emotes()

	# compile list of all channel commands
	basicCommandJSON = {}
	cmdListBasic = []
	cmdListAdv = ['!bttv', '!commands', '!ffz', '!followage', '!sudoku', '!test',
                  '!uptime']
	cmdListQuote = ['!addquote', '!editquote', '!quote', '!remquote']

	with open('commandsBasic.txt') as basicCommandFile:
		basicCommandJSON = json.load(basicCommandFile)

	for command in basicCommandJSON:
		cmdListBasic.append(command)

	cmdListAll = cmdListAdv + cmdListBasic + cmdListQuote


	def __init__(self):
		s = open_socket()
		join_room(s)
		readbuffer = ''
		send_message(s, 'We in there boiii (Botissimo, v. 1.0)')
		self.run(s, readbuffer)


	# --------------------------------------------------------------------------
	# ------------------------------Bot Functions-------------------------------
	# --------------------------------------------------------------------------
	def bannedTermTimeout(self, s):
		timeoutMsg = '/timeout ' + self.user + ' 600'
		send_message(s, timeoutMsg)
		send_message(s, 'JKanStyle JKanStyle JKanStyle JKanStyle')


	def isMod(self):
		if 'broadcaster' in self.badges or 'moderator' in self.badges:
			return True
		else:
			return False


	# --------------------------------------------------------------------------
	# ----------------------------Advanced Functions----------------------------
	# --------------------------------------------------------------------------
	def comm_bttv(self, s):
		send_message(s, 'BetterTTV emotes for this channel: ' + self.bttvEmotes)


	def comm_chatters(self, s):
		url = 'http://tmi.twitch.tv/group/user/' + CHANNEL + '/chatters'
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").prettify()
		soup_dict = json.loads(soup)

		mods = []
		for mod in soup_dict["chatters"]["moderators"]:
			mods.append(mod)

		reply = 'Moderators for this channel are: '
		for mod in mods:
			reply += mod + ', '

		send_message(s, reply)


	def comm_commands(self, s):
		send_message(s, 'Command coming soon!!')
		"""
		reply = 'Commands for this channel: '
		for cmd in self.cmdListAll:
			reply += cmd + ', '
		send_message(s, reply)
		"""


	def comm_ffz(self, s):
		send_message(s, 'FFZ emotes for this channel: ' + self.ffzEmotes)


	def comm_followage(self, s):
		url = 'https://decapi.me/twitch/followage/' + CHANNEL + '/' + self.user + '?precision=7'
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()

		if soup == 'A user cannot follow themself.':
			send_message(s, 'You can\'t follow yourself, idiot FeelsWeirdMan')
		else:
			send_message(s, self.user + ' has been following ' + CHANNEL + ' for ' + soup + '.')


	def comm_sudoku(self, s):
		reply = '/timeout ' + self.user + ' 5'
		send_message(s, reply)
		send_message(s, '/me FeelsBadMan 🗡️ An honorable way to go.')


	def comm_test(self, s):
		# fucky command, just for testing new stuff
		pass


	def comm_uptime(self, s):
		url = 'https://decapi.me/twitch/uptime?channel=' + CHANNEL
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()

		if soup == (CHANNEL + ' is offline'):
			send_message(s, CHANNEL.capitalize() + ' is offline.')
		else:
			send_message(s, CHANNEL.capitalize() + ' has been live for ' + soup)


	# --------------------------------------------------------------------------
	# -------------------------------Run Function-------------------------------
	# --------------------------------------------------------------------------
	def run(self, s, readbuffer):
		while True:
			print('\n===Start of new wait period.===\n')
			readbuffer = ''
			readbuffer = readbuffer + s.recv(1024).decode('utf-8')
			if not readbuffer:
				s = open_socket()
				continue
			temp = readbuffer.split('\n')
			readbuffer = temp.pop()

			for line in temp:
				if line.split(' ')[0] == 'PING':
					s.send(bytes(line.replace('PING', 'PONG'), 'utf-8'))
					send_message(s, 'Refreshed bot.')
					continue
				else:
					try:
						self.user = get_user(line)
						self.msg = get_message(line)
						self.badges = get_badges(line)
					except:
						break

					isQuoteCmd = False
					arglist = []
					for i in range(0, len(self.msg)):
						if self.msg[i] in BANNEDTERMS:
							self.bannedTermTimeout(s)
							break
						elif i is 0:
							if self.msg[i] in self.cmdListBasic:
								send_message(s, self.basicCommandJSON[self.msg[i]]['return'])

							elif self.msg[i] in self.commandsAdv:
								self.commandsAdv[self.msg[i]](self, s)

							elif self.msg[i] in self.commandsQuote:
								if (self.msg[i] == '!addquote' or
								    self.msg[i] == '!remquote' or
								    self.msg[i] == '!editquote') and self.isMod():
									isQuoteCmd = True
								elif self.msg[i] == '!quote':
									isQuoteCmd = True
						else:
							if isQuoteCmd:
								arglist.append(self.msg[i])

					if isQuoteCmd:
						qmsg = self.commandsQuote[self.msg[0]](arglist)
						send_message(s, qmsg)


	commandsAdv = {
		'!bttv': comm_bttv,
		'!chatters': comm_chatters,
		'!commands': comm_commands,
		'!ffz': comm_ffz,
		'!followage': comm_followage,
		'!sudoku': comm_sudoku,
		'!test': comm_test,
		'!uptime': comm_uptime
	}

	commandsQuote = {
		'!addquote': addquote,
		'!editquote': editquote,
		'!quote': quote,
		'!remquote': remquote
	}


# ------------------------------------------------------------------------------
# ------------------------------------main--------------------------------------
# ------------------------------------------------------------------------------
if __name__ == '__main__':
	bot = Botissimo()
