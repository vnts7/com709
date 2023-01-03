import textwrap
from helpers import *
import matplotlib.pyplot as plt


def option_5():
    """Visualise the songs had been on top 1 and 
      number of weeks those songs being on top in a particular year .
    """
    year = input_year()
    rows = query_option_5(year)
    show_result_option_5(rows, year)


def query_option_5(year):
	"""Perform query of option 5

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
		c.song, count(c.weeks) as weeks
	FROM chart c
	WHERE c.rank = 1 and strftime('%Y', c.date) = ?
	GROUP BY c.song
	'''
	# connect db and execute sql
	rows = query(sql_query, str(year))
	return rows


def show_result_option_5(rows, year):
	"""Visualise the result of option 5 to the user.

	Parameters
	----------
	rows: list
		a list of rows to visualise
    """
	# If no row was found, print statement and return
	if not rows:
		print('No top song on this year')
		return

	# seperate data in list rows to two group lists, with one bar per group
	group_songs = []
	group_weeks = []
	for r in rows:
		group_songs.append(textwrap.shorten(r[0], 20))
		group_weeks.append(r[1])

	# automatically make room for elements in the figures that we create
	plt.rcParams.update({'figure.autolayout': True})
	fig, ax = plt.subplots()  # generate an instance of figure.Figure and axes.Axes
	ax.barh(group_songs, group_weeks)  # plot on top of Axes instance

	# set name and font sizes for the figure title and the axis labels
	fig.suptitle(f'Top songs in {year}', fontsize=20)
	plt.ylabel('Song', fontsize=16)
	plt.xlabel('Number of weeks on top 1', fontsize=16)

	# show the figure
	plt.show()
