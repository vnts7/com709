import textwrap
from helpers import *
import matplotlib.pyplot as plt

def visualise_top_songs():
  year = None
  while(year == None):
    try:
      year = int(input('Year to look up (yyyy): '))
    except:
      print("Please enter a valid year")

  sql_query = '''
    SELECT  
      c.song, count(c.rank) as times
    FROM chart c
    WHERE c.rank = 1 and strftime('%Y', c.date) = ?
	  GROUP BY c.song
  '''
  cur = connect_db().cursor()
  
  cur.execute(sql_query, (str(year),))
  rows = cur.fetchall()
  if not rows:
    print('No top song on this year')
    return
  
  group_songs = []
  group_times = []
  for r in rows:
    group_songs.append(textwrap.shorten(r[0], 20))
    group_times.append(r[1])
  
  plt.rcParams.update({'figure.autolayout': True}) #automatically make room for elements in the figures that we create
  fig, ax = plt.subplots() #generate an instance of figure.Figure and axes.Axes
  ax.barh(group_songs, group_times) #plot on top of Axes instance

  #set name and font sizes for the figure title and the axis labels
  fig.suptitle(f'Top songs in {year}', fontsize=20)
  plt.ylabel('Song', fontsize=16)
  plt.xlabel('Times on top 1', fontsize= 16)

  #show the figure
  plt.show()
