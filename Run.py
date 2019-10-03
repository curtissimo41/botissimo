# ------------------------------------------------------------------------------
# -----------------------------------Imports------------------------------------
# ------------------------------------------------------------------------------
from Socket import open_socket, send_message
from Initialize import join_room
from readInput import get_user, get_message, get_badges
import requests
from Settings import CHANNEL
from bs4 import BeautifulSoup
import commandsBasic
import commandsQuote
import helpers
import json
import random


# ------------------------------------------------------------------------------
# ----------------------------------Bot Class-----------------------------------
# ------------------------------------------------------------------------------
class Botissimo:
	user = ''
	msg = ''
	badges = []
	bannedTerms = ['fggTayTay']
	bttvEmotes = helpers.get_bttv_emotes()
	ffzEmotes = helpers.get_ffz_emotes()


	def __init__(self):
		s = open_socket()
		join_room(s)
		readbuffer = ''
		self.run(s, readbuffer)


	# --------------------------------------------------------------------------
	# ------------------------------Bot Functions-------------------------------
	# --------------------------------------------------------------------------

	def comm_addquote(self, s, arglist):
		send_message(s, 'Command coming soon!!')
		"""
		print('Arg List: ' + str(arglist))
		print('Length of arglist: ' + str(len(arglist)))

		if len(arglist) < 2:
			send_message(s, 'Usage: !addquote <originator> <quote>')
			return

		else:
			originator = arglist[0]
			quote = ''
			quote_num = 0

			for i in range(1, len(arglist)):
				quote += arglist[i]
				if i != len(arglist) - 1:
					quote += ' '

			# write quote information to quotes.txt file
			# quote_to_add = quote + ' - ' + originator + ' [' + current game +
			#                ', ' + current date + ']'
			# with open('Resources/quotes.txt', encoding='utf-8') as f:


			reply = 'Quote #' + str(quote_num) + ' by ' + originator + \
			        ' has been added.'
			send_message(s, reply)
		"""


	def comm_anime(self, s):
		reply = 'Visit https://kitsu.io/users/curtissimo/library to check out \
				 which animu I\'ve seen, am currently watching, & plan to \
				 watch!'
		send_message(s, reply)


	def comm_band(self, s):
		reply = '🎤 Tuturu curtisLewd 🎸 MakiShy ⌨️'
		send_message(s, reply)


	def comm_bondwithme(self, s):
		reply = 'WutFace https://www.youtube.com/watch?v=LB871SVYMhI WutFace'
		send_message(s, reply)


	def comm_brush(self, s):
		reply = 'NiceMoves WAG NiceMoves THAT NiceMoves BRUSH NiceMoves'
		send_message(s, reply)


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


	def comm_dancebitches(self, s):
		reply = 'NiceMoves PepePls dittoPride MagDance NiceMoves PepePls \
		 		 dittoPride MagDance NiceMoves PepePls dittoPride MagDance \
				 NiceMoves PepePls dittoPride MagDance NiceMoves PepePls \
				 dittoPride MagDance NiceMoves PepePls dittoPride MagDance \
				 NiceMoves PepePls dittoPride MagDance NiceMoves PepePls \
				 dittoPride MagDance NiceMoves PepePls dittoPride MagDance \
				 NiceMoves PepePls dittoPride MagDance NiceMoves PepePls \
				 dittoPride MagDance NiceMoves PepePls dittoPride MagDance \
				 NiceMoves'
		send_message(s, reply)


	def comm_discord(self, s):
		reply = 'Tuturu https://discord.gg/T7Bhj9z Tuturu'
		send_message(s, reply)


	def comm_dontworry(self, s):
		reply = 'FeelsOakyMan https://clips.twitch.tv/HardLuckyWormUncleNox \
			   	 FeelsOakyMan'
		send_message(s, reply)


	def comm_drop(self, s):
		reply = '/me ┏(-_-)┓ ┏(-_-)┛ ┗(-_- )┓ ┗(-_-)┛ ┏(-_-)┓ ┏( -_-)┛ \
				 ┗(-_- )┓ ┗(-_-)┛ ┏(-_-)┓ ┏(-_-)┛ ┗(-_-)┓ ┗(-_-)┛ ┏(-_-)┓ \
				 ┏(-_-)┛ ┏(-_-)┓ ┏(-_-)┛ ┗(-_- )┓ ┗(-_-)┛ ┏(-_-)┓ ┏( -_-)┛ \
				 ┗(-_-)┓ ┗(-_-)┛ ┏(-_-)┓ ┏(-_-)┛ ┗(-_- )┓ ┗(-_-)┛ ┏(-_-)┓ \
				 ┏(-_-)┛'
		send_message(s, reply)


	def comm_editquote(self, s, arglist):
		send_message(s, 'Command coming soon!!')


	def comm_ffz(self, s):
		return_msg = 'FFZ emotes for this channel: '
		for emote in self.ffzEmotes:
			return_msg += emote['name'] + ' '

		send_message(s, return_msg)


	def comm_followage(self, s):
		url = 'https://decapi.me/twitch/followage/' + CHANNEL + '/' + \
			   self.user + '?precision=7'
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()

		if soup == 'A user cannot follow themself.':
			send_message(s, 'You can\'t follow yourself, idiot FeelsWeirdMan')
		else:
			send_message(s, self.user + ' has been following ' + CHANNEL + \
						 ' for ' + soup + '.')


	def comm_host(self, s):
		reply = 'haHAA hey streamer haHAA can you host me after this? haHAA \
				 trying to reach affiliate, thanks haHAA'
		send_message(s, reply)


	def comm_kylf(self, s):
		reply = '/me Gotta give big papi Kylf the guud succ'
		send_message(s, reply)


	def comm_legends(self, s):
		reply = 'Users who have greatly improved some of my playthroughs \
				 through helpful tips and advice are: itspieflavor (Tales of \
				 Symphonia), BlasianMaestro (Mega Man X), & dreadpirateht \
				 (Final Fantasy VIII)'
		send_message(s, reply)


	def comm_lotus(self, s):
		reply = 'slash ban Lotus WutFace'
		send_message(s, reply)


	def comm_over(self, s):
		reply = 'SwiftRage \
				 https://soundcloud.com/seth-joy/cheese05-ovah-trap-remix \
			   	 SwiftRage (courtesy of cheese FeelsOakyMan )'
		send_message(s, reply)


	def comm_playtwos(self, s):
		reply = 'In an attempt to keep things s p i c y & fresh, I will be \
				 alternating between one longer, more intense game and one \
				 shorter, simpler game at a time! Current pairing: Persona 5 \
				 (Long) / Donkey Kong Country 3 (Short)'
		send_message(s, reply)


	def comm_quote(self, s, arglist):
		quote_id = 0
		if len(arglist) > 0:
			try:
				quote_id = int(arglist[0]) - 1
			except:
				pass

		with open('Resources/quotes.txt', encoding='utf-8') as f:
			quotes_list = f.readlines()
			if quote_id == 0:
				quote_id = random.randrange(0, len(quotes_list))
			print(quote_id)
			send_message(s, 'Quote #' + str(quote_id + 1) + ': ' + \
						 quotes_list[quote_id])


	def comm_remquote(self, s, arglist):
		send_message(s, 'Command coming soon!!')


	def comm_shakeit(self, s):
		reply = 'NiceMoves https://www.youtube.com/watch?v=_wjFahULCK8 \
				 NiceMoves'
		send_message(s, reply)


	def comm_sudoku(self, s):
		reply = '/timeout ' + self.user + ' 5'
		send_message(s, reply)
		send_message(s, '/me FeelsBadMan 🗡️ An honorable way to go.')


	def comm_test(self, s):
		# fucky command, just for testing new stuff
		messageTemp = bytes('USERSTATE #' + CHANNEL + ' :curtissimo41', 'utf-8')
		# s.send(messageTemp + b'\r\n')
		s.send(bytes('WHO ' + CHANNEL + '\r\n', 'utf-8'))


	def comm_tumblingdown(self, s):
		reply = "/me I know I know I\'ve let you down FeelsBadMan 🕯️ I\'ve \
				 been a fool to myself FeelsBadMan 🕯️ I thought that I could \
				 live for no one else FeelsBadMan 🕯️ But now through all the \
				 hurt and pain FeelsBadMan 🕯️ It\'s time for me to respect \
				 FeelsBadMan 🕯️ The ones who love me more than anything \
				 FeelsBadMan 🕯️ So with sadness in my heart FeelsBadMan 🕯️ \
				 Feel the best thing I could do FeelsBadMan 🕯️ Is end it all \
				 and leave forever FeelsBadMan 🕯"
		send_message(s, reply)


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
				# respond to PING message, to avoid timing out
				if line.split(' ')[0] == 'PING':
					s.send(bytes(line.replace('PING', 'PONG'), 'utf-8'))
					continue
				else:
					try:
						self.user = get_user(line)
						self.msg = get_message(line)
						self.badges = get_badges(line)
					except:
						break

					commandname = ''
					arglist = []

					for i in range(0, len(self.msg) - 1):
						if self.msg[i] in self.bannedTerms:
							timeoutMsg = '/timeout ' + self.user + ' 600'
							send_message(s, 'JKanStyle JKanStyle JKanStyle \
																	JKanStyle')
							send_message(s, timeoutMsg)
						elif i is 0:
							if self.msg[i] in self.commandsBasic:
								self.commandsBasic[self.msg[i]](self, s)
							elif self.msg[i] in self.commandsQuote:
								commandname = self.msg[i]
						elif commandname is not '' and i is not 0:
							arglist.append(self.msg[i])

					if commandname is not '':
						if commandname in self.commandsQuote:
							self.commandsQuote[commandname](self, s, arglist)

	commandsBasic = {
		'!anime': comm_anime,
		'!band': comm_band,
		'!bondwithme': comm_bondwithme,
		'!brush': comm_brush,
		'!bttv': comm_bttv,
		'!chatters': comm_chatters,
		'!commands': comm_commands,
		'!dancebitches': comm_dancebitches,
		'!dontworry': comm_dontworry,
		'!discord': comm_discord,
		'!drop': comm_drop,
		'!ffz': comm_ffz,
		'!followage': comm_followage,
		'!host': comm_host,
		'!kylf': comm_kylf,
		'!legends': comm_legends,
		'!lotus': comm_lotus,
		'!over': comm_over,
		'!sudoku': comm_sudoku,
		'!test': comm_test,
		'!tumblingdown': comm_tumblingdown,
		'!uptime': comm_uptime
	}

	commandsQuote = {
		'!addquote': comm_addquote,
		'!editquote': comm_editquote,
		'!quote': comm_quote,
		'!remquote': comm_remquote
	}


# ------------------------------------------------------------------------------
# ------------------------------------main--------------------------------------
# ------------------------------------------------------------------------------
if __name__ == '__main__':
	bot = Botissimo()
