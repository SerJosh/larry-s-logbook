from beautifultable import BeautifulTable
from colorama import Fore, Back, Style
# Import textwrap to wrap long text for a better visual
import textwrap
# Import os to let clear_terminal clear the terminal screen
import os

# COLOR TAGS
# !! This can be made into classes !!
# reset_all = Style.RESET_ALL           # Reset to normal
# d_color =          # Data color
# q_color =    # Question color
#     # Header and Image color
# e_color =                     # Error color


class Color:
    blue = Style.BRIGHT + Fore.BLUE
    yellow = Fore.LIGHTYELLOW_EX
    green = Style.BRIGHT + Fore.GREEN
    red = Back.RED
    reset = Style.RESET_ALL


color = Color()


def clear_terminal():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")

# OUTPUT FUNCTIONS


def welcome_message():
    '''
    Display the logo, image and welcome message
    '''
    print(color.blue + '''dP                                                               
88                                                               
88        .d8888b. 88d888b. 88d888b. dP    dP .d8888b.           
88        88'  `88 88'  `88 88'  `88 88    88 Y8ooooo.           
88        88.  .88 88       88       88.  .88       88           
88888888P `88888P8 dP       dP       `8888P88 `88888P'           
                                          .88                    
                                      d8888P                     
dP                           888888ba                    dP      
88                           88    `8b                   88      
88        .d8888b. .d8888b. a88aaaa8P' .d8888b. .d8888b. 88  .dP 
88        88'  `88 88'  `88  88   `8b. 88'  `88 88'  `88 88888"  
88        88.  .88 88.  .88  88    .88 88.  .88 88.  .88 88  `8b.
88888888P `88888P' `8888P88  88888888P `88888P' `88888P' dP   `YP
                        .88                                      
                    d8888P                                       ''')
#     print(h_color + '''\n      __...--~~~~~-._   _.-~~~~~--...__
#     //               `V'               \\ 
#    //                 |                 \\ 
#   //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
#  //__.....----~~~~._\ | /_.~~~~----.....__\\
# ====================\\|//====================
#                     `---`\n''')
    name_question()
    clear_terminal()
    print(color.reset + 'Welcome to Larrys LogBook!\n')
    print(textwrap.fill(f'Hi {name}! Im Larry, your personal budgeting tool! '
                        'I may not be as fancy as those AI thingy majigs you '
                        'kids use nowadays but I get my job done just fine :)'
                        '. Im here to help you with your personal budgeting '
                        'projections. Be it for the month, a couple of days '
                        'for a holiday or even the whole year if you up to it'
                        '. Just give me all the information I need and Il do '
                        'all the magic for you in my trusty logbook, '
                        'revealing some more insight into your budget rather '
                        'than just how many pennys you have left over ' 
                        ';).', 80))
    print()
    print(textwrap.fill('So the information that my logbook needs to work ' 
                        'with are your available funds, incomes, expenses and '
                        'the timeframe in which you want to budget for. There '
                        'is an option to choose whether you want to budget '
                        'for a given month or a particular amount of days, '
                        'the choice is completely yours :) To simply put it, ' 
                        'you are dealing with a simple formula of available '
                        'funds + income - expenses. Use that formula as '
                        'you wish in any way you want, but walking it with '
                        'me may give you more insightful results. None the '
                        'less try out the LogBook and lets see where it '
                        'takes us.', 80))
    print()
    print(textwrap.fill('A few of the questions I am going to ask will give '
                        'you a y/n at the end. What y/n means is that you ' 
                        'have to choose either y which means yes or n which '
                        'means no. Choose whichever one you suits your desired'
                        ' purpose. Lets give it a shot with the question below'
                        '.', 80))


def name_question():
    '''
    Display, append and validate name question
    '''
    global detail_table
    global name
  
    # detail_table = BeautifulTable()
    # detail_table.columns.header = ["", ""]

    name = str(input(color.green + "\nPlease enter your name: " + color.reset))
    try:
        # Validate that name contains the right amount of characters
        if len(name) <= 0:
            raise ValueError("The name can't be left empty.")
        if len(name) >= 10:
            raise ValueError("The name has too many characters.")
    except ValueError as e:
        print(color.red + f'Invalid name. {e} Please provide your name again.' 
              + color.reset) 
        return name_question()


def first_question_confirmation():
    '''
    Display and validate name question
    '''
    question_confirm = str(input(color.green + 
                                 f"\nSo your name is {name} correct? (y/n): "
                                 + color.reset))
    try:
        # Validate that the input given is "y" or "n"
        if question_confirm == "y" or question_confirm == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(color.red + f'Invalid answer. {e} Please try again.' +
              color.reset)
        return first_question_confirmation()

    # Direct to functions on choice of "y" or "n" 
    if question_confirm == 'y':
        clear_terminal()
    if question_confirm == "n":
        clear_terminal()
        return name_question()
      
# First Questions Functions


def month_question():
    '''
    Display, validate and direct (to relevant next question) month question.
    '''
    global month_or_day
    month_or_day = (input(color.green + 
                          "\nWould you like to budget for a "
                          "particular month? (y/n): " 
                          + color.reset))
    try:
        # Validate that the input given is "y" or "n"
        if month_or_day == "y" or month_or_day == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(color.red + f'Invalid answer. {e} Please try again.' +
              color.reset)
        return month_question()

    # Direct to functions on choice of "y" or "n"  
    if month_or_day == 'y':
        return choose_month()
    if month_or_day == "n":
        return choose_day()


def choose_month():
    '''
    Display, append and validate choose month question
    '''
    global exact_days
    global chosen_month
    month = int(input(color.green + "Please give me the number of the month "
                      "you want to budget for \n(ie 1 is January and so on): "
                      + color.reset))
    try:
        # Validate that month input contains the corrrect details
        if month <= 0:
            raise ValueError("This cannot be 0 or under ")
        if month >= 13:
            raise ValueError("Please choose the months between 1 and 12.")
    except ValueError as e:
        print(color.red + f'Invalid input. {e} Please try again.' +
              color.reset)
        return choose_month()
    # !!! THIS NEEDS TO CHANGE !!!
    # Recieves data from which month number was chosen
    if month == 1: chosen_month = 'January'; exact_days =31
    if month == 2: chosen_month = 'Febuary';exact_days =28
    if month == 3: chosen_month = 'March';exact_days =31
    if month == 4: chosen_month = 'April';exact_days =30
    if month == 5: chosen_month = 'May';exact_days =31
    if month == 6: chosen_month = 'June';exact_days =30
    if month == 7: chosen_month = 'July';exact_days =31
    if month == 8: chosen_month = 'August';exact_days =31
    if month == 9: chosen_month = 'September';exact_days =30
    if month == 10: chosen_month = 'October';exact_days =31
    if month == 11: chosen_month = 'November';exact_days =30
    if month == 12: chosen_month = 'December';exact_days =31
	
	
def choose_day():
    '''
    Display, append and validate choose day question
    '''
    global exact_days
    exact_days = (input(color.green + "Then how many days do you want to "
                        "budget for?: " + color.reset))
    try:
        # Validate that month input contains the corrrect details
        if len(exact_days) <= 0:
            raise ValueError("This cannot be left empty.")
        if exact_days == "0":
            raise ValueError("Lets not go there.. atleast put 1 xD.")
    except ValueError as e:
        print(color.red + f'Invalid input. {e} Please try again.' +
              color.reset)
        return choose_day()


def timeframe_summary():
    '''
    Display all results from questions asked and give option to start over
    '''
    clear_terminal()
    if month_or_day == "y":
        print(color.reset + 
              (f"\n{name}, So you are budgeting for" + color.yellow +
               f" {chosen_month}," + color.reset + " which is approximately "
               + color.yellow + str(exact_days) + color.reset + " days long."
               ))
    if month_or_day == "n":
        print(color.reset + 
              (f"\n{name}, So you are budgeting for" + color.yellow +
               f"{exact_days} days."))

    timeframe_question = (input(color.green + "\nWould you like to enter your"
                          " timeframe details again?(y/n): " + color.reset))
    if timeframe_question == "y":
        clear_terminal()
        return first_questions()
    if timeframe_question == "n":
        clear_terminal()


# def reset_table():
#     '''
#     Resets detail_table and restarts the first questions function
#     '''
#     global detail_table
#     detail_table = None
#     detail_table = BeautifulTable()
#     detail_table.columns.header = ["", ""]
#     clear_terminal()
#     return first_questions()

# Financial Asset Functions


def asset_calculate():
    '''
   Takes in data of the financial assets plugged in
    '''
    asset = (input(color.green + "\nPlease enter The name of your available"
             " fund: " + color.reset))
    try:
        # Validate that the asset name contains the right amount of characters
        if len(asset) <= 0:
            raise ValueError("The asset name can't be left empty.")
        if len(asset) >= 20:
            raise ValueError("The asset name has too many characters.")
    except ValueError as e:
        print(color.red + f'Invalid name. {e} Please provide your asset name'
              ' again.' + color.reset)     
        return asset_calculate()

    amount = float(input(color.green + "Please enter the amount of that "
                         "available fund: " + color.reset))
    add_asset.append(amount)
    total = sum(add_asset)
    asset_table.rows.append([color.yellow + asset, amount, total])
    clear_terminal()
    print(asset_table)
    another_asset = (input(color.green + "Do you want to add another available"
                           " fund? y/n: " + color.reset))
    if another_asset == "y":
        clear_terminal()
        asset_calculate()
    if another_asset == "n":
        clear_terminal()
        print(color.blue + "Available funds" + color.reset)
        print(asset_table)
        asset_confirmation()


def asset_confirmation():
    '''
   Confirms if user wants to redo the  available funds
    '''
    restart_asset = (input(color.green + "\nWould you like to enter your "
                           "available funds again?(y/n): " + color.reset))
    try:
        # Validate that the input given is "y" or "n"
        if restart_asset == "y" or restart_asset == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(color.red + f'Invalid answer. {e} Please try again.' +
              color.reset)
        return asset_confirmation()

    if restart_asset == "y":
        clear_terminal()
        reset_asset_table()  
    if restart_asset == "n":
        clear_terminal()


def reset_asset_table():
    '''
   Resets asset table and starts  available funds questions again
    '''
    global asset_table
    global add_asset
    asset_table = None
    asset_table = BeautifulTable()
    asset_table.columns.header = ["asset", "amount", "total"]
    add_asset = []
    return asset_calculate() 

# Income Functions


def income_calculate():
    '''
   Takes in data of the incomes plugged in
    '''
    income = (input(color.green + "\nPlease enter The name of your income: "
              + color.reset))
    try:
        # Validate that the income name contains the right amount of characters
        if len(income) <= 0:
            raise ValueError("The income name can't be left empty.")
        if len(income) >= 20:
            raise ValueError("The income name has too many characters.")
    except ValueError as e:
        print(color.red + f'Invalid name. {e} Please provide your income name'
              ' again.' + color.reset)   
        return income_calculate()

    amount = float(input(color.green + "Please enter the amount of that "
                         "income: " + color.reset))  
    add_income.append(amount)
    total = sum(add_income)
    income_table.rows.append([color.yellow + income, amount,  total])
    clear_terminal()
    print(income_table)
    another_income = (input(color.green + "Do you want to add another income?"
                            " y/n: " + color.reset))
    if another_income == "y":
        clear_terminal()
        income_calculate()
    if another_income == "n":
        clear_terminal()
        print(color.blue + "Income" + color.reset)
        print(income_table)
        income_confirmation()


def income_confirmation():
    '''
   Confirms if user wants to redo the income
    '''
    restart_income = (input(color.green + "\nWould you like to enter your"
                            " income again?(y/n): " + color.reset))
                            
    try:
        # Validate that the input given is "y" or "n"
        if restart_income == "y" or restart_income == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(color.red + f'Invalid answer. {e} Please try again.' +
              color.reset)
        return income_confirmation()

    if restart_income == "y":
        clear_terminal()
        reset_income_table()  
    if restart_income == "n":
        clear_terminal()


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


def expense_calculate():
    '''
   Takes in data of the expenses plugged in
    '''
    expense = (input(color.green + "\nPlease enter The name of your expense: " 
               + color.reset))
    try:
        # Validate that expense name contains right amount of characters
        if len(expense) <= 0:
            raise ValueError("The income name can't be left empty.")
        if len(expense) >= 20:
            raise ValueError("The income name has too many characters.")
    except ValueError as e:
        print(color.red + f'Invalid name. {e} Please provide your income name'
              ' again.' + color.reset)  
        return expense_calculate()

    amount_exp = float(input(color.green + "Please enter the amount of that"
                             " expense: " + color.reset))
    add_expense.append(amount_exp)
    total = sum(add_expense)
    expense_table.rows.append([color.yellow + expense, amount_exp, total])
    clear_terminal()
    print(expense_table)
    another_expense = (input(color.green + "Do you want to add another expense"
                       "? y/n: " + color.reset))
    if another_expense == "y":
        clear_terminal()
        expense_calculate()
    if another_expense == "n":
        clear_terminal()
        print(color.blue + "Income" + color.reset)
        print(expense_table)
        expense_confirmation() 


def expense_confirmation():
    '''
   Confirms if user wants to redo the expense
    '''
    restart_expense = (input(color.green + "\nWould you like to enter your"
                       " expenses again?(y/n):  " + color.reset))
    try:
        # Validate that the input given is "y" or "n"
        if restart_expense == "y" or restart_expense == "n":
            accept = True
        else:
            accept = False
            if accept == False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(color.red + f'Invalid answer. {e} Please try again.' +
              color.reset)
        return expense_confirmation()

    if restart_expense == "y":
        clear_terminal()
        reset_expense_table()  
    if restart_expense == "n":
        clear_terminal()


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


def result_calculations():
    global asset_total
    global inco_total
    global expe_total
    global surplus
    global day_result
    inco_total = sum(add_income)
    expe_total = sum(add_expense)
    asset_total = sum(add_asset)
    calc_days = (int(f"{exact_days}"))

    # Calculations
    surplus = asset_total + inco_total - expe_total
    day_result = surplus / calc_days

    results_table.rows.append(["Available Funds", + asset_total])
    results_table.rows.append(["Income", + inco_total])
    results_table.rows.append(["Expenses", + expe_total])
    results_table.rows.append(["Surplus", + surplus])
    results_table.rows.append(["Budget per day", + day_result])


def results_page(): 
    '''
   Displays all calculated results and tables from information provided
    '''
    print(color.blue + f'Budget Summary of {name}' + color.reset)
    print(results_table)
    print(color.blue + "Your available funds are " 
          + color.reset + str(asset_total))
    print(color.blue + "Your total income is " 
          + color.reset + str(inco_total))
    print(color.blue + "Your total expense is " 
          + color.reset + str(expe_total))
    print(color.blue + "Your gross amount will be " 
          + color.reset + str(surplus))
    print(color.blue + f"you will be able to spend "
          + color.reset + f"{day_result} per day")
    print(color.reset + 
          textwrap.fill(f'Thanks {name}, for using Larrys Logbook, I hope I '
                        'have helped :) If you wish to start over just press '
                        'Run Program on top of the Terminal. See ya '
                        f'{name} ', 80))


# This is the main function, this is where everything runs---->

# And these are my global variables-->
# name = "x"
# detail_table = "y"
exact_days = "z"
days = "x"

asset_table = BeautifulTable()
asset_table.columns.header = ["asset", "amount", "total"]
add_asset = []

income_table = BeautifulTable()
income_table.columns.header = ["income", "amount",  "total"]
add_income = []

expense_table = BeautifulTable()
expense_table.columns.header = ["expense", "amount", "total"]
add_expense = []

results_table = BeautifulTable()
results_table.columns.header = ["", "",]
# And these are my global variables-->

#----condensed functions--------->


def first_questions():
    '''
   Condenses all of the question functions into one functon
    '''
    clear_terminal()
    print(color.reset + 
          textwrap.fill(f'Ok {name}... first I am going to ask you about your '
                        'timeframe before we go on to the actual available '
                        'funds, incomes and expenditures. Whether you want '
                        'to budget for a given month or a particular amount '
                        'of days, you choose :).', 80))
    month_question()
    timeframe_summary()


def budget_questions():
    print(color.reset + 
          textwrap.fill('Now lets get cracking with the available'
                        ' funds :). By available funds I mean money that you'
                        ' already have on you that you are willing to use in'
                        ' your budget. So if its a pension, a deeply imbedded'
                        ' life savings account or anything of that sort, '
                        'maybe just leave that out ;). What I mean is money '
                        'in your current account, or an amount in it you are '
                        'willing to give in your budget, same goes with  '
                        'revolut or other institutions like that. Cash on '
                        'hand may be another one you want to put in here. '
                        'In the end its all up to you to decide what you want '
                        'in here, but try leave nothing out that may be '
                        'necessary which may constitute as available funds,'
                        ' as the more detail you put in only helps you more.'
                        ' Add as many available funds as you wish and I will '
                        'add the total up for you :)', 80))
    asset_calculate()
    print(color.reset + 
          textwrap.fill('Now lets get cracking with the Income :).'
                        'Im sure you know what an income is, but an income in '
                        'what I am asking for is any amount of money you will '
                        'recieve within the timeframe you have given. Be it '
                        'a paycheck, an amount someone else is going to pay '
                        'you or any other situation that ends up with you '
                        'recieving money which you want to be added to your '
                        'budget. Just be aware not to add any amount that '
                        'still includes tax, try give the amount after '
                        'taxation. Add as many incomes as you wish and I will'
                        ' add the total up for you :) ', 80))
    income_calculate()
    print(color.reset +
          textwrap.fill('Now lets get cracking with the expenses'
                        ' :). Im sure we all know what expenses are, but '
                        'without this we would never really need to ever '
                        'budget in our lives! By expenses I am asking for '
                        'anything that will cost you money, ie: take money '
                        'away from you rather than recieve. There are loads '
                        'of expenses like rent, electricity, loan payments, '
                        'traveling expenses, groceries, anything that will '
                        'cost you. But im oonly asking you for all expenses '
                        'inside the timeframe you have given. Add as many '
                        'expenses as you wish and I will add the total up '
                        'for you as usual :) ', 80))
    expense_calculate()
    result_calculations()
    results_page()
# ----condensed functions------->


def main():
    '''
   Takes in all neccessary functions and initiates the functions 
    '''
    welcome_message()
    first_question_confirmation()
    first_questions()
    budget_questions()


main()

# This is the main function, this is where everything runs---->
