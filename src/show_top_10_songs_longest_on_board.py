from helpers import *
import textwrap
def show_top_10_songs_longest_on_board():
  """Prints the details of the 10 songs with the longest number of weeks on the board 
    and number of weeks on the board of these songs.
  """

  sql_query = '''
    SELECT  
      c.song, c.artist, COUNT(c.weeks) as WeeksOnBoard
    FROM chart c
    GROUP BY c.song, c.artist
	  ORDER BY WeeksOnBoard DESC
	  LIMIT 10;
  '''

  #connect db and execute sql
  cur = connect_db().cursor()
  cur.execute(sql_query)
  rows = cur.fetchall()

  #print result
  #header
  width = 92
  h = ['Song Title', 'Artist', 'Total Weeks On Board']
  print(f'{textwrap.shorten(h[0], 35):40}{textwrap.shorten(h[1], 25):30}{h[2]:20}')
  print('─' * (width))
  #data
  for r in rows:
    print(f'{textwrap.shorten(r[0], 35):40}{textwrap.shorten(r[1], 25):30}{r[2]:<20}')