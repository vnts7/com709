from option_1 import *
from option_2 import *
from option_3 import *
from option_4 import *
from option_5 import *
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
    Menu(1, '1. Retrieve the details of the top ranked song for a particular day', option_1),
    Menu(2, '2. Retrieve the details of the artists having top ranked songs in a particular year', option_2),
    Menu(3, '3. Retrieve the details of the song with the longest number of weeks on the board of a particular artist', option_3),
    Menu(4, '4. Retrieve the song that has moved the most in ranking on the board in a particular year', option_4),
    Menu(5, '5. Visualise the top songs in a particular year', option_5),
    Menu(6, '6. Exit', _exit)
]

#Connect to the db
connect_db("charts.db")

dic_menu = {}
for m in menus:
    dic_menu[m.command] = m

while (True):
    for m in menus:
        print(m.text)
    command = None
    while(command == None or command > 6 or command < 1):
        try:
            command = int(input('Select option: '))
        except:
            print('Please enter a valid number')
    if dic_menu[command]:
        dic_menu[command].fn()
        input('Press enter to return to main menu...')
