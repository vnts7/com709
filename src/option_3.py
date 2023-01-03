from helpers import *
import textwrap


def option_3():
    """Prints the details of the song with the longest number of weeks
       on the board of a particular artist.
    """
    artist = input_str('Artist')
    rows = query_option_3(artist)
    show_result_option_3(rows)


def query_option_3(artist):
	"""Perform query of option 3

	Parameters
	----------
	artist: string
		artist passed in the query

	Returns
	-------
	list
		a list of rows returned from the database
	"""
	sql_query = '''
	SELECT
		c.song, c.artist, COUNT(c.weeks) as WeeksOnBoard
	FROM chart c
	WHERE c.artist = ? COLLATE NOCASE
	GROUP BY c.song, c.artist
	ORDER BY WeeksOnBoard DESC
	LIMIT 1;
	'''

	# connect db and execute sql
	rows = query(sql_query, artist)
	return rows


def show_result_option_3(rows):
	"""Display the result of option 3 to the user.

	Parameters
	----------
	rows: list
		a list of rows to print
    """
	# If no row was found, print statement and return
	if not rows:
		print('Artist not found')
		return
    # print result
    # header
	width = 92
	h = ['Song Title', 'Artist', 'Total Weeks On Board']
	print(
		f'{textwrap.shorten(h[0], 35):40}{textwrap.shorten(h[1], 25):30}{h[2]:20}')
	print('─' * (width))
	# data
	for r in rows:
		print(
			f'{textwrap.shorten(r[0], 35):40}{textwrap.shorten(r[1], 25):30}{r[2]:<20}')
