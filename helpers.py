import requests
from Settings import CHANNEL
from bs4 import BeautifulSoup
import json
from datetime import datetime


def get_bttv_emotes():
	url = 'https://decapi.me/bttv/emotes?channel=' + CHANNEL
	response = requests.get(url)
	return BeautifulSoup(response.content, "html.parser").get_text()


def get_ffz_emotes():
	url = 'https://decapi.me/ffz/emotes/' + CHANNEL
	response = requests.get(url)
	return BeautifulSoup(response.content, "html.parser").get_text()


def get_current_date():
	return datetime.now().strftime('%m/%d/%Y')


def get_current_game():
	url = 'https://decapi.me/twitch/game/' + CHANNEL
	response = requests.get(url)
	return BeautifulSoup(response.content, "html.parser").get_text()


def get_stream_title():
	url = 'https://decapi.me/twitch/status/' + CHANNEL
	response = requests.get(url)
	return BeautifulSoup(response.content, "html.parser").get_text()


def set_current_game():
	pass


def set_stream_title():
	pass
