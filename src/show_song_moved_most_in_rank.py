from helpers import *
import textwrap
def show_song_moved_most_in_rank():
  """Prints the songs that has moved the most in ranking on the board.
  """

  #Get the songs that have ranking range
  #equal to the most moved song in ranking on the board
  sql_query = '''
    SELECT  
      c.song, c.artist, (max(c.peak) - min(c.peak)) as RangeRank
    FROM chart c
    GROUP BY c.song, c.artist
	  HAVING (max(c.peak) - min(c.peak)) =    (SELECT  
                                              (max(c.peak) - min(c.peak)) as RangeRank
                                            FROM chart c
                                            GROUP BY c.song, c.artist
                                            ORDER BY RangeRank DESC
                                            LIMIT 1)
  '''
  #connect db and execute sql
  cur = connect_db().cursor()
  cur.execute(sql_query)
  rows = cur.fetchall()

  #print result
  #header
  width = 85
  h = ['Song Title', 'Artist', 'Ranking Range']
  print(f'{textwrap.shorten(h[0], 35):40}{textwrap.shorten(h[1], 25):30}{h[2]:20}')
  print('─' * (width))
  #data
  for r in rows:
    print(f'{textwrap.shorten(r[0], 35):40}{textwrap.shorten(r[1], 25):30}{r[2]:<20}')