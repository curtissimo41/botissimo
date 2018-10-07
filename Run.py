# ------------------------------------------------------------------------------
# -----------------------------------Imports------------------------------------
# ------------------------------------------------------------------------------
from Socket import open_socket, send_message
from Initialize import join_room
from readInput import get_user, get_message
import requests
from Settings import CHANNEL
from bs4 import BeautifulSoup
import json
import random


# ------------------------------------------------------------------------------
# ----------------------------------Bot Class-----------------------------------
# ------------------------------------------------------------------------------
class Botissimo:
	user = ''
	msg = ''

	def __init__(self):
		s = open_socket()
		join_room(s)
		readbuffer = ''
		self.run(s, readbuffer)

	def comm_addquote(self, s):
		pass

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

	def comm_bttv(self, s):
		url = 'https://decapi.me/bttv/emotes?channel=' + CHANNEL
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()
		send_message(s, 'BetterTTV emotes for this channel: ' + soup)

	def comm_commands(self, s):
		send_message(s, 'Command coming soon!!')

	def comm_dancebitches(self, s):
		reply = 'NiceMoves PepePls dittoPride RareMonkey NiceMoves PepePls \
				 dittoPride RareMonkey NiceMoves PepePls dittoPride RareMonkey \
				 NiceMoves PepePls dittoPride NiceMoves PepePls dittoPride \
				 RareMonkey PepePls dittoPride RareMonkey NiceMoves PepePls \
				 dittoPride RareMonkey'
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

	def comm_ffz(self, s):
		url = 'https://api.frankerfacez.com/v1/room/' + CHANNEL
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").prettify()
		soup_dict = json.loads(soup)
		room_emote_set = soup_dict['room']['set']
		emotes_dict = json.loads(soup)['sets'][str(room_emote_set)]['emoticons']
		emotes_list = []

		return_msg = 'FFZ emotes for this channel: '
		for emote in emotes_dict:
			return_msg += emote['name'] + ' '

		send_message(s, return_msg)

	def comm_followage(self, s):
		url = 'https://decapi.me/twitch/followage/' + CHANNEL + '/' + \
			   self.user + '?precision=7'
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()

		if soup == 'A user cannot follow themself.':
			send_message(s, 'A user cannot follow his/her self.')
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
			   	 SwiftRage (courtesy of cheese05 FeelsOakyMan )'
		send_message(s, reply)

	def comm_quote(self, s):
		with open('Resources/quotes.txt', encoding='utf-8') as f:
			quotes_list = f.readlines()
			rand_num = random.randrange(0, len(quotes_list))
			print(rand_num)
			send_message(s, 'Quote #' + str(rand_num) + ': ' + \
						 quotes_list[rand_num])

	def comm_sudoku(self, s):
		reply = '/timeout ' + self.user + ' 5'
		send_message(s, reply)
		send_message(s, '/me FeelsBadMan 🗡️ An honorable way to go.')

	def comm_test(self, s):
		# fucky command, just for testing new stuff
		messageTemp = bytes('CLEARCHAT #' + CHANNEL + ' :v4r0123', 'utf-8')
		s.send(messageTemp + b'\r\n')

	def comm_uptime(self, s):
		url = 'https://decapi.me/twitch/uptime?channel=' + CHANNEL
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()

		if soup == (CHANNEL + ' is offline'):
			send_message(s, CHANNEL.capitalize() + ' is offline.')
		else:
			send_message(s, CHANNEL.capitalize() + ' has been live for ' + soup)

	def run(self, s, readbuffer):
		while True:
			readbuffer = readbuffer + s.recv(1024).decode('utf-8')
			print(readbuffer)
			temp = readbuffer.split('\n')
			readbuffer = temp.pop()

			for line in temp:
				if line.split(' ')[0] == 'PING':
					s.send(bytes(line.replace('PING', 'PONG'), 'utf-8'))
				else:
					self.user = get_user(line)
					self.msg = get_message(line).replace('\r', ' ').split(' ')

					if '!fakeCommand' in self.msg:
						send_message(s, 'Kappa')

					elif 'fggTayTay' in self.msg: # create list of banned words
						timeoutMsg = '/timeout ' + self.user + ' 600'
						send_message(s, 'JKanStyle JKanStyle JKanStyle \
										JKanStyle')
						send_message(s, timeoutMsg)

					elif self.msg[0] in self.commands:
						self.commands[self.msg[0]](self, s)

	commands = {
		'!anime': comm_anime,
		'!band': comm_band,
		'!bondwithme': comm_bondwithme,
		'!bttv': comm_bttv,
		'!commands': comm_commands,
		'!dancebitches': comm_dancebitches,
		'!dontworry': comm_dontworry,
		'!drop': comm_drop,
		'!ffz': comm_ffz,
		'!followage': comm_followage,
		'!host': comm_host,
		'!kylf': comm_kylf,
		'!legends': comm_legends,
		'!lotus': comm_lotus,
		'!over': comm_over,
		'!quote': comm_quote,
		'!sudoku': comm_sudoku,
		'!test': comm_test,
		'!uptime': comm_uptime
	}


# ------------------------------------------------------------------------------
# ------------------------------helper functions--------------------------------
# ------------------------------------------------------------------------------
def get_current_game():
	pass

def get_stream_title():
	pass

def set_current_game():
	pass

def set_stream_title():
	pass


# ------------------------------------------------------------------------------
# ------------------------------------main--------------------------------------
# ------------------------------------------------------------------------------
if __name__ == '__main__':
	bot = Botissimo()
	bot.run()
