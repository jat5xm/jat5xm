########################################################################
##
## CS 101 Lab
## Program 5
## Jair Tobias-Zamora
## jat5xm@umsystem.edu
##
## PROBLEM : Need to create a program that creates a check digit to ensure data entry is correct and valid
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

# import statements


# functions

def get_school(libcard) -> str: #WORKS
    if libcard[5] == '1': #if index 5 in library card is 1, the school is School of Computing and Engineering SCE
        school = 'School of Computing and Engineering SCE'
        return school
    elif libcard[5] == '2': #if index 5 in library card is 2, the school is School of Law
        school = 'School of Law'
        return school
    elif libcard[5] == '3': #if index 5 in library card is 3, the school is College of Arts and Sciences
        school = 'College of Arts and Sciences'
        return school
    else: #if index 5 is in library card is any other value, the school is Invalid School
        school = 'Invalid School'
        return school


def get_grade(libcard) -> str: #WORKS
    if libcard[6] == '1': #if index 6 in library card is 1, the grade is Freshman
        grade = 'Freshman'
        return grade
    elif libcard[6] == '2': #if index 6 in library card is 2, the grade is Sophomore
        grade = 'Sophomore'
        return grade
    elif libcard[6] == '3': #if index 6 in library card is 3, the grade is Junior
        grade = 'Junior'
        return grade
    elif libcard[6] == '4': #if index 6 in library card is 4, the grade is Senior
        grade = 'Senior'
        return grade
    else: #if index 6 in library card is 1, the grade is Invalid Grade
        grade = 'Invalid Grade'
        return grade

def character_value(ch : str) -> int: #WORKS
    for i in ch: #checks index in ch and assigns chvalue to the asci code of (ch) - 65 so A can be worth 0 and Z be worth 25
        chvalue = ord(ch) - 65
    return chvalue

'''def get_check_digit(libcard : str) -> int: #DOESNT WORK
    check_digit = 
    return check_digit'''

def verify_check_digit(libcard : str) -> tuple: #DOESNT WORK
    if len(libcard) != 10: #if library card length isn't 10, user is notified of error
        print('The length of the number given must be 10')
        return False
    '''if :
        print('The first 5 characters must be A-Z. the invalid character is at !! is !!')
        return False
    if :
        print('The last 3 characters must be 0-9, the invalid character is at !! is !!')
        return False'''
    if libcard[5] != '1' or libcard[5] != '2' or libcard[5] != 3:
        print('The sixth character must be 1, 2, or 3')
        return False
    if libcard[6] != '1' or libcard[6] != '2' or libcard[6] != '3' or libcard[6] != '4':
        print('The seventh character must be 1, 2, 3, or 4')
        return False
    else:
        print(' ')
        return True
    '''if :
        print('Check Digit !!! does not match calculated value !!!')
        return False'''

if __name__ == "__main__":

    # main program
    playing = True
    print('Main Program'.center(50)) #prints Main program and centers it
    print('Linda Hall'.center(50)) #prints Linda Hall and centers it
    print('Library Card Check'.center(50)) #prints Library Card Check and centers it
    print('=' * 50) #prints a border created by '=' signs
    print()

    while playing:

        libcard = str(input('Enter Library Card. Hit ENTER to exit. ==> ')) #prompts user to enter their library card
        ch = ' '

        school = get_school(libcard)
        grade = get_grade(libcard)
        chvalue = character_value(ch)
        '''check_digit = get_check_digit(libcard)'''
        verification = verify_check_digit(libcard)
    
        if verification is True: #if verification ends up being True, prints what school the student belongs to and their grade based off the library card info
            print('Library card is valid.')
            print(f'The card belongs to a student in {school}')
            print(f'The card belongs to a {grade}')
            break
        else:
            print()
            libcard = str(input('Enter Library Card. Hit ENTER to exit. ==> '))

    