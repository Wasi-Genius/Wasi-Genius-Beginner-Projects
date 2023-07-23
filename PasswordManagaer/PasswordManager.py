import string
import time
import random as r

print('Hello welcome to the program!')

num_of_pwords = input('How many passwords are you submitting today?: ')

while True:
    try:
        num_of_pwords = int(num_of_pwords)
        if 1 <= num_of_pwords <= 10:
            break
        elif num_of_pwords == 0:
            print(
                "If you do not have any passwords, have a good day!")
            break
        else:
            num_of_pwords = input(
                "Uh oh, you inputted a wrong value! Please only enter an integer number between 1 and 10: ")
    except ValueError:
        num_of_pwords = input(
            "Uh oh, you inputted a wrong value! Please only enter an integer number between 1 and 10: ")

dont_start = ""
if num_of_pwords == 0:
    dont_start = True
else:
    dont_start = False

websites_list = []
scrambled_passwords = []
processed_password = []
stored_passwords = []
org_password_list = []

i = 0
while i != num_of_pwords and not dont_start:
    website = input(f'\nWhat website/service are you inputting your password for?: ')
    websites_list.append(website)
    password = input('Thank you, what is the password?: ')
    user_scramble = input('Do you want me to scramble that password for you? (Y/N): ')
    while True:
        try:
            user_scramble = str(user_scramble)
            if user_scramble == "Y":
                org_password_list.append(password)
                scramble_process = [*password]
                h = 0
                for item in scramble_process:
                    scramble_symbol = r.choice(string.ascii_letters + string.digits + string.punctuation)
                    scramble_process[h] = scramble_symbol
                    h += 1
                    print("scrambling...")
                    time.sleep(.5)
                    processed_password = ''.join(scramble_process)
                time.sleep(1)
                print("\nAll Scrambled!")
                stored_passwords.append(processed_password)
                i += 1
                break
            elif user_scramble == "N":
                org_password_list.append('')
                stored_passwords.append(password)
                i += 1
                break
            else:
                user_scramble = input("\nUh oh, you didn't input (Y/N), please try again!: ")
        except ValueError:
            user_scramble = input("\nUh oh, you didn't input (Y/N), please try again!: ")


user_end = False
a = 0
while not user_end and not dont_start:
    time.sleep(.5)
    view_passwords = input(
        '\nAll passwords have been stored or scrambled or both. \nWould you like to view them? (Y/N) Or would you like to delete them? (D): ')
    while True:
        try:
            view_passwords = str(view_passwords)
            if view_passwords == "Y":
                for item in websites_list:
                    time.sleep(1)
                    print("\nWebsite: " + websites_list[a])
                    print("Password: " + stored_passwords[a])
                    if org_password_list[a] != '':
                        see_original_password = input("Would you like to see the original password? (Y/N): ")
                        if see_original_password == "Y":
                            # noinspection SpellCheckingInspection
                            descram_con = [*org_password_list[a]]
                            for i in descram_con:
                                time.sleep(.5)
                                print("descrambling...")
                            time.sleep(1)
                            print(f'\nThe original password was: {org_password_list[a]}')
                            a += 1
                        else:
                            print("\nGot it!")
                            a += 1
                    else:
                        a += 1
                break
            elif view_passwords == "N":
                time.sleep(1)
                print('\nAlright, you can always view them when you wish!')
                break
            elif view_passwords == "D":
                time.sleep(1)
                print('\nThank you for using my program, All of your websites and passwords have been deleted, have a good day!')
                websites_list = []
                stored_passwords = []
                user_end = True
                break
            else:
                view_passwords = input("\nUh oh, you didn't input (Y/N) or (D), please try again!: ")
        except ValueError:
            view_passwords = input("\nUh oh, you didn't input (Y/N) or (D), please try again!: ")







        
