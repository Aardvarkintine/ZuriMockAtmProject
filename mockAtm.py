# Task Title: Python: Loops & Functions

# Improve on your ATM mockup from last course to include the following:

# 1. Use functions

# 2. Include register, and login

# 3. Generate Account Number

# 4. Any other improvement you can think of (extra point)

# Imports
import random
import datetime as dt

# Database
database = {}

# Timestamp
timeStamp = dt.datetime.now()

# Feedback
errorMessage = 'Transaction failed \n'
successMessage = 'Transaction successful \n'

# FUNCTIONS
# Program Entry


def init():
    print('Welcome to Bank PYTHON')

    haveAccount = int(
        input('Do you have an account with us? \n1. Yes \n2. No \n'))
    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()

    else:
        print('Invalid option selected')

# Account number generation


def generateAccountNumber():
    return random.randrange(0000000000, 9999999999)


# Registration
def register():
    print('======== REGISTRATION ========')

    firstName = input('First name \n')
    lastName = input('Last name \n')
    otherName = input('Other name \n')
    email = input('Email address \n')
    phoneNumber = int(input('Phone number \n'))
    password = input('Password \n')
    defaultBalance = 0
    complaint = ''

    isPasswordMatch = False

    while isPasswordMatch == False:
        confirmPassword = input('Confirm password \n')

        if(password == confirmPassword):

            isPasswordMatch = True
            print('Your account has been created successfully \n')

            accountNumber = generateAccountNumber()
            database[accountNumber] = [firstName, lastName, otherName,
                                       email, phoneNumber, password, defaultBalance, complaint]

            print('This is your account number: %s' % accountNumber)
            print('Please keep if safe')
            print('=== ==== ====== === ====')
            login()

        else:
            print('error 001: Passwords do not match!')


# Login
def login():
    print('======== LOGIN ========')

    userAccountNumber = int(input('Your account number \n'))
    isUserValid = False

    for accountNumber, userDetails in database.items():
        while isUserValid == False:

            if(userAccountNumber == accountNumber):
                isUserValid = True
                password = input('Your password \n')

                if(password == userDetails[5]):
                    bankOperation(accountNumber)

                else:
                    print('Incorrect password or account number')
            else:
                print('User not found')
                login()


# Operations
def bankOperation(accountNumber):
    print(f'Welcome {database[accountNumber][0]}\n')
    print('Today is %s ' % timeStamp.strftime('%y-%m-%d  %H : %M : %S \n'))
    print('These are the available options \n')
    print('1. Withdrawal \n')
    print('2. Cash Deposit \n')
    print('3. Complaint \n')
    selectedOption = int(input('Please select an option \n'))

    if (selectedOption == 1):
        withdrawal(accountNumber)

    elif (selectedOption == 2):
        deposit(accountNumber)

    elif (selectedOption == 3):
        complaint(accountNumber)

    else:
        print('Invalid option selected, Please try again')


# Withdrawal
def withdrawal(accountNumber):
    print('You have selected withdrawal \n')
    withdrawal = int(input('How much would you like to withdraw? \n '))
    if (withdrawal > database[accountNumber][6]):
        print(errorMessage.upper() + 'Insufficient funds!')
    else:
        print(successMessage.upper() + 'Please take your cash \n')
        database[accountNumber][6] -= withdrawal
        print(f'Your balance is: {database[accountNumber][6]}')
        moreOptions()


# Cash Deposit
def deposit(accountNumber):
    print('You have selected cash deposit \n')
    deposit = int(input('How much would you like to deposit? \n'))
    database[accountNumber][6] += deposit
    print(successMessage.upper())
    print(f'Your balance is: {database[accountNumber][6]}')
    moreOptions()


# Complaint
def complaint(accountNumber):
    print('You have selected complaint \n')
    complaint = input('What issue will you like to report? \n')
    database[accountNumber][7] = complaint
    print('Your issue will be resolved in the next 24 hours \nThank you for contacting us')
    moreOptions()


def moreOptions():
    print('')


# ********* PROGRAM ZONE ***********
init()