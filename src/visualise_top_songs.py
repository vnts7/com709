import textwrap
from helpers import *
import matplotlib.pyplot as plt

def visualise_top_songs():
  """Visualise the songs have been on top 1 and 
    number of weeks those songs being on top a in particular year .
  """
  #Ensure that user enter a valid year 
  year = None
  while(year == None):
    try:
      year = int(input('Year to look up (yyyy): '))
    except:
      print("Please enter a valid year")

  #Get the top songs in the year passed in and 
  #count the number of weeks those songs being on top in passed in year
  sql_query = '''
    SELECT  
      c.song, count(c.weeks) as weeks
    FROM chart c
    WHERE c.rank = 1 and strftime('%Y', c.date) = ?
	  GROUP BY c.song
  '''

  #connect db and execute sql
  cur = connect_db().cursor()
  cur.execute(sql_query, (str(year),))
  rows = cur.fetchall()

  #If no row was found, print statement and return
  if not rows:
    print('No top song on this year')
    return
  
  #seperate data in list rows to two group lists, with one bar per group
  group_songs = []
  group_weeks = []
  for r in rows:
    group_songs.append(textwrap.shorten(r[0], 20))
    group_weeks.append(r[1])
  
  plt.rcParams.update({'figure.autolayout': True}) #automatically make room for elements in the figures that we create
  fig, ax = plt.subplots() #generate an instance of figure.Figure and axes.Axes
  ax.barh(group_songs, group_weeks) #plot on top of Axes instance

  #set name and font sizes for the figure title and the axis labels
  fig.suptitle(f'Top songs in {year}', fontsize=20)
  plt.ylabel('Song', fontsize=16)
  plt.xlabel('Number of week on top 1', fontsize= 16)

  #show the figure
  plt.show()
