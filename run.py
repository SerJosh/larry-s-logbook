from beautifultable import BeautifulTable
from colorama import Fore, Back, Style
# Import textwrap to wrap long text for a better visual
import textwrap

# COLOR TAGS

reset_all = Style.RESET_ALL           # Reset to normal
d_color = Fore.LIGHTYELLOW_EX         # Data color
q_color = Style.BRIGHT + Fore.GREEN   # Question color
h_color = Style.BRIGHT + Fore.BLUE    # Header and Image color

def welcome_message():
    '''
    Display the logo, image and welcome message
    '''
    print(Style.BRIGHT + Fore.BLUE +''' ▄█          ▄████████    ▄████████    ▄████████ ▄██   ▄      ▄████████         
███         ███    ███   ███    ███   ███    ███ ███   ██▄   ███    ███         
███         ███    ███   ███    ███   ███    ███ ███▄▄▄███   ███    █▀          
███         ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███   ███                
███       ▀███████████ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀▀▀   ▄██   ███ ▀███████████         
███         ███    ███ ▀███████████ ▀███████████ ███   ███          ███         
███▌    ▄   ███    ███   ███    ███   ███    ███ ███   ███    ▄█    ███         
█████▄▄██   ███    █▀    ███    ███   ███    ███  ▀█████▀   ▄████████▀          
▀                                                        
 ▄█        ▄██████▄     ▄██████▄  ▀█████████▄   ▄██████▄   ▄██████▄     ▄█   ▄█▄
███       ███    ███   ███    ███   ███    ███ ███    ███ ███    ███   ███ ▄███▀
███       ███    ███   ███    █▀    ███    ███ ███    ███ ███    ███   ███▐██▀  
███       ███    ███  ▄███         ▄███▄▄▄██▀  ███    ███ ███    ███  ▄█████▀   
███       ███    ███ ▀▀███ ████▄  ▀▀███▀▀▀██▄  ███    ███ ███    ███ ▀▀█████▄   
███       ███    ███   ███    ███   ███    ██▄ ███    ███ ███    ███   ███▐██▄  
███▌    ▄ ███    ███   ███    ███   ███    ███ ███    ███ ███    ███   ███ ▀███▄
█████▄▄██  ▀██████▀    ████████▀  ▄█████████▀   ▀██████▀   ▀██████▀    ███   ▀█▀
▀                                                                      ▀        \n''')
    print('''   ____________________________________________________
  |____________________________________________________|
  | __     __   ____   ___ ||  ____    ____     _  __  |
  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
  ||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
  ||_______________________||__________________________|
  | _____________________  ||      __   __  _  __    _ |
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
  ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|
  | _____   _   __  |/      \../      \|  __   __   ___|
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
  |_________ __________\___\____/___/___________ ______|
  |__    _  /    ________     ______           /| _ _ _|
  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
  | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
__|  \/\|/   /(____|/ //                    /  /||~|~|~|__
  |___\_/   /________//   ________         /  / ||_|_|_|
  |___ /   (|________/   |\_______\       /  /| |______|
      /                  \|________)     /  / | |\n''')

    print(reset_all +'Welcome to Larrys LogBook!\n')
    print(textwrap.fill('Hi! Im Larry, your personal budgeting tool! '
                        'I may not be as fancy as those AI thingy majigs you kids use nowadays '
                        'but I get my job done just fine :). Im here to help you with your personal budgeting '
                        'projections, be it for the month, a couple of days for a holiday or '
                        'even the whole year if you up to it. Just give me all the information I need and '
                        'Il do all the magic for you in my trusty logbook, revealing some more insight into your '
                        'budget rather than just how many pennys you have left over ;).', 80))
    print()
    print(textwrap.fill('So the information that my logbook needs to work with are your financial assets, '
                        'incomes, expenses and the timeframe in which you want to budget for. There is additional '
                        'information which is completely optional for you to provide me with but wouldnt it be fun '
                        'to just go all out and discover you financial budgeting story!? '
                        'None the less try out the LogBook and lets see where it takes us.', 80))
    print(Style.BRIGHT + Fore.BLUE +'''\n      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                    `---`\n''')


print(welcome_message())

print(reset_all + textwrap.fill('Ok... So first I am going to ask a few questions before we go on to '
                    'the actual incomes and expenditures, just some information that might '
                    'be useful to me in regards to your budgeting so hear me out :).', 80))
print()

detail_table = BeautifulTable()
detail_table.columns.header = ["", ""]

name = str(input(q_color + "What is your name?: " + reset_all))
detail_table.rows.append([ "NAME", d_color + name])
print(f"Hello {name} :).")

month_or_day = (input(q_color + "\nWould you like to budget for a given month(y/n): " + reset_all))
if month_or_day == "y":
    month = (input(q_color + "Please give me the number of the month eg: 1 is January and so on: " + reset_all))
    if month == "1":
        chosen_month = "January"
        exact_days = 31
        detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "2":
        chosen_month = "Febuary"
        exact_days = 31
        detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "3":
        chosen_month = "March"
        exact_days = 31
        detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "4":
        chosen_month = "April"
        exact_days = 31
        detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "5":
        chosen_month = "May"
        exact_days = 31
        detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "6":
        chosen_month = "June"
        exact_days = 31
        detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "7":
        chosen_month = "July"
        exact_days = 31
        detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "8":
        chosen_month = "August"
        exact_days = 31
        detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "9":
        chosen_month = "September"
        exact_days = 31
        detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "10":
        chosen_month = "October"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "11":
        chosen_month = "November"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
    if month == "12":
        chosen_month = "December"
        exact_days = 31
        table4.rows.append(["MONTH", d_color + chosen_month, ])
if month_or_day == "n":
    days = (input(q_color + "Then how many days do you want to budget for?: " + reset_all))
    table4.rows.append(["Days", d_color + days, ])