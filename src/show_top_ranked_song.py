from helpers import *
from datetime import datetime, timedelta 
import textwrap
def show_top_ranked_song():
  date = None
  while(date == None):
    try:
      date_str = input('Date to look up (yyyy-mm-dd): ')
      date_list = date_str.split('-')
      date = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    except:
      print("Please enter a valid date")

  sql_query = '''
    SELECT  
      c.id, c.date,
      c.song, c.artist, 
      c.last, c.weeks
    FROM chart c
    WHERE c.date = ? and c.rank = 1;
  '''
  cur = connect_db().cursor()
  
  for x in range(7):
    cur.execute(sql_query, (date.strftime("%Y-%m-%d"),))
    rows = cur.fetchall()
    if(rows): break
    date = date - timedelta(days=1)

  if not rows:
    print('No top ranked song on this date')
    return
  #header
  width = 135
  h = ['ID', 'Ranking Date ', 'Song Title', 'Artist','Rank Last Week', 'Weeks On Board']
  print(f'{h[0]:10}{h[1]:20}{textwrap.shorten(h[2], 35):40}{textwrap.shorten(h[3], 25):30}{h[4]:20}{h[5]:20}')
  print('─' * (width))
  for r in rows:
    print(f'{r[0]:<10}{r[1]:20}{textwrap.shorten(r[2], 35):40}{textwrap.shorten(r[3], 25):30}{r[4]:<20}{r[5]:<20}')