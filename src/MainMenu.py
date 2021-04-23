def mainmenu():
    print('*********WELCOME TO ATM**********\n')
    print("Enter 1 to Login")
    print("Enter 2 to create an Account")
    print("Enter 3 to exit the menu")
    choice = int(input())
    if choice == 1:
        clear_screen()
        try:
            login(accounts_list)
        except KeyboardInterrupt:
            clear_screen()
    elif choice == 2:
        create_account(accounts_list)
    elif choice == 3:
        # close the program
        exit(0)
    else:
        clear_screen()
        print("ERROR: Wrong choice\n")
    mainmenu()


if __name__ == '__main__':
    mainmenu()
