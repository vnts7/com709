from helpers import *
import textwrap


def option_4():
    """Prints the songs that has moved the most in ranking on the board in a particular year.
    """
    year = input_year()
    rows = query_option_4(year)
    show_result_option_4(rows)


def query_option_4(year):
	"""Perform query of option 4

	Parameters
	----------
	year: int
		year passed in the query

	Returns
	-------
	list
		a list of rows returned from the database
	"""

	sql_query = '''
	SELECT
		c.song, c.artist, (max(c.peak) - min(c.peak)) as RangeRank
	FROM chart c
	WHERE strftime('%Y', c.date) = ?
	GROUP BY c.song, c.artist
	ORDER BY RangeRank DESC
	LIMIT 1;
	'''
	# connect db and execute sql
	rows = query(sql_query, str(year))
	return rows


def show_result_option_4(rows):
	"""Display the result of option 4 to the user.

	Parameters
	----------
	rows: list
		a list of rows to print
    """
    # If no row was found, print statement and return
	if not rows:
		print('No song found in this year')
		return
	# print result
	# header
	width = 85
	h = ['Song Title', 'Artist', 'Ranking Range']
	print(
		f'{textwrap.shorten(h[0], 35):40}{textwrap.shorten(h[1], 25):30}{h[2]:20}')
	print('─' * (width))
	# data
	for r in rows:
		print(
			f'{textwrap.shorten(r[0], 35):40}{textwrap.shorten(r[1], 25):30}{r[2]:<20}')
