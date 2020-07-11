from bs4 import BeautifulSoup
from Initialize import join_room
from readInput import get_badges, get_user, get_message, parse_yt_link
from Settings import CHANNEL, BANNEDTERMS, GAMES_DICT, YT_BANLIST
from Socket import open_socket, send_message
from timeBasedModule import runTBM, cmdsOnCooldown

import helpers
import json
import requests
import threading
import time
import os

class Botissimo:
	commandsCmds = ['!addcomm', '!delcomm', '!editcomm']
	commandsQuote = ['!addquote', '!editquote', '!quote', '!delquote']

	# compile list of all channel commands
	basicCommandJSON = {}
	fileDir = f'{os.path.dirname(os.path.realpath(__file__))}/'
	with open(f'{fileDir}commandsBasic.txt', encoding = 'utf-8') as basicCommandFile:
		basicCommandJSON = json.load(basicCommandFile)

	def __init__(self):
		s = open_socket()
		join_room(s)

		# start timeBasedModule thread in background
		tbmThread = threading.Thread(target=runTBM, args=[s])
		tbmThread.daemon = True
		tbmThread.start()

		readbuffer = ''
		send_message(s, 'We in there boiii (Botissimo, v. 0.5.5)')
		self.run(s, readbuffer)

	# --------------------------------------------------------------------------
	# ------------------------------Bot Functions-------------------------------
	# --------------------------------------------------------------------------
	def bannedTermTimeout(self, s, user):
		timeoutMsg = f'/timeout {user} 300'
		send_message(s, timeoutMsg)
		send_message(s, 'Hey, pal...let\'s not do that FeelsWeirdMan')

	def isMod(self, badges):
		if 'broadcaster' in badges or 'moderator' in badges:
			return True
		else:
			return False

	def comm_bttv(self, s):
		send_message(s, f'BetterTTV emotes for this channel: {helpers.get_bttv_emotes()}')

	def comm_ffz(self, s):
		send_message(s, f'FFZ emotes for this channel: {helpers.get_ffz_emotes()}')

	def comm_followage(self, s, user):
		url = f'https://decapi.me/twitch/followage/{CHANNEL}/{user}?precision=7'
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()

		if soup == 'A user cannot follow themself.':
			send_message(s, 'You can\'t follow yourself, idiot FeelsWeirdMan')
		elif soup == 'Follow not found':
			send_message(s, 'Not following? I see how it is FeelsWeirdMan')
		else:
			send_message(s, f'{user} has been following {CHANNEL} for {soup}.')
		
	def comm_sudoku(self, s, user):
		reply = f'/timeout {user} 5'
		send_message(s, reply)
		send_message(s, '/me FeelsBadMan 🗡️ An honorable way to go.')

	def comm_uptime(self, s):
		url = f'https://decapi.me/twitch/uptime?channel={CHANNEL}'
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser").get_text()

		if soup == f'{CHANNEL} is offline':
			send_message(s, f'{CHANNEL.capitalize()} is offline.')
		else:
			send_message(s, f'{CHANNEL.capitalize()} has been live for {soup}')

	# --------------------------------------------------------------------------
	# ------------------------------Main Function-------------------------------
	# --------------------------------------------------------------------------
	def run(self, s, readbuffer):
		while True:
			print('\n===Start of new wait period.===\n')
			readbuffer = ''
			try:
				readbuffer = s.recv(1024).decode('utf-8')
			except:
				print('Loop broke, starting new loop.\n')
			if not readbuffer:
				s = open_socket()
				continue
			temp = readbuffer.split('\n')
			readbuffer = temp.pop()

			for line in temp:
				print(f'{str(line).encode("utf-8")}\n')
				if line.split(' ')[0] == 'PING':
					s.send(bytes(line.replace('PING', 'PONG'), 'utf-8'))
					send_message(s, 'Refreshed bot.')
					continue
				else:
					msgThread = threading.Thread(target=self.run_thread, args=[s, line])
					msgThread.daemon = True
					msgThread.start()
					
	def run_thread(self, s, line):
		try:
			user = get_user(line)
			msg = get_message(line)
			badges = get_badges(line)
		except:
			return

		print(f'{str(user)}: {str(msg).encode("utf-8")}\n')

		if " ".join(msg[0:]) == 'yo gl' and 'yo gl' not in cmdsOnCooldown:
			send_message(s, 'yo thanks FeelsOkayMan 👍')
			cmdsOnCooldown['yo gl'] = int(time.time()) + 60

		for i in range(0, len(msg)):
			if msg[i].lower() in BANNEDTERMS:
				self.bannedTermTimeout(s, user)
				break

			elif 'youtube' in msg[i] or 'youtu.be' in msg[i]:
				try:
					yt_code = parse_yt_link(msg[i])
					if yt_code in YT_BANLIST:
						send_message(s, 'Nice try...except that it wasn\'t FeelsWeirdMan')
						break
					vidMeta = helpers.get_yt_metadata(yt_code)
					send_message(s, f'{user} linked the video "{vidMeta[0]}", uploaded by {vidMeta[1]} ({vidMeta[2]} '
									f'views, {vidMeta[3]} Likes, {vidMeta[4]} Dislikes)')
				except:
					pass

			elif i is 0:
				if msg[i] in self.basicCommandJSON and msg[i] not in cmdsOnCooldown:
					send_message(s, self.basicCommandJSON[msg[i]]['return'])
					cooldown = self.basicCommandJSON[msg[i]]['cooldown']
					cmdsOnCooldown[msg[i]] = int(time.time()) + cooldown

				elif msg[i] in self.commandsBot and msg[i] not in cmdsOnCooldown:
					self.commandsBot[msg[i]](self, s)
					cmdsOnCooldown[msg[i]] = int(time.time()) + 60

				elif msg[i] == '!followage':
					self.comm_followage(s, user)

				elif msg[i] == '!sudoku':
					self.comm_sudoku(s, user)

				elif msg[i] == '!setgame' and self.isMod(badges):
					try:
						if msg[1] in GAMES_DICT:
							send_message(s, helpers.set_current_game(GAMES_DICT[msg[1]]))
						else:
							send_message(s, helpers.set_current_game(' '.join(msg[1:])))
					except:
						send_message(s, 'Correct usage: !setgame <game>')
					
				elif msg[i] == '!settitle' and self.isMod(badges):
					try:
						title = " ".join(msg[1:])
						helpers.set_current_title(title)
						send_message(s, 'Stream title updated FeelsOkayMan 👍')
					except:
						send_message(s, 'Error when setting stream title monakS')

				elif msg[i] in self.commandsCmds and self.isMod(badges):
					send_message(s, helpers.edit_cmds(msg, self.basicCommandJSON))

				elif msg[i] in self.commandsQuote:
					send_message(s, helpers.edit_quotes(msg, self.isMod(badges)))

	commandsBot = {
		'!bttv': comm_bttv,
		'!ffz': comm_ffz,
		'!uptime': comm_uptime
	}


if __name__ == '__main__':
	bot = Botissimo()
