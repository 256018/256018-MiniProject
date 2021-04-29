import os
import withdraw
import deposit
import PasswordChange


def clear_screen():
    # function to clear the output of the screen
    os.system('cls')
    print()  # print blank line after clearing the screen


def menu2(account):
    # account is a list of account info
    # account[0] id
    # account[1] name
    # account[2] password
    # account[3] balance

    print("\n---------Hello, {0}--------- ".format(account[1]))
    ch = int(input("\n1) show info \n2) deposit\n3) withdraw\n"
                   "4) change password \n5) logout\n\nchoice>> "))

    clear_screen()
    if ch == 1:
        print("ID: {}\nName: {}\nBalance: {}\n".format(account[0], account[1], account[3]))
    elif ch == 2:
        deposit.deposit(account)
    elif ch == 3:
        withdraw.withdraw(account)
    elif ch == 4:
        PasswordChange.change_password(account)
    elif ch == 5:
        return
    else:
        print("ERROR: Wrong choice. Please Enter a valid choice\n")

    menu2(account)
