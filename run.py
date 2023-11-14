from beautifultable import BeautifulTable
from colorama import Fore, Back, Style
# Import textwrap to wrap long text for a better visual
import textwrap
# Import os to let clear_terminal clear the terminal screen
import os


class Color:
    # Colors used throughout code.
    blue = Style.BRIGHT + Fore.BLUE
    yellow = Fore.LIGHTYELLOW_EX
    green = Style.BRIGHT + Fore.GREEN
    red = Back.RED
    reset = Style.RESET_ALL


# Functions used throughout code.


def clear_terminal():
    """
    Clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def y_n_validator(question, function):
    """
    Validate y/n questions.
    """
    try:
        # Validate that the input given is "y" or "n"
        if question == "y" or question == "n":
            accept = True
        else:
            accept = False
            if accept is False:
                raise ValueError("Please only type 'y' or 'n'.")
    except ValueError as e:
        print(color.red + f'Invalid answer. {e} Please try again.' +
              color.reset)
        return function()


# INTRODUCTION AND NAME FUNCTIONS


def welcome_message():
    '''
    Display the logo, image and welcome message
    '''
    print(color.blue + '''#
#          ##    #####   #####   #   #   ####
#         #  #   #    #  #    #   # #   #
#        #    #  #    #  #    #    #     ####
#        ######  #####   #####     #         #
#        #    #  #   #   #   #     #    #    #
#######  #    #  #    #  #    #    #     ####
                                                        
#                        ######
#         ####    ####   #     #   ####    ####   #    #
#        #    #  #    #  #     #  #    #  #    #  #   #
#        #    #  #       ######   #    #  #    #  ####
#        #    #  #  ###  #     #  #    #  #    #  #  #
#        #    #  #    #  #     #  #    #  #    #  #   #
#######   ####    ####   ######    ####    ####   #    #''')
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
    print(textwrap.fill('A few of the questions I am going to ask will give '
                        'you a y/n at the end. What y/n means is that you '
                        'have to choose either y which means yes or n which '
                        'means no. Choose whichever one you suits your desired'
                        ' purpose. Lets give it a shot with the question below'
                        '.', 80))


def name_question():
    '''
    Display and validate name question
    '''
    global name
    name = str(input(color.green + "\nPlease enter your name: " + color.reset))
    try:
        if name.isspace() is True:
            raise ValueError("The name can't be left empty.")
        # Validate that name contains the right amount of characters
        if len(name) <= 0:
            raise ValueError("The name can't be left empty.")
        if len(name) >= 10:
            raise ValueError("The name has too many characters.")
    except ValueError as e:
        print(color.red + f'Invalid name. {e} Please provide your name again.'
              + color.reset) 
        return name_question()


def name_confirmation():
    '''
    Display and validate name question
    '''
    question_confirm = str(input(color.green +
                                 f"\nSo your name is {name} correct? (y/n): "
                                 + color.reset).lower())
    # Validates y/n input questions.
    y_n_validator(question_confirm, name_confirmation)
    # Direct to functions on choice of "y" or "n"
    if question_confirm == 'y':
        clear_terminal()
    if question_confirm == "n":
        clear_terminal()
        return name_re_enter()


def name_re_enter():
    '''
    Display and validate re-enter name question
    '''
    global name
    name = str(input(color.green + "\nPlease enter your name: " + color.reset))
    # Validate that name contains the right amount of characters
    try:
        if name.isspace() is True:
            raise ValueError("The name can't be left empty.")
        if len(name) <= 0:
            raise ValueError("The name can't be left empty.")
        if len(name) >= 10:
            raise ValueError("The name has too many characters.")
    except ValueError as e:
        print(color.red + f'Invalid name. {e} Please provide your name again.'
              + color.reset)
        return name_re_enter()
    return name_confirmation()


# TIMEFRAME FUNCTIONS


def month_question():
    '''
    Display and direct (to relevant next question) month question.
    '''
    global month_or_day
    month_or_day = (input(color.green +
                          "\nWould you like to budget for a "
                          "particular month? (y/n): "
                          + color.reset).lower())
    # Validates y/n input questions.
    try:
        # Validate that the input given is "y" or "n"
        if month_or_day == "y" or month_or_day == "n":
            accept = True
        else:
            accept = False
            if accept is False:
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
    # Validate if input given is an int/float.
    while True:
        try:
            month = int(input(color.green + "Please give me the number of the "
                              "month you want to budget for \n(ie 1 is "
                              "January and so on): " + color.reset))
            # Validate that month input contains the corrrect details
            if month <= 0:
                raise ValueError("This cannot be 0 or under.")
            if month >= 13:
                raise ValueError("Please choose the months between 1 and "
                                 "12.")
            # Recieves data from which month number was chosen
            if month == 1:
                chosen_month = 'January'
                exact_days = 31
            if month == 2:
                chosen_month = 'Febuary'
                exact_days = 28
            if month == 3:
                chosen_month = 'March'
                exact_days = 31
            if month == 4:
                chosen_month = 'April'
                exact_days = 30
            if month == 5:
                chosen_month = 'May'
                exact_days = 31
            if month == 6:
                chosen_month = 'June'
                exact_days = 30
            if month == 7:
                chosen_month = 'July'
                exact_days = 31
            if month == 8:
                chosen_month = 'August'
                exact_days = 31
            if month == 9:
                chosen_month = 'September'
                exact_days = 30
            if month == 10:
                chosen_month = 'October'
                exact_days = 31
            if month == 11:
                chosen_month = 'November'
                exact_days = 30
            if month == 12:
                chosen_month = 'December'
                exact_days = 31
            break
        except ValueError:
            print(color.red + "Thats not a valid number. Please enter a "
                  "number." + color.reset)

	
def choose_day():
    '''
    Display and validate choose day question.
    '''
    global exact_days
    # Validate if input given is an int/float.
    while True:
        try:
            exact_days = int(input(color.green + "Then how many days do you "
                                   "want to budget for?: " + color.reset))
            try:
                # Validate that month input contains the corrrect details
                if exact_days <= 0:
                    raise ValueError("Lets not go there.. atleast put 1 xD.")
            except ValueError as e:
                print(color.red + f'Invalid input. {e} Please try again.' +
                      color.reset)
                return choose_day()
            break
        except ValueError:
            print(color.red + "Thats not a valid number. Please enter a "
                  "number." + color.reset)


def timeframe_summary():
    '''
    Display summary of timeframe questions
    '''
    clear_terminal()
    # Direct to print statements on choice of "y" or "n"
    if month_or_day == "y":
        print(color.reset +
              (f"\n{name}, So you are budgeting for" + color.yellow +
               f" {chosen_month}," + color.reset + " which is "
               + color.yellow + str(exact_days) + color.reset + " days long."
               ))
    if month_or_day == "n":
        print(color.reset + 
              (f"\n{name}, So you are budgeting for " + color.yellow +
               f"{exact_days} days."))


def timeframe_re_enter():
    '''
    Give option to re enter timeframe questions
    '''
    timeframe_question = (input(color.green + "\nWould you like to re-enter "
                          "your timeframe details again?(y/n): "
                                + color.reset).lower())
    # Validates y/n input questions.
    y_n_validator(timeframe_question, timeframe_re_enter)
    # Direct to functions on choice of "y" or "n"
    if timeframe_question == "y":
        clear_terminal()
        return timeframe_questions()
    if timeframe_question == "n":
        clear_terminal()


# AVAILABLE FUNDS FUNCTIONS


def fund_calculate():
    '''
    Takes in data of the available funds plugged in
    '''
    fund = (input(color.green + "\nPlease enter the name of your available"
                  " fund: " + color.reset))
    try:
        # Validate that available fund name contains right amount of characters
        if fund.isspace() is True:
            raise ValueError("The name can't be left empty.")
        if len(fund) <= 0:
            raise ValueError("The available fund name can't be left empty.")
        if len(fund) >= 20:
            raise ValueError("The available fund name has too many "
                             "characters.")
    except ValueError as e:
        print(color.red + f'Invalid name. {e} Please provide your\n available'
              'fund name again.' + color.reset)     
        return fund_calculate()
    # Validate if amount input is a number. 
    while True:
        try:
            amount = float(input(color.green + "Please enter the amount of "
                           "that available fund: " + color.reset))
            break
        except ValueError:
            print(color.red + "Thats not a valid number. Please enter a "
                  "number." + color.reset)
    # Append, round, calculate and display Available Fund data.
    add_fund.append(round(amount, 2))
    total = sum(add_fund)
    fund_table.rows.append([color.yellow + fund, round(amount, 2), total])
    clear_terminal()
    print(fund_table)
    return extra_fund()


def extra_fund():
    '''
    Displays funds supplied and gives option to re-enter again
    '''
    another_fund = (input(color.green + "Do you want to add another available"
                          " fund? y/n: " + color.reset).lower())
    # Validates y/n input questions.
    y_n_validator(another_fund, extra_fund)
    # Direct to functions on choice of "y" or "n"
    if another_fund == "y":
        clear_terminal()
        fund_calculate()
    if another_fund == "n":
        clear_terminal()
        print(color.blue + "Available funds" + color.reset)
        print(fund_table)
        print()
        print("These are the Available Funds you have supplied.")
        fund_confirmation()
        

def fund_confirmation():
    '''
   Confirms if user wants to redo the available funds
    '''
    restart_fund = (input(color.green + "\nWould you like to re-enter your "
                          "available funds again?(y/n): " 
                          + color.reset).lower())
    # Validates y/n input questions.
    y_n_validator(restart_fund, fund_confirmation)
    # Direct to functions on choice of "y" or "n"
    if restart_fund == "y":
        clear_terminal()
        reset_fund_table()  
    if restart_fund == "n":
        clear_terminal()


def reset_fund_table():
    '''
   Resets fund table and starts available funds questions again
    '''
    global fund_table
    global add_fund
    fund_table = None
    fund_table = BeautifulTable()
    fund_table.columns.header = ["available funds", "amount", "total"]
    add_fund = []
    return fund_calculate() 


# INCOME FUNCTIONS


def income_calculate():
    '''
   Takes in data of the incomes plugged in
    '''
    income = (input(color.green + "\nPlease enter The name of your income: "
              + color.reset))
    try:
        # Validate that the income name contains the right amount of characters
        if income.isspace() is True:
            raise ValueError("The name can't be left empty.")
        if len(income) <= 0:
            raise ValueError("The income name can't be left empty.")
        if len(income) >= 20:
            raise ValueError("The income name has too many characters.")
    except ValueError as e:
        print(color.red + f'Invalid name. {e} Please provide your\n income '
              'name again.' + color.reset)   
        return income_calculate()
    # Validate if amount input is a number.   
    while True:
        try:
            amount = float(input(color.green + "Please enter the amount of "
                                 "that income: " + color.reset))
            break
        except ValueError:
            print(color.red + "Thats not a valid number. Please enter a "
                  "number." + color.reset)
    # Append, round, calculate and display Income data.
    add_income.append(round(amount, 2))
    total = sum(add_income)
    income_table.rows.append([color.yellow + income, round(amount, 2), total])
    clear_terminal()
    print(income_table)
    return extra_income()


def extra_income():
    '''
    Displays income supplied and gives option to re-enter again
    '''
    another_income = (input(color.green + "Do you want to add another income?"
                            " y/n: " + color.reset).lower())
    # Validates y/n input questions.
    y_n_validator(another_income, extra_income)
    # Direct to functions on choice of "y" or "n"
    if another_income == "y":
        clear_terminal()
        income_calculate()
    if another_income == "n":
        clear_terminal()
        print(color.blue + "Income" + color.reset)
        print(income_table)
        print()
        print("These are the Incomes you have supplied.")
        income_confirmation()


def income_confirmation():
    '''
   Confirms if user wants to redo the income
    '''
    restart_income = (input(color.green + "\nWould you like to re-enter your"
                            " income again?(y/n): " + color.reset).lower()) 
    # Validates y/n input questions.
    y_n_validator(restart_income, income_confirmation)                     
    # Direct to functions on choice of "y" or "n"
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


# EXPENSE FUNCTIONS


def expense_calculate():
    '''
   Takes in data of the expenses plugged in
    '''
    expense = (input(color.green + "\nPlease enter The name of your expense: " 
               + color.reset))
    try:
        # Validate that expense name contains right amount of characters
        if expense.isspace() is True:
            raise ValueError("The name can't be left empty.")
        if len(expense) <= 0:
            raise ValueError("The expense name can't be left empty.")
        if len(expense) >= 20:
            raise ValueError("The expense name has too many characters.")
    except ValueError as e:
        print(color.red + f'Invalid name. {e} Please provide your\n expense '
              'name again.' + color.reset)  
        return expense_calculate()
    # Validate if amount input is a number.
    while True:
        try:
            amount = float(input(color.green + "Please enter the amount of"
                                 " that expense: " + color.reset))
            break
        except ValueError:
            print(color.red + "Thats not a valid number. Please enter a "
                  "number." + color.reset)
    # Append, round, calculate and display Expense data.
    add_expense.append(round(amount, 2))
    total = sum(add_expense)
    expense_table.rows.append([color.yellow + 
                               expense, round(amount, 2), total])
    clear_terminal()
    print(expense_table)
    return extra_expense()


def extra_expense():
    '''
    Displays expenses supplied and gives option to re-enter again
    '''
    another_expense = (input(color.green + "Do you want to add another expense"
                       "? y/n: " + color.reset).lower())
    # Validates y/n input questions.
    y_n_validator(another_expense, extra_expense)
    # Direct to functions on choice of "y" or "n"
    if another_expense == "y":
        clear_terminal()
        expense_calculate()
    if another_expense == "n":
        clear_terminal()
        print(color.blue + "Expenses" + color.reset)
        print(expense_table)
        print()
        print("These are the Expenses you have supplied.")
        expense_confirmation() 


def expense_confirmation():
    '''
   Confirms if user wants to redo the expense
    '''
    
    restart_expense = (input(color.green + "\nWould you like to re-enter your"
                       " expenses again?(y/n):  " + color.reset).lower())
    # Validates y/n input questions.
    y_n_validator(restart_expense, expense_confirmation)
    # Direct to functions on choice of "y" or "n"
    if restart_expense == "y":
        clear_terminal()
        reset_expense_table()  
    if restart_expense == "n":
        clear_terminal()


def reset_expense_table():
    '''
    Resets expense table and starts expense questions again
    '''
    global expense_table
    global add_expense
    expense_table = None
    expense_table = BeautifulTable()
    expense_table.columns.header = ["expense", "amount", "total"]
    add_expense = []
    return expense_calculate()


def result_calculations():
    '''
    Calculates data given and calculates results for results page
    '''
    global fund_total
    global inco_total
    global expe_total
    global round_surplus
    global round_day_result
    # Adds available funds, income and exspense
    inco_total = sum(add_income)
    expe_total = sum(add_expense)
    fund_total = sum(add_fund)
    # Converts exact days into an interger
    calc_days = (int(f"{exact_days}"))
    # Calculations for Results Page
    surplus = fund_total + inco_total - expe_total
    round_surplus = round(surplus, 2)
    day_result = surplus / calc_days
    round_day_result = round(day_result, 2)
    # Appends calculations to results_table for Results Page
    results_table.rows.append(["Available Funds", color.yellow
                               + str(fund_total)])
    results_table.rows.append(["Income", color.yellow + str(inco_total)])
    results_table.rows.append(["Expenses", color.yellow + str(expe_total)])
    results_table.rows.append(["Surplus", color.yellow + str(round_surplus)])
    results_table.rows.append(["Days", color.yellow + str(exact_days)])
    results_table.rows.append(["Budget per day", color.yellow
                               + str(round_day_result)])


def results_page():
    '''
    Displays all calculated results and results_table from info provided
    '''
    # Direct to print statements on choice of "y" or "n"
    if month_or_day == 'y':

        print(color.blue + f'Budget Summary of {name} for ' + color.yellow
              + f'{chosen_month}' + color.reset)
    else:
        print(color.blue + f'Budget Summary of {name} for ' + color.yellow
              + f'{exact_days} days' + color.reset)
    # Print statements and results_table to be displayed on Results Page
    print(results_table)
    print(color.blue + "Your available funds are "
          + color.reset + str(fund_total))
    print(color.blue + "Your total income is "
          + color.reset + str(inco_total))
    print(color.blue + "Your total expense is "
          + color.reset + str(expe_total))
    print(color.blue + "Your surplus (amount left after expenses) will be "
          + color.reset + str(round_surplus))
    if round_day_result >= 0:
        print(color.blue + f"you will be able to spend "
              + color.reset + f"{round_day_result} per day")
    else:
        print(color.blue + "Unfortunately there is not a daily budget "
              "as it will be in negative :(.")
    print()
    # Ending Message
    print(color.reset +
          textwrap.fill(f'Thanks {name}, for using Larrys Logbook, I hope I '
                        'have helped :) If you wish to start over just press '
                        'Run Program on top of the Terminal, or press s '
                        f'below to start over. See ya {name}', 80)) 
    start_over = (input(color.green + "Please enter s to start over: "
                  + color.reset).lower())
    # Validates y/n input questions.
    try:
        # Validate that the input given is "y" or "n"
        if start_over == "s":
            accept = True
        else:
            accept = False
            if accept is False:
                raise ValueError("Please only type 's'.")
    except ValueError as e:
        print(color.red + f'Invalid answer. {e} Please try again.' +
              color.reset)
        clear_terminal()
        return results_page()
    # Direct to functions on key "s"
    if start_over == 's':
        clear_terminal()
        return restart()


def restart():
    '''
    Restarts the application
    '''
    global fund_table
    global income_table
    global expense_table
    global results_table
    global add_fund
    global add_income
    global add_expense
    fund_table = None
    fund_table = BeautifulTable()
    fund_table.columns.header = ["available fund", "amount", "total"]
    add_fund = []
    income_table = None
    income_table = BeautifulTable()
    income_table.columns.header = ["income", "amount",  "total"]
    add_income = []
    expense_table = None
    expense_table = BeautifulTable()
    expense_table.columns.header = ["expense", "amount", "total"]
    add_expense = []
    results_table = None
    results_table = BeautifulTable()
    results_table.columns.header = ["", ""]
    return main()


# ALL TABLES AND COLOR CLASS

color = Color()

fund_table = BeautifulTable()
fund_table.columns.header = ["available fund", "amount", "total"]
add_fund = []

income_table = BeautifulTable()
income_table.columns.header = ["income", "amount",  "total"]
add_income = []

expense_table = BeautifulTable()
expense_table.columns.header = ["expense", "amount", "total"]
add_expense = []

results_table = BeautifulTable()
results_table.columns.header = ["", ""]


# CONDENSED FUNCTIONS


def timeframe_questions():
    '''
    Condenses all of the timeframe functions into one functon.
    '''
    month_question()
    timeframe_summary()
    timeframe_re_enter()


def budget_questions():
    '''
    Condenses all of the budget functions into one functon.
    '''
    print(color.blue + "Available funds" + color.reset)
    print()
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
    fund_calculate()
    print(color.blue + "Income" + color.reset)
    print()
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
    print(color.blue + "Expenses" + color.reset)
    print()
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


def main():
    '''
   Takes in all neccessary functions and initiates the functions 
    '''
    welcome_message()
    name_confirmation()
    clear_terminal()
    print(textwrap.fill(f'Ok {name}... So the information that my logbook ' 
                        'needs to work with are your available funds, incomes,'
                        ' expenses and the timeframe in which you want to '
                        'budget for. There is an option to choose whether you '
                        'want to budget for a given month or a particular '
                        'amount of days, the choice is completely yours :). ' 
                        'To simply put it, you are dealing with a simple '
                        'formula of available funds + income - expenses. Use '
                        'that formula as you wish in any way you want, but '
                        'walking it with me may give you more insightful '
                        'results. None the less try out the LogBook and lets '
                        'see where it takes us.', 80))
    print()
    print(color.reset + 
          textwrap.fill('First I am going to ask you about your '
                        'timeframe before we go on to the actual available '
                        'funds, incomes and expenditures. Whether you want '
                        'to budget for a given month or a particular amount '
                        'of days, you choose :).', 80))
    timeframe_questions()
    budget_questions()


main()
