from helpers import *
import textwrap
def show_artist_with_most_top():
  sql_query = '''
    SELECT  
      c.artist,
      count(DISTINCT c.song) as Quantity
    FROM chart c
    WHERE c.rank = 1
    GROUP BY c.Artist
    ORDER BY Quantity DESC
    LIMIT 1;
  '''
  cur = connect_db().cursor()
  
  cur.execute(sql_query)
  rows = cur.fetchall()
  #header
  width = 55
  h = ['Artist', 'Quantity of Top Songs']
  print(f'{textwrap.shorten(h[0], 25):30}{h[1]:20}')
  print('─' * (width))
  for r in rows:
    print(f'{textwrap.shorten(r[0], 25):30}{r[1]:<20}')