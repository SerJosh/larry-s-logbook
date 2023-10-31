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

# First Questions Functions

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
    Display, validate and direct (to relevant next question) month question.
    '''
    global detail_table
    global chosen_month
    global exact_days 
    month_or_day = (input(q_color + "\nWould you like to budget for a given month(y/n): " + reset_all))
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

    # Direct to functions on choice of "y" or "n"  
    if month_or_day=='y':
        return choose_month()
    if month_or_day == "n":
        return choose_day()


def choose_month():
    '''
    Display, append and validate choose month question
    '''
    global exact_days
    month = int(input(q_color + "Please give me the number of the month eg: 1 is January and so on: " + reset_all))
    try:
        # Validate that name contains the right amount of characters
        if month <= 0:
            raise ValueError("This cannot be left empty.")
        if month >= 13:
            raise ValueError("Please choose the months between 1 and 12.")
    except ValueError as e:
        print(e_color + f'Invalid input. {e} Please try again.' +
              reset_all)
        return choose_month()
    if month== 1 :chosen_month='January';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 2 :chosen_month='Febuary';exact_days=28;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 3 :chosen_month='March';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 4 :chosen_month='April';exact_days=30;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 5 :chosen_month='May';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 6 :chosen_month='June';exact_days=30;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 7 :chosen_month='July';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 8 :chosen_month='August';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 9 :chosen_month='September';exact_days=30;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 10 :chosen_month='October';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 11 :chosen_month='November';exact_days=30;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
    if month== 12 :chosen_month='December';exact_days=31;detail_table.rows.append(["MONTH", d_color + chosen_month, ])
	
	
def choose_day():
    '''
    Display, append and validate choose day question
    '''
    global exact_days
    exact_days = (input(q_color + "Then how many days do you want to budget for?: " + reset_all))
    detail_table.rows.append(["Days", d_color + exact_days, ])


def currency_question():
    '''
    Display, append and validate currency question
    '''
    currency = (input(q_color + "\nWhat currency would you like to use?(Only one character/symbol neccessary): " + reset_all))
    try:
        # Validate that the currency has the right amount of characters
        if len(currency) >= 2:
            raise ValueError("You can only use one symbol/character.")
    except ValueError as e:
        print(e_color + f'Invalid currency. {e} Please try again.' +
              reset_all)
        return currency_question()
    detail_table.rows.append(["CURRENCY", d_color + currency])


def goal_question():
    '''
    Display, append and validate goal question
    '''
    global goal
    global goal_set_question
    goal_set_question =  (input(q_color + "\nDo you want to set a budget goal? ie: a desired amount you want after all expenses(y/n): " + reset_all))
    try:
        # Validate that the input given is "y" or "n"
        if goal_set_question == "y" or goal_set_question == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
              reset_all)
        return goal_question()
        
    if goal_set_question == "y":
        goal = (input((q_color + "Enter the amount of your goal: " + reset_all)))
        detail_table.rows.append(["Goal", d_color + goal ])


def question_summary():
    '''
    Display all results from questions asked and giving the option to start over
    '''
    print(reset_all + "\nSo these are the details you have given to me so far...\n")
    print(detail_table)
    summary_question = (input(q_color + "\nThese are the details you supplied, would you like to start over?(y/n): " + reset_all))
    if summary_question == "y":
        return reset_table()


def reset_table():
    '''
    Resets detail_table and restarts the first questions function
    '''
    detail_table = None
    return first_questions()

# Financial Asset Functions

def financial_asset_option():
    '''
    Gives option of choosing if you want to add financial assets
    '''
    asset_choice = (input(q_color + "\nWould you like to add financial assets?(y/n): " + reset_all))
    try:
        # Validate that the input given is "y" or "n"
        if asset_choice == "y" or asset_choice == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
              reset_all)
        return financial_asset_option()

    if asset_choice=='y':
        return financial_asset_info_question()


def financial_asset_info_question():
    '''
    Gives option of choosing if you want to hear more about financial assets
    '''
    asset_info = (input(q_color + "\nDo you want to hear more about financial assets?(y/n): " + reset_all))
    try:
    # Validate that the input given is "y" or "n"
        if asset_info == "y" or asset_info == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
            reset_all)
        return financial_asset_info_question()

    if asset_info=='y':
        print(reset_all + textwrap.fill('\nNow lets get cracking with the financial assets :). '
                        'By financial assets I mean money that you already have on you that you are willing '
                        'to use in your budget, so if its a pension, a deeply imbedded life savings account '
                        'or anything of that sort, maybe just leave that out ;). What I mean is money in your current '
                        'account, or an amount in it you are willing to give in your budget, same goes with revolut '
                        'or other institutions like that. Cash on hand may be another one you want to put in here '
                        'In the end its all up to you to decide what you want in here, but try leave nothing out '
                        'which may constitute as a financial asset as the more detail you put in only helps you more.', 80))
        return asset_calculate()
    if asset_info == "n":
        return asset_calculate()


def asset_calculate():
    '''
   Takes in data of the financial assets plugged in
    '''
    asset = (input(q_color + "\nEnter The name of your financial asset: " + reset_all))
    try:
        # Validate that the asset name contains the right amount of characters
        if len(asset) <= 0:
            raise ValueError("The asset name can't be left empty.")
        if len(asset) >= 20:
            raise ValueError("The asset name has too many characters.")
    except ValueError as e:
        print(e_color + f'Invalid name. {e} Please provide your asset name again.' +
              reset_all)
        return asset_calculate()

    amount = float(input(q_color + "Enter the amount of that financial asset: " + reset_all))
    add_asset.append(amount)
    total = sum(add_asset)
    asset_table.rows.append([d_color + asset, amount, total])

    print(asset_table)
    another_asset = (input(q_color + "Do you want to add another financial asset? y/n: " + reset_all))
    if another_asset =="y":
        asset_calculate()
        print(asset_table)
    if another_asset == "n":
        print(asset_table)
        asset_confirmation()


def asset_confirmation():
    '''
   Confirms if user wants to redo the financial assets
    '''
    restart_asset = (input(q_color + "Are you happy with the details or would you like to start over?(y/n): " + reset_all))
    try:
    # Validate that the input given is "y" or "n"
        if restart_asset == "y" or restart_asset == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
            reset_all)
        return asset_confirmation()
    if restart_asset =="y":
        reset_asset_table()  
    if restart_asset == "n":
        print("ok")


def reset_asset_table():
    '''
   Resets asset table and starts assets questions again
    '''
    global asset_table
    global add_asset
    asset_table = None
    asset_table = BeautifulTable()
    asset_table.columns.header = ["asset", "amount", "total"]
    add_asset = []
    return asset_calculate() 

# Income Functions

def income_option():
    '''
    Gives option of choosing if you want to add incomes
    '''
    income_choice = (input(q_color + "\nWould you like to add Income?(y/n): " + reset_all))
    try:
        # Validate that the input given is "y" or "n"
        if income_choice == "y" or income_choice == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
              reset_all)
        return income_option()

    if income_choice=='y':
        return income_info_question()


def income_info_question():
    '''
    Gives option of choosing if you want to hear more about income
    '''
    income_info = (input(q_color + "\nDo you want to hear more about income?(y/n): " + reset_all))
    try:
    # Validate that the input given is "y" or "n"
        if income_info == "y" or income_info == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
            reset_all)
        return income_info_question()

    if income_info=='y':
        print(reset_all + textwrap.fill('\nNow lets get cracking with the financial assets :). '
                        'By financial assets I mean money that you already have on you that you are willing '
                        'to use in your budget, so if its a pension, a deeply imbedded life savings account '
                        'or anything of that sort, maybe just leave that out ;). What I mean is money in your current '
                        'account, or an amount in it you are willing to give in your budget, same goes with revolut '
                        'or other institutions like that. Cash on hand may be another one you want to put in here '
                        'In the end its all up to you to decide what you want in here, but try leave nothing out '
                        'which may constitute as a financial asset as the more detail you put in only helps you more.', 80))
        return income_calculate()
    if income_info == "n":
        return income_calculate()

def income_calculate():
    '''
   Takes in data of the incomes plugged in
    '''
    income = (input(q_color + "Enter The name of your income: " + reset_all))
    try:
        # Validate that the income name contains the right amount of characters
        if len(income) <= 0:
            raise ValueError("The income name can't be left empty.")
        if len(income) >= 20:
            raise ValueError("The income name has too many characters.")
    except ValueError as e:
        print(e_color + f'Invalid name. {e} Please provide your income name again.' +
              reset_all)
        return income_calculate()

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

# Expense Functions

def expense_calculate():
    expense = (input(q_color + "Enter The name of your expense: " + reset_all))
    try:
        # Validate that the expense name contains the right amount of characters
        if len(expense) <= 0:
            raise ValueError("The income name can't be left empty.")
        if len(expense) >= 20:
            raise ValueError("The income name has too many characters.")
    except ValueError as e:
        print(e_color + f'Invalid name. {e} Please provide your income name again.' +
              reset_all)
        return expense_calculate()

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


def results_page():
    inco_total = sum(add_income)
    expe_total = sum(add_expense)
    asset_total = sum(add_asset)
    calc_days = (int(f"{exact_days}"))

    if goal_set_question == "y":
        goal_result = (float(f"{goal}"))

    # Calculations
    surplus = asset_total + inco_total - expe_total
    day_result = surplus / calc_days

    print(f'Budget Summary of {name}')
    print()
    print(h_color + "Financial Assets" + reset_all)
    print(asset_table)
    print()
    print(h_color + "Income" + reset_all)
    print(income_table)
    print()
    print(h_color + "Expenses" + reset_all)
    print(expense_table)
    print()
    print(" Your financial assets are " + str(asset_total))
    print(" Your total income is " + str(inco_total))
    print(" Your total expense is " + str(expe_total))
    print("your gross amount will be " + str(surplus))
    print(f"you will be able to spend {day_result} per day")

    if goal_set_question == "y":
        target_goal = surplus - goal_result 
        if target_goal >= 0:
            print("You are over your goal by: " + str(target_goal) + "\n")
        else:
            print("You are under your goal by: " + str(target_goal) + " short \n")


# This is the main function, this is where everything runs---->

# And these are my global variables-->
name = "x"
detail_table = "y"
exact_days = "z"
days = "x"
goal_set_question = "a"

asset_table = BeautifulTable()
asset_table.columns.header = ["asset", "amount", "total"]
add_asset = []

income_table = BeautifulTable()
income_table.columns.header = ["income", "amount",  "total"]
add_income = []

expense_table = BeautifulTable()
expense_table.columns.header = ["expense", "amount", "total"]
add_expense = []
# And these are my global variables-->

#----condensed functions--------->
def first_questions():
    name_question()
    month_question()
    currency_question()
    goal_question()
    question_summary()
# ----condensed functions------->

def main():
    welcome_message()
    print(reset_all + textwrap.fill('Ok... So first I am going to ask a few questions before we go on to '
                    'the actual incomes and expenditures, just some information that might '
                    'be useful to me in regards to your budgeting so hear me out :).', 80))
    print()
    first_questions()
    print()
    financial_asset_option()
    income_calculate()
    expense_calculate()
    results_page()


main()

# This is the main function, this is where everything runs---->
