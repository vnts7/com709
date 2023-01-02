from show_top_ranked_song import *
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
    Menu(5, '5. Exit', _exit)
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
