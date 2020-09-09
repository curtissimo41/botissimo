import re
import requests
from Settings import CHANNEL, CHANNEL_ID, PASS, CLIENT_ID, YT_API_KEY
from bs4 import BeautifulSoup
import json
from datetime import datetime
from commandsCommands import addcomm, delcomm, editcomm
from commandsQuote import addquote, editquote, quote, delquote
from pyyoutube import Api, models

import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()
yt_service.ssl = True

def edit_cmds(msg, cmd_JSON):
	if msg[0] == '!addcomm':
		try:
			return addcomm(cmd_JSON, msg[1], msg[2:])
		except:
			return 'Correct usage: !addcomm <name> <message>'
	elif msg[0] == '!delcomm':
		try:
			return delcomm(cmd_JSON, msg[1])
		except:
			return 'Correct usage: !delcomm <name>'
	else:
		try:
			return editcomm(cmd_JSON, msg[1], msg[2:])
		except:
			return 'Correct usage: !editcomm <name> <new message>'


def edit_quotes(msg, is_mod):
	if msg[0] != '!quote' and is_mod:
		if msg[0] == '!addquote':
			try:
				return addquote(msg[1], ' '.join(msg[2:]), get_current_date(), get_current_game())
			except:
				return 'Correct usage: !addquote <spoken by> <quote>'
		elif msg[0] == '!editquote':
			try:
				return editquote(int(msg[1]) - 1, msg[2], ' '.join(msg[3:]))
			except:
				return 'Correct usage: !editquote <quote ID> <spoken by> <quote>'
		else:
			try:
				return delquote(int(msg[1]) - 1)
			except:
				return 'Correct usage: !delquote <quote ID>'
	else:
		try:
			quote_id = int(msg[1]) - 1
		except:
			quote_id = -1
		return quote(quote_id)


def get_bttv_emotes():
	url = f'https://decapi.me/bttv/emotes?channel={CHANNEL}'
	response = requests.get(url)
	return BeautifulSoup(response.content, "html.parser").get_text()


def get_ffz_emotes():
	url = f'https://decapi.me/ffz/emotes/{CHANNEL}'
	response = requests.get(url)
	return BeautifulSoup(response.content, "html.parser").get_text()


def get_current_date():
	return datetime.now().strftime('%m/%d/%Y')


def get_current_game():
	url = f'https://decapi.me/twitch/game/{CHANNEL}'
	response = requests.get(url)
	currGame = BeautifulSoup(response.content, "html.parser").get_text()
	return currGame


def get_stream_title():
	url = f'https://decapi.me/twitch/status/{CHANNEL}'
	response = requests.get(url)
	return BeautifulSoup(response.content, "html.parser").get_text()


def get_user_info(username):
	url = f'https://api.twitch.tv/kraken/users?login={username}'
	headers = {
		"Client-ID": f"{CLIENT_ID}",
		"Accept": "application/vnd.twitchtv.v5+json",
		"Authorization": f"OAuth {PASS.split(':')[1]}"
	}
	data = requests.get(url=url, headers=headers)
	return json.loads(BeautifulSoup(data.content, "html.parser").get_text())['users'][0]['updated_at'].split('T')[0]


def get_yt_metadata(url):
	videoInfo = f'https://www.googleapis.com/youtube/v3/videos?id={url}&part=contentDetails&key={YT_API_KEY}&fields=' \
				f'items(id,snippet(channelTitle,title),statistics)&part=snippet,statistics'
	response = requests.get(videoInfo)
	videoData = json.loads(BeautifulSoup(response.content, "html.parser").get_text())['items'][0]
	
	title = videoData['snippet']['title']
	uploader = videoData['snippet']['channelTitle']
	views = videoData['statistics']['viewCount']
	likes = videoData['statistics']['likeCount']
	dislikes = videoData['statistics']['dislikeCount']

	return (title, uploader, views, likes, dislikes)


def set_current_game(game):
	url = f'https://api.twitch.tv/kraken/channels/{CHANNEL_ID}'
	headers = {
		"Client-ID": f"{CLIENT_ID}",
		"Accept": "application/vnd.twitchtv.v5+json",
		"Authorization": f"OAuth {PASS.split(':')[1]}"
	}
	data = {
		'channel[game]': game
	}
	requests.put(url=url, headers=headers, data=data)

	global currGame
	currGame = game

	return 'Stream category updated FeelsOkayMan 👍'


def set_current_title(title):
	url = f"https://api.twitch.tv/kraken/channels/{CHANNEL_ID}"
	headers = {
		"Client-ID": f"{CLIENT_ID}",
		"Accept": "application/vnd.twitchtv.v5+json",
		"Authorization": f"OAuth {PASS.split(':')[1]}"
	}
	data = {
		'channel[status]': title,
		'channel[game]': currGame
	}
	requests.put(url=url, headers=headers, data=data)

currGame = get_current_game()
