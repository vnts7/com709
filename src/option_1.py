from helpers import *
from datetime import timedelta
import textwrap


def option_1():
    """Prints the details of the top ranked song for a particular day.
    """
    date = input_date()
    rows = query_option_1(date)
    show_result_option_1(rows)


def query_option_1(date):
	"""Perform query of option 1

	Parameters
	----------
	date: datetime
		date passed in the query

	Returns
	-------
	list
		a list of rows returned from the database
	"""
	sql_query = '''
	SELECT
		c.id, c.date,
		c.song, c.artist,
		c.last, c.weeks
	FROM chart c
	WHERE c.date = ? and c.rank = 1;
	'''
	# Loop and execute sql to find the date on board that week 
	# (week that the date input belongs to), if found -> break
	for _ in range(7):
		rows = query(sql_query, date.strftime("%Y-%m-%d"))
		if (rows):
			break
		date = date - timedelta(days=1)
	return rows


def show_result_option_1(rows):
	"""Display the result of option 1 to the user.

	Parameters
	----------
	rows: list
		a list of rows to print
    """
	# If no row was found, print statement and return
	if not rows:
		print('No top ranked song found on this date')
		return

	# print the result
	# header
	width = 135
	h = ['ID', 'Ranking Date ', 'Song Title',
			'Artist', 'Rank Last Week', 'Weeks On Board']
	print(f'{h[0]:10}{h[1]:20}{textwrap.shorten(h[2], 35):40}{textwrap.shorten(h[3], 25):30}{h[4]:20}{h[5]:20}')
	print('─' * (width))
	# data
	for r in rows:
		print(f'{r[0]:<10}{r[1]:20}{textwrap.shorten(r[2], 35):40}{textwrap.shorten(r[3], 25):30}{r[4]:<20}{r[5]:<20}')
