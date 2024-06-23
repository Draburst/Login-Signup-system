import time
import dbcommunicate as db
from database import User, session
from colorama import init, Fore, Style
import keyboard
import os

init()

RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE

is_work = True
#########################################################################################################################################

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
        
def process_option_admin(option, username):
    if str(option).isdigit():
        option_value = int(option)
        if option_value in menu_admin.values():
            if option_value == 0:
                # Логіка для опції 'acount'
                db.get_user_info(username)
            elif option_value == 1:
                # Логіка для опції 'users'
                db.get_all_user(status=1)
            elif option_value == 2:
                print('Before deleting a user, find out his id')
                get_id = str(input(YELLOW + '[*] '))
                db.delete_user(get_id)
            elif option_value == 3:
                print('Create transaction...')
                get_amount = str(input(YELLOW + '[*] '))
                get_category = str(input(YELLOW + '[*] '))
                db.create_transaction(username, get_amount, get_category)
            elif option_value == 4:
                print('Get transaction by username...')
                db.get_transaction_by_user(username)
        else:
            print("Невідома опція")
    else:
        print("Невідома опція")

def process_option_all(option, username):
    if str(option).isdigit():
        option_value = int(option)
        if option_value in menu.values():
            if option_value == 0:
                # Логіка для опції 'acount'
                db.get_user_info(username)
            elif option_value == 1:
                print('Create transaction')
                get_amount = str(input(YELLOW + '[*] '))
                db.create_transaction(username, get_amount)
            # Треба ще придумати щось для простих користувачів
            #elif option_value == 1:
            #    # Логіка для опції 'users'
            #    print("Ви вибрали опцію 'users'")
            #elif option_value == 2:
            #    # Логіка для опції 'delete_user'
            #    print("Ви вибрали опцію 'delete_user'")
        else:
            print("Невідома опція")
    else:
        print("Невідома опція")
menu = {
    'ACOUNT': 0,
    'CREATE_TRANSACTION': 1,
    'GET_TRANSACTIONS': 2,
}
menu_admin = {
    'ACOUNT': 0,
    'USERS' : 1,
    'DELETE_USER': 2,
    'CREATE_TRANSACTION': 3,
    'GET_TRANSACTIONS': 4,
}
category = {
    'product': 0,
    'medecine': 1,
    'profit': 2,
}
def menu_prog(username):
    if db.is_user_admin:
        print('SUCCES ADMIN!\nHere is your opportunity')
        print(
        "\n"
        "\033[92m +------------------------------------------+\n"
        "\033[92m |  1. Account: {}                          |\033[37m\n"               
        "\033[92m |  2. Users: {}                            |\033[37m\n"
        "\033[92m |  3. Delete User: {}                      |\033[37m\n"
        "\033[92m |  4. Create Transaction: {}               |\033[37m\n"
        "\033[92m |  5. Get Transactions: {}                 |\033[37m\n"
        "\033[92m +------------------------------------------+\n".format(
            menu_admin['ACOUNT'],
            menu_admin['USERS'],
            menu_admin['DELETE_USER'],
            menu_admin['CREATE_TRANSACTION'],
            menu_admin['GET_TRANSACTIONS']
        ))
        question_option = int(input(YELLOW + '[*] '))
        process_option_admin(question_option, username)
    else:
        print('SUCCES USER!\nHere is your opportunity')
        print(
        "\n"
        "\033[92m +------------------------------------------+\n"
        "\033[92m | 1. Account: {}                           |\033[37m\n"
        "\033[92m | 4. Create Transaction: {}                |\033[37m\n"
        "\033[92m | 5. Get Transactions: {}                  |\033[37m\n"
        "\033[92m +------------------------------------------+\n".format(
            menu["ACOUNT"],
            menu["CREATE_TRANSACTION"],
            menu["GET_TRANSACTIONS"],
        ))
        question_option_two = int(input(YELLOW + '[*] '))
        process_option_all(question_option_two, username)
def start():
    print(
       BLUE + "                                                                                                 \n"
    + BLUE + "                                                                                                 \n"
    + BLUE + "`7MM\"\"\"Yb. `7MM\"\"\"Mq.        db      `7MM\"\"\"Yp, `7MMF'   `7MF'`7MM\"\"\"Mq.   .M\"\"\"bgd MMP\"\"MM\"\"YMM \n"
    + BLUE + "  MM    `Yb. MM   `MM.      ;MM:       MM    Yb   MM       M    MM   `MM. ,MI    \"Y P'   MM   `7 \n"
    + BLUE + "  MM     `Mb MM   ,M9      ,V^MM.      MM    dP   MM       M    MM   ,M9  `MMb.          MM      \n"
    + BLUE + "  MM      MM MMmmdM9      ,M  `MM      MM\"\"\"bg.   MM       M    MMmmdM9     `YMMNq.      MM      \n"
    + BLUE + "  MM     ,MP MM  YM.      AbmmmqMA     MM    `Y   MM       M    MM  YM.   .     `MM      MM      \n"
    + BLUE + "  MM    ,dP' MM   `Mb.   A'     VML    MM    ,9   YM.     ,M    MM   `Mb. Mb     dM      MM      \n"
    + BLUE + ".JMMmmmdP' .JMML. .JMM..AMA.   .AMMA..JMMmmmd9     `bmmmmd\"'  .JMML. .JMM.P\"Ybmmd\"     .JMML.    \n"
    + BLUE + "                                                                                                 \n"
    + BLUE + "                                                                                                 \n"
        + BLUE + "                              " + GREEN + "  Version: 1.0    \n"
        + YELLOW + "                 Draburst - System Login                    \n"
        + BLUE + "                    Written by Draburst                      \n"
        + WHITE + "                                                                  \n"
        + WHITE + "                      ** DISCLAIMER **                            \n"
        + WHITE + " THIS SOFTWARE DEMONSTRATES A SIMPLE LOGIN AND REGISTRATION SYSTEM.\n"
        + WHITE + " YOU CAN REGISTER A NEW USER AND THEN LOG IN WITH THE CREATED CREDENTIALS.\n"
        + WHITE + " ENJOY EXPLORING THE FUNCTIONALITIES AND LEARNING HOW AUTHENTICATION WORKS.\n"
        + WHITE + " NOTE: THIS IS A DEMONSTRATION SOFTWARE AND SHOULD NOT BE USED IN PRODUCTION.\n"
        + WHITE + "                                                                  \n"
        + WHITE + " Close this window if you wish to exit. Otherwise,                \n"
        + WHITE + " press [ENTER] key to continue..."
        )
    while True:
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
                clear_screen()
                break
            time.sleep(0.1)
    print(
    f"{Fore.GREEN}\n"
    " +------------------------------------------+\n"
    " |                                          |\n"
    " |           HELLO USER!                    |\n"
    " | This is an example for login and signup  |\n"
    " |                                          |\n"
    " |             [*] Sign-up                  |\n"
    " |             [*] Sign-in                  |\n"
    " |                                          |\n"
    " +------------------------------------------+\n"
    f"{Style.RESET_ALL}"
    )
    mes = input(f"{Fore.GREEN}Please enter your choice: {Style.RESET_ALL}")
    if mes == 'Sign-up':
        message_one = str(input(YELLOW + '[*] ''Enter your username:\t'))
        message_two = int(input(YELLOW + '[*] ''Enter name password:\t'))
        is_admin_input = input(Fore.YELLOW + '[*] ' + Fore.GREEN + 'Is this user an admin? (yes/no):\t').strip().lower()
        # Перевірка введення is_admin
        is_admin = is_admin_input in ['yes', 'y', 'true', '1']
        if db.add_user(name=message_one, password=message_two, is_admin=is_admin):
            clear_screen()
            print(Fore.GREEN + "User added successfully.")
            user = session.query(User).filter_by(username=message_one).first()
            menu_prog(user.username)
        else:
            print(RED + 'Invalid username or password')
    if mes == 'Sign-in':
        messages = str(input(YELLOW + '[*] ' +'Enter your username:\t'))
        messages_one = str(input(YELLOW + '[*] ' +'Enter your password:\t'))
        if db.check_user_in_bd_by(messages, messages_one) == True:
            clear_screen()
            menu_prog(messages)
        else:
            print(RED + 'Invalid username or password')
start()





