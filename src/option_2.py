from helpers import *
import textwrap


def option_2():
    """Prints the details of the artists having top ranked songs
          and the quantity of the top ranked songs of these artists in a particular year.
    """
    year = input_year()
    rows = query_option_2(year)
    show_result_option_2(rows)


def query_option_2(year):
	"""Perform query of option 2

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
		c.artist,
		count(DISTINCT c.song) as Quantity
	FROM chart c
	WHERE c.rank = 1 and strftime('%Y', c.date) = ?
	GROUP BY c.Artist
	ORDER BY Quantity DESC;
	'''
	# connect db and execute sql
	rows = query(sql_query, str(year))
	return rows


def show_result_option_2(rows):
	"""Display the result of option 2 to the user.

	Parameters
	----------
	rows: list
		a list of rows to print
    """
	# If no row was found, print statement and return
	if not rows:
		print('No top ranked song on this year')
		return
	# print the result
	# header
	width = 55
	h = ['Artist', 'Quantity of Top Ranked Songs']
	print(f'{textwrap.shorten(h[0], 25):30}{h[1]:20}')
	print('─' * (width))
	# data
	for r in rows:
		print(f'{textwrap.shorten(r[0], 25):30}{r[1]:<20}')
