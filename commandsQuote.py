import random
import os
from helpers import get_current_date, get_current_game

fileDir = os.path.dirname(os.path.realpath(__file__)) + '/'

def addquote(arglist):
	if len(arglist) < 2:
		return 'Correct usage: !addquote <spoken by> <quote>'

	try:
		spokenBy = arglist[0]
		quote = ''
		quote_num = 0

		for i in range(1, len(arglist)):
			quote += arglist[i]
			if i != len(arglist) - 1:
				quote += ' '

		currentDate = get_current_date()
		currentGame = get_current_game()
		quote_to_add = '"{0}" - {1} [{2}, {3}]'.format(quote, spokenBy, currentGame, currentDate)
	except:
		return 'Encountered a problem when creating the quote monakS'

	try:
		with open(fileDir + 'Resources/quotes.txt', 'r+', encoding = 'utf-8') as f:
			quote_num = len(f.readlines()) + 1
			f.write(quote_to_add + '\n')
		return 'Quote #{0} by {1} has been added FeelsOkayMan 👍'.format(str(quote_num), spokenBy)
	except:
		return 'Encountered a problem when opening the file to add the quote monakS'


def editquote(arglist):
	if len(arglist) < 3:
		return 'Correct usage: !editquote <quote ID> <spoken by> <quote>'

	try:
		quote_id = int(arglist[0]) - 1
	except:
		return 'Correct usage: !editquote <quote ID> <spoken by> <quote>'

	try:
		spokenBy = arglist[1]
		quote = ''
		for i in range(2, len(arglist)):
			quote += arglist[i]
			if i != len(arglist) - 1:
				quote += ' '
	except:
		return 'Encountered a problem when editing the quote monakS'

	try:
		with open(fileDir + 'Resources/quotes.txt', 'r+', encoding = 'utf-8') as f:
			lines = f.readlines()
			if quote_id < 0 or quote_id >= len(lines):
				return 'Quote does not exist FeelsWeirdMan'
			oldQuoteInfo = lines[quote_id].split('[')[1]
			newQuote = '"{0}" - {1} [{2}'.format(quote, spokenBy, oldQuoteInfo)
			lines[quote_id] = newQuote
			f.seek(0)
			f.truncate()
			f.writelines(lines)
	except:
		return 'Encountered a problem when opening the file to edit the quote monakS'

	return 'Quote #{0} by {1} has been edited FeelsOkayMan 👍'.format(str(quote_id+1), spokenBy)


def quote(arglist):
	quote_id = -1
	try:
		quote_id = int(arglist[0]) - 1
	except:
		pass

	try:
		with open(fileDir + 'Resources/quotes.txt', 'r', encoding = 'utf-8') as f:
			quotes_list = f.readlines()
			if quote_id < 0 or quote_id >= len(quotes_list):
				quote_id = random.randrange(0, len(quotes_list))
			return 'Quote #{0}: {1}'.format(str(quote_id + 1), quotes_list[quote_id])
	except:
		return 'Could not access the quotes monakS'


def remquote(arglist):
	quote_id = -1
	try:
		quote_id = int(arglist[0]) - 1
	except:
		return 'Correct usage: !remquote <quote ID>'

	try:
		with open(fileDir + 'Resources/quotes.txt', 'r+', encoding = 'utf-8') as f:
			lines = f.readlines()
			if quote_id < 0 or quote_id >= len(lines):
				return 'Quote does not exist FeelsWeirdMan'
			del lines[quote_id]
			f.seek(0)
			f.truncate()
			f.writelines(lines)
			return 'Quote #{0} successfully removed madnakS 👎'.format(str(quote_id + 1))
	except:
		return 'Could not remove quote monakS'
