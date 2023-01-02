from helpers import *
import textwrap
def show_top_ranked_song():
  date = input("Date to look up (yyyy-mm-dd): ")
  sql_query = '''
    SELECT  
      c.id as SongID, c.song as SongTitle, c.artist as Artist, 
      c.last as LastWeek, c.weeks as WeeksOnBoard 
    FROM chart c
    WHERE c.date = ? and c.rank = 1;
  '''
  cur = connect_db().cursor()
  
  cur.execute(sql_query, (date,))
  rows = cur.fetchall()
  if not rows:
    print('No top ranked song on this date')
    return
  #header
  width = 120
  h = ['Song ID', 'Song Title', 'Artist','Last For (Week)', 'Weeks On Board']
  print(f'{h[0]:10}{textwrap.shorten(h[1], 35):40}{textwrap.shorten(h[2], 25):30}{h[3]:20}{h[4]:20}')
  print('─' * (width))
  for r in rows:
    print(f'{r[0]:<10}{textwrap.shorten(r[1], 35):40}{textwrap.shorten(r[2], 25):30}{r[3]:<20}{r[4]:<20}')