from helpers import *
import textwrap
def show_song_moved_most_in_rank():
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
  cur = connect_db().cursor()
  
  cur.execute(sql_query)
  rows = cur.fetchall()
  #header
  width = 85
  h = ['Song Title', 'Artist', 'Ranking Rank']
  print(f'{textwrap.shorten(h[0], 35):40}{textwrap.shorten(h[1], 25):30}{h[2]:20}')
  print('─' * (width))
  for r in rows:
    print(f'{textwrap.shorten(r[0], 35):40}{textwrap.shorten(r[1], 25):30}{r[2]:<20}')