from Socket import openSocket, sendMessage
from Initialize import joinRoom
from readInput import getUser, getMessage
import requests
from Settings import CHANNEL
from bs4 import BeautifulSoup


s = openSocket()
joinRoom(s)
readbuffer = ''

while True:
	readbuffer = readbuffer + s.recv(1024).decode('utf-8')
	print(readbuffer)
	temp = readbuffer.split('\n')
	readbuffer = temp.pop()

	for line in temp:
		if line.split(' ')[0] == 'PING':
			s.send(bytes(line.replace('PING', 'PONG'), 'utf-8'))
		else:
			user = getUser(line)
			msg = getMessage(line).replace('\r', ' ').split(' ')

			if '!fakeCommand' in msg:
				sendMessage(s, 'Kappa')

			elif 'fggTayTay' in msg:
				timeoutMsg = '/timeout ' + user + ' 600'
				sendMessage(s, timeoutMsg)
				sendMessage(s, 'JKanStyle JKanStyle JKanStyle JKanStyle')

			elif msg[0] == '!dancebitches':
				dance = 'NiceMoves PepePls dittoPride RareMonkey NiceMoves \
                       PepePls dittoPride RareMonkey NiceMoves PepePls \
                       dittoPride RareMonkey NiceMoves PepePls dittoPride \
                       RareMonkey NiceMoves PepePls dittoPride RareMonkey \
                       NiceMoves PepePls dittoPride RareMonkey NiceMoves \
                       PepePls dittoPride RareMonkey'
				sendMessage(s, dance)

			elif msg[0] == '!band':
				reply = '🎤 Tuturu curtisLewd 🎸 MakiShy ⌨️'
				sendMessage(s, reply)

			elif msg[0] == '!dontworry':
				reply = 'FeelsOakyMan \
                       https://clips.twitch.tv/HardLuckyWormUncleNox \
                       FeelsOakyMan'
				sendMessage(s, reply)

			elif msg[0] == '!host':
				reply = 'haHAA hey streamer haHAA can you host me after this? \
                       haHAA trying to reach affiliate, thanks haHAA'
				sendMessage(s, reply)

			elif msg[0] == '!kylf':
				reply = '/me Gotta give big papi Kylf the guud succ'
				sendMessage(s, reply)

			elif msg[0] == '!over':
				reply = 'SwiftRage \
                       https://soundcloud.com/seth-joy/cheese05-ovah-trap-remix\
                       SwiftRage (courtesy of cheese05 FeelsOakyMan )'
				sendMessage(s, reply)

			elif msg[0] == '!anime':
				reply = 'Visit https://kitsu.io/users/curtissimo/library to \
                         check out which animu I\'ve seen, am currently \
                         watching, & plan to watch!'
				sendMessage(s, reply)

			elif msg[0] == '!bondwithme':
				reply = 'WutFace https://www.youtube.com/watch?v=LB871SVYMhI \
                         WutFace'
				sendMessage(s, reply)

			elif msg[0] == '!drop':
				reply = '/me ┏(-_-)┓ ┏(-_-)┛ ┗(-_- )┓ ┗(-_-)┛ ┏(-_-)┓ ┏( -_-)┛ \
                         ┗(-_- )┓ ┗(-_-)┛ ┏(-_-)┓ ┏(-_-)┛ ┗(-_-)┓ ┗(-_-)┛ \
                         ┏(-_-)┓ ┏(-_-)┛ ┏(-_-)┓ ┏(-_-)┛ ┗(-_- )┓ ┗(-_-)┛ \
                         ┏(-_-)┓ ┏( -_-)┛ ┗(-_-)┓ ┗(-_-)┛ ┏(-_-)┓ ┏(-_-)┛ \
                         ┗(-_- )┓ ┗(-_-)┛ ┏(-_-)┓ ┏(-_-)┛'
				sendMessage(s, reply)

			elif msg[0] == '!legends':
				reply = 'Users who have greatly improved some of my \
                         playthroughs through helpful tips and advice are: \
                         itspieflavor (Tales of Symphonia), BlasianMaestro \
                         (Mega Man X), & dreadpirateht (Final Fantasy VIII)'
				sendMessage(s, reply)

			elif msg[0] == '!lotus':
				reply = 'slash ban Lotus WutFace'
				sendMessage(s, reply)

			elif msg[0] == '!sudoku':
				reply = '/timeout ' + user + ' 5'
				sendMessage(s, reply)
				sendMessage(s, '/me FeelsBadMan 🗡️ An honorable way to go.')

			elif msg[0] == '!followage':
				url = 'https://decapi.me/twitch/followage/' + CHANNEL + \
				      '/' + user + '?precision=7'
				response = requests.get(url)
				soup = BeautifulSoup(response.content, "html.parser").get_text()

				if soup == 'A user cannot follow themself.':
					sendMessage(s, 'A user cannot follow his/her self.')
				else:
					sendMessage(s, user + ', you have been following ' +
					            CHANNEL + ' for ' + soup + '.')

			elif msg[0] == '!uptime':
				url = 'https://decapi.me/twitch/uptime?channel=' + CHANNEL
				response = requests.get(url)
				soup = BeautifulSoup(response.content, "html.parser").get_text()

				if soup == (CHANNEL + ' is offline'):
					sendMessage(s, CHANNEL + ' is offline.')
				else:
					sendMessage(s, CHANNEL + ' has been live for ' + soup)

			elif msg[0] == '!bttv':
				url = 'https://decapi.me/bttv/emotes?channel=' + CHANNEL
				response = requests.get(url)
				soup = BeautifulSoup(response.content, "html.parser").get_text()
				sendMessage(s, 'BetterTTV emotes for this channel: ' + soup)