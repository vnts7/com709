from helpers import *
import textwrap
def show_artist_with_most_top():
  """Prints the details of the artists with the most top ranked songs 
      and the quantity of top ranked songs.
  """

  #Get the artists having quantity of top ranked song
  #equal to the largest quantity of top ranked song belonging to a artist
  sql_query = '''
    SELECT  
      c.artist,
      count(DISTINCT c.song) as Quantity
    FROM chart c
    WHERE c.rank = 1
    GROUP BY c.Artist
	  HAVING Quantity =  (SELECT  
                          count(DISTINCT c.song) as Quantity
                        FROM chart c
                        WHERE c.rank = 1
                        GROUP BY c.Artist
                        ORDER BY Quantity DESC
                        LIMIT 1);
  '''
  #connect db and execute sql
  cur = connect_db().cursor()
  cur.execute(sql_query)
  rows = cur.fetchall()

  #print the result
  #header
  width = 55
  h = ['Artist', 'Quantity of Top Ranked Songs']
  print(f'{textwrap.shorten(h[0], 25):30}{h[1]:20}')
  print('─' * (width))
  #data
  for r in rows:
    print(f'{textwrap.shorten(r[0], 25):30}{r[1]:<20}')