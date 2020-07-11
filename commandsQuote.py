import random
import os

fileDir = f'{os.path.dirname(os.path.realpath(__file__))}/'

def addquote(spokenBy, quote, currentDate, currentGame):
	if not quote:
		return 'Correct usage: !addquote <spoken by> <quote>'
		
	quote_num = 0
	quote_to_add = f'"{quote}" - {spokenBy} [{currentGame}, {currentDate}]'

	try:
		with open(f'{fileDir}Resources/quotes.txt', 'r+', encoding = 'utf-8') as f:
			quote_num = len(f.readlines()) + 1
			f.write(f'{quote_to_add}\n')
		return f'Quote #{quote_num} by {spokenBy} has been added FeelsOkayMan 👍'
	except:
		return 'Encountered a problem when opening the file to add the quote monakS'


def editquote(quote_id, spokenBy, quote):
	try:
		with open(f'{fileDir}Resources/quotes.txt', 'r+', encoding = 'utf-8') as f:
			lines = f.readlines()
			if quote_id < 0 or quote_id >= len(lines):
				return 'Quote does not exist FeelsWeirdMan'
			oldQuoteInfo = lines[quote_id].split('[')[1]
			newQuote = f'"{quote}" - {spokenBy} [{oldQuoteInfo}'
			lines[quote_id] = newQuote
			f.seek(0)
			f.truncate()
			f.writelines(lines)
	except:
		return 'Encountered a problem when opening the file to edit the quote monakS'

	return f'Quote #{quote_id+1} by {spokenBy} has been edited FeelsOkayMan 👍'


def quote(quote_id):
	try:
		with open(f'{fileDir}Resources/quotes.txt', 'r', encoding = 'utf-8') as f:
			quotes_list = f.readlines()
			if quote_id < 0 or quote_id >= len(quotes_list):
				quote_id = random.randrange(0, len(quotes_list))
			return f'Quote #{quote_id + 1}: {quotes_list[quote_id]}'
	except:
		return 'Could not access the quotes monakS'


def delquote(quote_id):
	try:
		with open(f'{fileDir}Resources/quotes.txt', 'r+', encoding = 'utf-8') as f:
			lines = f.readlines()
			if quote_id < 0 or quote_id >= len(lines):
				return 'Quote does not exist FeelsWeirdMan'
			del lines[quote_id]
			f.seek(0)
			f.truncate()
			f.writelines(lines)
			return f'Quote #{quote_id+1} successfully removed madnakS 👎'
	except:
		return 'Could not remove quote monakS'
