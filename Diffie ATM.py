print("Welcome to Diffie Bank Mobile ATM!")
continuing = True
StartBal = 1000000
CurrentBal = StartBal
usereman = "JohnDeereGreen"
name = input("Input your username into this space like a hand in a glove: ")
if name != usereman:
    print("That username is incorrect. Please reload and try again.")
    continuing = False
if name == usereman:
    password = "PickupTruck"
    pwinput = input("Hello there, Mr. Diffie, please enter the classification of your first car. ")
    if pwinput == password:
        print("")
        print("Correct password entered.")
        print("")
        actionchoice = input("Just make your next selection: Would you like to deposit money, withdraw money, view balance, or log out? ")
    if pwinput != password:
            print("Sorry, that password doesn't match our records. Please reload the page and try again.")
            continuing = False
    while (continuing) == True:
        if actionchoice == "deposit":
            deposit = int(input("While you're still in line, you can pay your last respects (One quarter at a time) in the form of: $"))
            print("Your account's current balance is $" + str(CurrentBal))
            CurrentBal = CurrentBal+deposit
            print("Your account's new balance is $" + str(CurrentBal))
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "Deposit":
            deposit = int(input("How much would you like to deposit into your account today? "))
            print("Your account's current balance is $" + str(CurrentBal))
            CurrentBal = CurrentBal+deposit
            print("Your account's new balance is $" + str(CurrentBal))
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "withdraw":
            withdraw = int(input("Don't spread my ashes out to sea, but input your desired withdrawal amount. Please don't lay me down to rest afterwards, either. "))
            print("Your account's current balance is $" + str(CurrentBal))
            CurrentBal = CurrentBal-withdraw
            print("Your account's new balance is $" + str(CurrentBal))
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "Withdraw":
            withdraw = int(input("How much would you like to withdraw from your account today? "))
            print("Your account's current balance is $" + str(CurrentBal))
            CurrentBal = CurrentBal-withdraw
            print("Your account's new balance is $" + str(CurrentBal))
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "view balance":
            print("Just let your balance of $" + str(CurrentBal) + " burn in memory of all of my good times.")
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "View Balance":
            print("Your account's current balance is $" + str(CurrentBal))
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "balance":
            print("Just let your balance of $" + str(CurrentBal) + " burn in memory of all of my good times.")
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "Balance":
            print("Your account's current balance is $" + str(CurrentBal))
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "current balance":
            print("Just let your balance of $" + str(CurrentBal) + " burn in memory of all of my good times.")
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "Current Balance":
            print("Your account's current balance is $" + str(CurrentBal))
            actionchoice = input("I can put your mind at ease if I fill your next request: ")
        if actionchoice == "log out":
            print("Your account's current balance is $" + str(CurrentBal) + ". You have now successfully logged out of Diffie Bank's Mobile ATM. Have a great day.")
            print()
            continuing = False

if continuing == False:
    print("RIP Joe Diffie. I am sure someone will fix you up with a mannequin, and we will make sure that it is blonde.")
    print("You will always be the life of the party, even if you are now dead and gone.")
    print()
    print("Joe Logan Diffie, December 28, 1958 - March 29, 2020. Rest In Peace, Mr. Diffie.")