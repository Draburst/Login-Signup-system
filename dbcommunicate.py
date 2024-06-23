from database import User, Transaction, session
import colorama
from colorama import Fore, Style

colorama.init()

def get_transaction_by_user(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        print(f'Succes!\nIts your transaction:')
        transactions = user.transactions
        for transaction in transactions:
            print(
            f"{Fore.GREEN}\n"
            "\t+------------------------------------------+\n"
            f"\t| {Fore.YELLOW}ID:{Fore.WHITE} {transaction.id:<36} |\n"
            "\t+------------------------------------------+\n"
            f"\t| {Fore.YELLOW}AMOUNT:{Fore.WHITE} {transaction.amount:<32} |\n"
            "\t+------------------------------------------+\n"
            f"\t| {Fore.YELLOW}CATEGORY:{Fore.WHITE} {transaction.category:<30} |\n"
            "\t+------------------------------------------+\n"
            f"{Style.RESET_ALL}"
            )
    else:
        return print(f'Not found name {username}')



def create_transaction(username, amount, category):
    user = session.query(User).filter_by(username=username).first()

    try:
        transaction = Transaction(category=category, amount=amount, user=user)
        session.add(transaction)
        session.commit()
        if transaction:
            return print('Transaction created succesful')
        else:
            return print('Error created transaction')
    except Exception as error:
        print(f'This is error: {error}')

def is_user_admin(username):
    user = session.query(User).filter_by(username=username).first()
    if user and user.is_admin:
        return True
    return False

def delete_user(id):
    user = session.query(User).filter_by(id=id).first()
    if user:
        session.delete(user)
        session.commit()
        return print('User has been deleted')
    else:
        return print('User not found')
    

def get_all_user(status):
    if status == 1:
        users = session.query(User).all()
        for user in users:
            print(f"\tID: {user.id}\n\tUsername: {user.username}\n\tPassword: {user.password}\n")
    else:
        return print('Sorry but you are not an admin!')
    

def get_user_info(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        return print(f'ACOUNT INFO:\n\tUser ID: {user.id}\n\tUsername: {user.username}\n\tPassword: {user.password}')
    else:
        return print(f'User with username "{username}" not found.')

def add_user(name, password, is_admin):
    try:
        user = User(username=name, password=password, is_admin=is_admin)
        session.add(user)
        session.commit()
        if user:
            return True
        else:
            return False
    except Exception as error:
        if 'UNIQUE constraint failed' in str(error):
            print('User already exists')
        else:
            print('Error created user', {error})
        
def check_user_in_bd_by(username, password):
    user = session.query(User).where(User.username == username and User.password == password).first()
    if user:
        return True
    return False