from beautifultable import BeautifulTable
from colorama import Fore, Back, Style
# Import textwrap to wrap long text for a better visual
import textwrap

# COLOR TAGS

reset_all = Style.RESET_ALL           # Reset to normal
d_color = Fore.LIGHTYELLOW_EX         # Data color
q_color = Style.BRIGHT + Fore.GREEN   # Question color
h_color = Style.BRIGHT + Fore.BLUE    # Header and Image color
e_color = Back.RED                    # Error color

# OUTPUT FUNCTIONS

def welcome_message():
    '''
    Display the logo, image and welcome message
    '''
    print(h_color + ''' ▄█          ▄████████    ▄████████    ▄████████ ▄██   ▄      ▄████████         
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

    print(reset_all + 'Welcome to Larrys LogBook!\n')
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
                        'To simply put it, you are dealing with a simple formula of financial assets + income - expenses. '
                        'Use that formula as you wish in any way you want, but walking it with me may give you more insightful results. '
                        'None the less try out the LogBook and lets see where it takes us.', 80))
    print(h_color + '''\n      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                    `---`\n''')


def name_question():
    '''
    Display, append and validate name question
    '''
    global detail_table
    global name
    
    detail_table = BeautifulTable()
    detail_table.columns.header = ["", ""]

    name = str(input(q_color + "What is your name?: " + reset_all))
    detail_table.rows.append([ "NAME", d_color + name])
    try:
        # Validate that name contains the right amount of characters
        if len(name) <= 0:
            raise ValueError("The name can't be left empty.")
        if len(name) >= 10:
            raise ValueError("The name has too many characters.")
    except ValueError as e:
        print(e_color + f'Invalid name. {e} Please provide your name again.' +
              reset_all)
        return name_question()
 

def month_question():
    '''
    Display, append and validate month question
    '''
    global detail_table
    global chosen_month
    global exact_days 
    month_or_day = str(input(q_color + "\nWould you like to budget for a given month(y/n): " + reset_all))
    try:
        # Validate that the input given is "y" or "n"
        if month_or_day == "y" or month_or_day == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
              reset_all)
        return month_question() 
    if month_or_day=='y':
	    month = (input(q_color + "Please give me the number of the month eg: 1 is January and so on: " + reset_all))
	    if month=='1':chosen_month='January';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='2':chosen_month='Febuary';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='3':chosen_month='March';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='4':chosen_month='April';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='5':chosen_month='May';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='6':chosen_month='June';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='7':chosen_month='July';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='8':chosen_month='August';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='9':chosen_month='September';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='10':chosen_month='October';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='11':chosen_month='November';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	    if month=='12':chosen_month='December';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month_or_day == "n":
        days = (input(q_color + "Then how many days do you want to budget for?: " + reset_all))
        detail_table.rows.append(["Days", d_color + days, ])


def currency_question():
    '''
    Display, append and validate currency question
    '''
    currency = (input(q_color + "\nWhat currency would you like to use?(Only one character/symbol neccessary): " + reset_all))
    detail_table.rows.append(["CURRENCY", d_color + currency])
    try:
        # Validate that the currency has the rigght amount of characters
        if len(currency) >= 2:
            raise ValueError("You can only use one symbol/character.")
    except ValueError as e:
        print(e_color + f'Invalid currency. {e} Please try again.' +
              reset_all)
        return currency_question()


def goal_question():
    goal_question =  (input(q_color + "\nDo you want to set a budget goal? ie: a desired amount you want after all expenses(y/n): " + reset_all))
    if goal_question == "y":
        goal = (input((q_color + "Enter the amount of your goal: " + reset_all)))
        detail_table.rows.append(["Goal", d_color + goal ])


# This is the main function, this is where everything runs---->
# And these are my global variables-->
name = "x"
detail_table = "y"
exact_days = "z"
days = "x"
# And these are my global variables-->

def main():
    welcome_message()
    print(reset_all + textwrap.fill('Ok... So first I am going to ask a few questions before we go on to '
                    'the actual incomes and expenditures, just some information that might '
                    'be useful to me in regards to your budgeting so hear me out :).', 80))
    print()
    name_question()
    month_question()
    currency_question()
    goal_question()

main()


# This is the main function, this is where everything runs---->


goal_question =  (input(q_color + "\nDo you want to set a budget goal? ie: a desired amount you want after all expenses(y/n): " + reset_all))
if goal_question == "y":
    goal = (input((q_color + "Enter the amount of your goal: " + reset_all)))
    detail_table.rows.append(["Goal", d_color + goal])

print(reset_all + "\nSo these are the details you have given to me so far...\n")
print(detail_table)
(input(q_color + "\nAre you happy with the details or would you like to start over?(y/n): "))

asset_table = BeautifulTable()
asset_table.columns.header = ["asset", "amount", "total"]
add_asset = []

print()
print(reset_all + textwrap.fill('\nNow lets get cracking with the financial assets :). '
                        'By financial assets I mean money that you already have on you that you are willing '
                        'to use in your budget, so if its a pension, a deeply imbedded life savings account '
                        'or anything of that sort, maybe just leave that out ;). What I mean is money in your current '
                        'account, or an amount in it you are willing to give in your budget, same goes with revolut '
                        'or other institutions like that. Cash on hand may be another one you want to put in here '
                        'In the end its all up to you to decide what you want in here, but try leave nothing out '
                        'which may constitute as a financial asset as the more detail you put in only helps you more.', 80))

def asset_calculate():
    '''
   Takes in data of the financial assets plugged in
    '''
    asset = (input(q_color + "\nEnter The name of your financial asset: " + reset_all))
    amount = float(input(q_color + "Enter the amount of that financial asset: " + reset_all))
    add_asset.append(amount)
    total = sum(add_asset)
    asset_table.rows.append([d_color + asset, amount, total])

    print(asset_table)
    continue1 = (input(q_color + "Do you want to add another financial asset? y/n: " + reset_all))
    if continue1 =="y":
        asset_calculate()
        print(asset_table)
    if continue1 == "n":
        return asset_table  

print(asset_calculate())

income_table = BeautifulTable()
income_table.columns.header = ["income", "amount",  "total"]
add_income = []

def income_calculate():
    '''
   Takes in data of the incomes plugged in
    '''
    income = (input(q_color + "Enter The name of your income: " + reset_all))
    amount = float(input(q_color + "Enter your amount of that income: " + reset_all))
    add_income.append(amount)
    total = sum(add_income)
    income_table.rows.append([d_color + income, amount,  total])

    print(income_table)
    continue1 = (input(q_color + "Do you want to add another income? y/n: " + reset_all))
    if continue1 =="y":
        income_calculate()
        print(income_table)
    if continue1 == "n":
        return income_table  

print(income_calculate())

expense_table = BeautifulTable()
expense_table.columns.header = ["expense", "amount", "total"]
add_expense = []

def expense_calculate():
    expense = (input(q_color + "Enter The name of your expense: " + reset_all))
    amount_exp = float(input(q_color + "Enter your amount of that expense: " + reset_all))
    add_expense.append(amount_exp)
    total = sum(add_expense)
    expense_table.rows.append([d_color + expense, amount_exp, total])

    print(expense_table)
    continue1 = (input(q_color + "Do you want to add another expense? y/n: " + reset_all))
    if continue1 =="y":
        expense_calculate()
        print(expense_table)
    if continue1 == "n":
        print("ok") 

print(expense_calculate())

inco_total = sum(add_income)
expe_total = sum(add_expense)
asset_total = sum(add_asset)

surplus = asset_total + inco_total - expe_total

print(asset_table)
print()
print(income_table)
print()
print(expense_table)
print()
print(" Your financial assets are " + str(asset_total))
print(" Your total income is " + str(inco_total))
print(" Your total expense is " + str(expe_total))
print("your gross amount will be " + str(surplus))