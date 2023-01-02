from show_top_ranked_song import *
from show_artist_with_most_top import *
from show_top_10_songs_longest_on_board import *
from helpers import *


class Menu:
    def __init__(self, command, text, fn):
        self.command = command
        self.text = text
        self.fn = fn


def _exit():
    close_db()
    quit()


menus = [
    Menu(1, '1. Retrieve the details for the top ranked song for a particular day', show_top_ranked_song),
    Menu(2, '2. Retrieve the details of the artist with the most top ranked song', show_artist_with_most_top),
    Menu(3, '3. Retrieve the details of the 10 songs with the longest number of weeks on the boards', show_top_10_songs_longest_on_board),
    Menu(4, '4. Retrieve the song that has moved the most in ranking on the board', show_artist_with_most_top),
    Menu(5, '5. Visualise the top songs', show_artist_with_most_top),
    Menu(6, '6. Exit', _exit)
]
dic_menu = {}
for m in menus:
    dic_menu[m.command] = m
while (True):
    for m in menus:
        print(m.text)
    command = int(input('Select option: '))
    if dic_menu[command]:
        dic_menu[command].fn()
        input('Press enter to return to main menu...')

# close_db()
