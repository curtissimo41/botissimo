import random
from helpers import get_current_date, get_current_game


def addquote(arglist):
	if len(arglist) < 2:
		return 'Correct usage: !addquote <spoken by> <quote>'
	else:
		spokenBy = arglist[0]
		quote = ''
		quote_num = 0

		for i in range(1, len(arglist)):
			quote += arglist[i]
			if i != len(arglist) - 1:
				quote += ' '

		currentDate = get_current_date()
		currentGame = get_current_game()

		quote_to_add = '"' + quote + '" - ' + spokenBy + ' [' + currentGame + ', ' + \
		               currentDate + ']'

		with open('Resources/quotes.txt', 'r+') as f:
			quote_num = len(f.readlines()) + 1
			f.write(quote_to_add + '\n')

		reply = 'Quote #' + str(quote_num) + ' by ' + spokenBy + ' has been added FeelsOkayMan 👍'

	return reply


def editquote(arglist):
	# Correct usage: !editquote <quote ID> <spoken by> <quote>
	if len(arglist) < 3:
		return 'Correct usage: !editquote <quote ID> <spoken by> <quote>'
	else:
		try:
			quote_id = int(arglist[0]) - 1
		except:
			return 'Correct usage: !editquote <quote ID> <spoken by> <quote>'
		spokenBy = arglist[1]
		quote = ''

		for i in range(2, len(arglist)):
			quote += arglist[i]
			if i != len(arglist) - 1:
				quote += ' '

		with open('Resources/quotes.txt', 'r+') as f:
			lines = f.readlines()
			if quote_id < 0 or quote_id >= len(lines):
				return 'Quote does not exist FeelsWeirdMan'
			oldQuoteInfo = lines[quote_id].split('[')[1]
			newQuote = '"' + quote + '" - ' + spokenBy + ' [' + oldQuoteInfo
			lines[quote_id] = newQuote
			f.seek(0)
			f.truncate()
			f.writelines(lines)

		reply = 'Quote #' + str(quote_id+1) + ' by ' + spokenBy + ' has been edited FeelsOkayMan 👍'

	return reply


def quote(arglist):
	quote_id = -1

	if len(arglist) > 0:
		try:
			quote_id = int(arglist[0]) - 1
		except:
			pass

	with open('Resources/quotes.txt', 'r') as f:
		quotes_list = f.readlines()
		if quote_id < 0 or quote_id >= len(quotes_list):
			quote_id = random.randrange(0, len(quotes_list))
		return 'Quote #' + str(quote_id + 1) + ': ' + quotes_list[quote_id]


def remquote(arglist):
	quote_id = -1

	if len(arglist) > 0 or len(arglist) == 0:
		try:
			quote_id = int(arglist[0]) - 1
		except:
			return 'Correct usage: !remquote <quote ID>'

	with open('Resources/quotes.txt', 'r+') as f:
		lines = f.readlines()
		if quote_id < 0 or quote_id >= len(lines):
			return 'Quote does not exist FeelsWeirdMan'
		del lines[quote_id]
		f.seek(0)
		f.truncate()
		f.writelines(lines)

	return 'Quote #' + str(quote_id + 1) + ' successfully removed madnakS 👎'
