import requests
from Settings import CHANNEL
from bs4 import BeautifulSoup
import json


def get_bttv_emotes():
	url = 'https://decapi.me/bttv/emotes?channel=' + CHANNEL
	response = requests.get(url)
	return BeautifulSoup(response.content, "html.parser").get_text()


def get_ffz_emotes():
	url = 'https://api.frankerfacez.com/v1/room/' + CHANNEL
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser").prettify()
	soup_dict = json.loads(soup)
	room_emote_set = soup_dict['room']['set']
	return json.loads(soup)['sets'][str(room_emote_set)]['emoticons']


def get_current_date():
	pass


def get_current_game():
	pass


def get_stream_title():
	pass


def set_current_game():
	pass


def set_stream_title():
	pass
