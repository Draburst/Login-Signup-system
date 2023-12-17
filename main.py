import dbcommunicate as db
from database import User, session


#########################################################################################################################################

def generate_decor():
    print("=========================================================================================")
    
generate_decor()

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
                get_id = str(input('-- '))
                db.delete_user(get_id)

            elif option_value == 3:
                print('Create transaction...')
                get_amount = str(input('-- '))
                db.create_transaction(username, get_amount)

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
                get_amount = str(input('-- '))
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
    if (username == 'Draburst'):
        
        print('SUCCES ADMIN!\nРere is your opportunity')
        for k,v in menu_admin.items():
            print(f'\t{k}: {v}')
        question_option = int(input('-- '))
        generate_decor()
        process_option_admin(question_option, username)

    else:
        print('SUCCES USER!\nРere is your opportunity')
        for k,v in menu.items():
            print(f'\t{k}: {v}')
        question_option_two = int(input('-- '))
        generate_decor() 
        process_option_all(question_option_two, username)   



mes = input('HELLO USER!\nThis is example for login and signup\n --Sign-up\n --Sign-in\n')    
if mes == 'Sign-up':
    generate_decor()
    message_one = str(input('Enter your username:\t'))
    message_two = int(input('Enter name password:\t'))
    generate_decor()
    if db.add_user(name=message_one, password=message_two) == True:
        menu_prog(message_one)
    else:
        print('Invalid username or password')

if mes == 'Sign-in':
    generate_decor()
    messages = str(input('Enter your username:\t'))
    messages_one = str(input('Enter your password:\t'))
    generate_decor()
    if db.check_user_in_bd_by(messages, messages_one) == True:
        menu_prog(messages)
    else:
        print('Invalid username or password')






