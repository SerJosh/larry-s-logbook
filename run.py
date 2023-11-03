from beautifultable import BeautifulTable
from colorama import Fore, Back, Style
# Import textwrap to wrap long text for a better visual
import textwrap
import os

# COLOR TAGS

reset_all = Style.RESET_ALL           # Reset to normal
d_color = Fore.LIGHTYELLOW_EX         # Data color
q_color = Style.BRIGHT + Fore.GREEN   # Question color
h_color = Style.BRIGHT + Fore.BLUE    # Header and Image color
e_color = Back.RED                    # Error color
#!!class
# OUTPUT FUNCTIONS


def clear_terminal():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_message():
    '''
    Display the logo, image and welcome message
    '''
    print(h_color + ''' _                           _              ___           _   
| |   __ _ _ _ _ _ _  _ ___ | |   ___  __ _| _ ) ___  ___| |__
| |__/ _` | '_| '_| || (_-< | |__/ _ \/ _` | _ \/ _ \/ _ \ / /
|____\__,_|_| |_|  \_, /__/ |____\___/\__, |___/\___/\___/_\_\
                   |__/               |___/                   ''')

    
    print(h_color + '''\n      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                    `---`\n''')

    print(reset_all + 'Welcome to Larrys LogBook!\n')
    name_question()
    clear_terminal()
    print(textwrap.fill(f'Hi {name}! Im Larry, your personal budgeting tool! '
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



def name_question():
    '''
    Display, append and validate name question
    '''
    global detail_table
    global name
    
    detail_table = BeautifulTable()
    detail_table.columns.header = ["", ""]

    name = str(input(q_color + "What is your name?: " + reset_all))
    # detail_table.rows.append([ "NAME", d_color + name])
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


def first_question_confirmation():
    '''
    Display and validate name question
    '''
    question_confirm = str(input(q_color + "Would you like to go through these additional questions? (y/n): " + reset_all))

    # Direct to functions on choice of "y" or "n"  
    if question_confirm == 'y':
        clear_terminal()
        return first_questions()
    if question_confirm == "n":
        clear_terminal()
        return budget_questions()
 
# First Questions Functions

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
    if month_or_day =='y':
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
        # Validate that month input contains the corrrect details
        if month <= 0:
            raise ValueError("This cannot be 0 or under silly xD.")
        if month >= 13:
            raise ValueError("Please choose the months between 1 and 12.")
        # if len(month) == 0:
        #     raise ValueError("This cannot be left empty.")
    except ValueError as e:
        print(e_color + f'Invalid input. {e} Please try again.' +
              reset_all)
        return choose_month()

    # Recieves data from which month number was chosen
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
	#!!!!!!
	
def choose_day():
    '''
    Display, append and validate choose day question
    '''
    global exact_days
    exact_days = (input(q_color + "Then how many days do you want to budget for?: " + reset_all))
    try:
        # Validate that month input contains the corrrect details
        if len(exact_days) <= 0:
            raise ValueError("This cannot be left empty.")
        if exact_days == "0":
            raise ValueError("Lets not go there.. atleast put 1 xD.")
    except ValueError as e:
        print(e_color + f'Invalid input. {e} Please try again.' +
              reset_all)
        return choose_day()

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
        if len(currency) <= 0:
            raise ValueError("This cannot be left empty.") 
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
    clear_terminal()
    print(reset_all + "\nSo these are the details you have given to me so far...\n")
    print(detail_table)
    summary_question = (input(q_color + "\nThese are the details you supplied, would you like to start over?(y/n): " + reset_all))
    if summary_question == "y":
        return reset_table()
    if summary_question == "n":
        return budget_questions()


def reset_table():
    '''
    Resets detail_table and restarts the first questions function
    '''
    # detail_table = None
    # return first_questions()
    global detail_table
    detail_table = None
    detail_table = BeautifulTable()
    detail_table.columns.header = ["", ""]
    clear_terminal()
    return first_questions()

# Financial Asset Functions

def financial_asset_option():
    '''
    Gives option of choosing if you want to add financial assets
    '''
    print('\nNow lets get cracking with the financial assets :). ')
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
        print(reset_all + textwrap.fill(
                        'By financial assets I mean money that you already have on you that you are willing '
                        'to use in your budget, so if its a pension, a deeply imbedded life savings account '
                        'or anything of that sort, maybe just leave that out ;). What I mean is money in your current '
                        'account, or an amount in it you are willing to give in your budget, same goes with revolut '
                        'or other institutions like that. Cash on hand may be another one you want to put in here. '
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
    restart_asset = (input(q_color + "These are the financial asset details your provided, would you like to start over?(y/n): " + reset_all))
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
    print('\nNow lets get cracking with the Income :).')
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
        print(reset_all + textwrap.fill(' '
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
    income = (input(q_color + "\nEnter The name of your income: " + reset_all))
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
    another_income = (input(q_color + "Do you want to add another income? y/n: " + reset_all))
    if another_income =="y":
        income_calculate()
        print(income_table)
    if another_income == "n":
        print(income_table)
        income_confirmation()


def income_confirmation():
    '''
   Confirms if user wants to redo the income
    '''
    restart_income = (input(q_color + "These are the income details you have provided, would you like to start over?(y/n): " + reset_all))
    try:
    # Validate that the input given is "y" or "n"
        if restart_income == "y" or restart_income == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
            reset_all)
        return income_confirmation()

    if restart_income =="y":
        reset_income_table()  
    if restart_income == "n":
        print("ok")


def reset_income_table():
    '''
   Resets income table and starts income questions again
    '''
    global income_table
    global add_income
    income_table = None
    income_table = BeautifulTable()
    income_table.columns.header = ["income", "amount",  "total"]
    add_income = []
    return income_calculate()  

# Expense Functions

def expense_option():
    '''
    Gives option of choosing if you want to add expenses
    '''
    print('\nNow lets get cracking with the expenses :).')
    expense_choice = (input(q_color + "\nWould you like to add Expenses?(y/n): " + reset_all))
    try:
        # Validate that the input given is "y" or "n"
        if expense_choice == "y" or expense_choice == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
              reset_all)
        return expense_option()

    if expense_choice=='y':
        return expense_info_question()


def expense_info_question():
    '''
    Gives option of choosing if you want to hear more about expenses
    '''
    expense_info = (input(q_color + "\nDo you want to hear more about expenses?(y/n): " + reset_all))
    try:
    # Validate that the input given is "y" or "n"
        if expense_info == "y" or expense_info == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
            reset_all)
        return expense_info_question()

    if expense_info=='y':
        print(reset_all + textwrap.fill(' '
                        'By financial assets I mean money that you already have on you that you are willing '
                        'to use in your budget, so if its a pension, a deeply imbedded life savings account '
                        'or anything of that sort, maybe just leave that out ;). What I mean is money in your current '
                        'account, or an amount in it you are willing to give in your budget, same goes with revolut '
                        'or other institutions like that. Cash on hand may be another one you want to put in here '
                        'In the end its all up to you to decide what you want in here, but try leave nothing out '
                        'which may constitute as a financial asset as the more detail you put in only helps you more.', 80))
        return expense_calculate()
    if expense_info == "n":
        return expense_calculate()


def expense_calculate():
    '''
   Takes in data of the expenses plugged in
    '''
    expense = (input(q_color + "\nEnter The name of your expense: " + reset_all))
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
    another_expense = (input(q_color + "Do you want to add another expense? y/n: " + reset_all))
    if another_expense =="y":
        expense_calculate()
        print(expense_table)
    if another_expense == "n":
        print(expense_table)
        expense_confirmation() 


def expense_confirmation():
    '''
   Confirms if user wants to redo the expense
    '''
    restart_expense = (input(q_color + "These are the expense details you have provided, would you like to start over?(y/n): " + reset_all))
    try:
    # Validate that the input given is "y" or "n"
        if restart_expense == "y" or restart_expense == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(e_color + f'Invalid answer. {e} Please try again.' +
            reset_all)
        return expense_confirmation()

    if restart_expense =="y":
        reset_expense_table()  
    if restart_expense == "n":
        print("ok")


def reset_expense_table():
    '''
   Resets expense table and starts income questions again
    '''
    global expense_table
    global add_expense
    expense_table = None
    expense_table = BeautifulTable()
    expense_table.columns.header = ["expense", "amount", "total"]
    add_expense = []
    return expense_calculate()


def results_page():
    '''
   Displays all calculated results and tables from information provided
    '''
    inco_total = sum(add_income)
    expe_total = sum(add_expense)
    asset_total = sum(add_asset)
    calc_days = (int(f"{exact_days}"))

    if goal_set_question == "y":
        goal_result = (float(f"{goal}"))

    # Calculations
    surplus = asset_total + inco_total - expe_total
    day_result = surplus / calc_days

    print(h_color + f'Budget Summary of {name}')
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
    print(h_color +"Your financial assets are " + reset_all + str(asset_total))
    print()
    print(h_color +"Your total income is " + reset_all + str(inco_total))
    print()
    print(h_color +"Your total expense is " + reset_all + str(expe_total))
    print()
    print(h_color +"Your gross amount will be " + reset_all + str(surplus))
    print()
    print(h_color + f"you will be able to spend " + reset_all +  f"{day_result} per day")

    if goal_set_question == "y":
        target_goal = surplus - goal_result 
        if target_goal >= 0:
            print(h_color + "You are over your goal by: " + reset_all + str(target_goal) + "\n")
        else:
            print(h_color + "You are under your goal by: " + reset_all + str(target_goal) + "\n")


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
    '''
   Condenses all of the question functions into one functon
    '''
    # name_question()
    print(reset_all + textwrap.fill('Ok... So first I am going to ask a few questions before we go on to '
                    'the actual incomes and expenditures, just some information that might '
                    'be useful to me in regards to your budgeting so hear me out :).', 80))
    month_question()
    currency_question()
    goal_question()
    question_summary()

def budget_questions():
    clear_terminal()
    financial_asset_option()
    clear_terminal()
    income_option()
    clear_terminal()
    expense_option()
    clear_terminal()
    results_page()
# ----condensed functions------->

def main():
    '''
   Takes in all neccessary functions and initiates the functions 
    '''
    welcome_message()
    first_question_confirmation()
    # print()
    first_questions()
    # print()
    budget_questions()
    


main()

# This is the main function, this is where everything runs---->
