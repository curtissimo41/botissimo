from bs4 import BeautifulSoup
from commandsQuote import addquote, editquote, quote, remquote
from Initialize import join_room
from readInput import get_user, get_message, get_badges
from Settings import CHANNEL, BANNEDTERMS
from Socket import open_socket, send_message

import helpers
import json
import requests
import os


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
	fileDir = os.path.dirname(os.path.realpath(__file__)) + '/'

	with open(fileDir + 'commandsBasic.txt', encoding = 'utf-8') as basicCommandFile:
		basicCommandJSON = json.load(basicCommandFile)


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


	def comm_bttv(self, s):
		send_message(s, 'BetterTTV emotes for this channel: ' + self.bttvEmotes)


	def comm_ffz(self, s):
		send_message(s, 'FFZ emotes for this channel: ' + self.ffzEmotes)


	def comm_followage(self, s):
		url = 'https://decapi.me/twitch/followage/' + CHANNEL + '/' + self.user + '?precision=7'
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()

		if soup == 'A user cannot follow themself.':
			send_message(s, 'You can\'t follow yourself, idiot FeelsWeirdMan')
		elif soup == 'Follow not found':
			send_message(s, 'Not following? I see how it is FeelsWeirdMan')
		else:
			send_message(s, self.user + ' has been following ' + CHANNEL + ' for ' + soup + '.')


	def comm_sudoku(self, s):
		reply = '/timeout ' + self.user + ' 5'
		send_message(s, reply)
		send_message(s, '/me FeelsBadMan 🗡️ An honorable way to go.')


	def comm_uptime(self, s):
		url = 'https://decapi.me/twitch/uptime?channel=' + CHANNEL
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()

		if soup == (CHANNEL + ' is offline'):
			send_message(s, CHANNEL.capitalize() + ' is offline.')
		else:
			send_message(s, CHANNEL.capitalize() + ' has been live for ' + soup)


	# --------------------------------------------------------------------------
	# ------------------------------Main Function-------------------------------
	# --------------------------------------------------------------------------
	def run(self, s, readbuffer):
		while True:
			print('\n===Start of new wait period.===\n')
			readbuffer = s.recv(1024).decode('utf-8')
			if not readbuffer:
				s = open_socket()
				continue
			temp = readbuffer.split('\n')
			readbuffer = temp.pop()

			line = temp[0]
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

				if 'yo gl' in line:
					send_message(s, 'yo thanks FeelsOkayMan 👍')

				for i in range(0, len(self.msg)):
					if self.msg[i] in BANNEDTERMS:
						self.bannedTermTimeout(s)
						break
					elif i is 0:
						if self.msg[i] in self.cmdListBasic:
							send_message(s, self.basicCommandJSON[self.msg[i]]['return'])

						elif self.msg[i] in self.commandsBot:
							self.commandsBot[self.msg[i]](self, s)

						elif self.msg[i] in self.commandsQuote:
							if self.msg[i] is not '!quote' and self.isMod():
								isQuoteCmd = True
							elif self.msg[i] == '!quote':
								isQuoteCmd = True
					else:
						if isQuoteCmd:
							arglist.append(self.msg[i])

				if isQuoteCmd:
					qmsg = self.commandsQuote[self.msg[0]](arglist)
					send_message(s, qmsg)


	commandsBot = {
		'!bttv': comm_bttv,
		'!ffz': comm_ffz,
		'!followage': comm_followage,
		'!sudoku': comm_sudoku,
		'!uptime': comm_uptime
	}

	commandsQuote = {
		'!addquote': addquote,
		'!editquote': editquote,
		'!quote': quote,
		'!remquote': remquote
	}


if __name__ == '__main__':
	bot = Botissimo()
