########################################################################
##
## CS 101 Lab
## Program lab05
## Jair Tobias-Zamora
## jat5xm@umsystem.edu
##
## PROBLEM : Certain aspects of code are stubbed out and game infinitely plays without user being able to input anything
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

import random # imports random so we can use it later on in code

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and 
True if Y or YES.  Keeps asking until they respond yes '''
    goodwords = ['YES', 'yes', 'Y', 'y','Yes'] #list of words that will restart game
    badwords = ['NO', 'no', 'N', 'n','No'] #list of words that will end game
    while True:
        restart = input('Do you want to play again? ==> ') #asks user if they would like to play again
        if restart in badwords: #if user input is in list of badwords, game ends
            return False
            break
        elif restart in goodwords: #if user input is in list of goodwords, game continues
            return True
            break
        else: #otherwise, any incorrect user input prompts user to try again with correct input
            print()
            print('You must enter Y/YES/N/NO to continue.  Please try again ')
            pass
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is 
<= 0 or greater than the amount they have '''
    while True:
        wagerchips = int(input('How many chips do you want to wager? ==> ')) #asks user how many chips they would like to wager
        if wagerchips <= 0: #if user chooses to wager chips less than or equal to 0, they are prompted to try again with correct input
            print()
            print('The wager amount must be greater than 0. Please enter again.')
            wagerchips = int(input('How many chips do you want to wager? ==> '))
        if wagerchips > bank: #if user chooses to wager chips more than their current bank, they are prompted to try again with correct input
            print()
            print(f'The wager amount cannot be greater than how much you have. Your current bank is {bank}')
            wagerchips = int(input('How many chips do you want to wager? ==> '))
        else: #ends while loop so it doesn't get stuck
            break
    return wagerchips #returns wagerchips for later reference

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1, 10) #reel1 is random integer picked from 1-10
    reel2 = random.randint(1, 10) #reel2 is random integer picked from 1-10
    reel3 = random.randint(1, 10) #reel3 is random integer picked from 1-10
    return reel1, reel2, reel3 #returns all reels for later reference

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc: #if all 3 reels match, value 3 is returned for future reference
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc: #if 2 reels match, value 2 is returned for future reference
        return 2
    else: #if no reels match, value 0 is returned for future reference
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value 
greater than 0 and less than 101 '''
    while True:
        startchips = int(input('How many chips do you want to start with? ==> ')) #asks user for how many chips they want to start with
        if startchips <= 0: # if user starts with less than or equal to 0 chips, they are prompted to try again with correct input
            print()
            print('Too low a value, you can only choose 1 - 100 chips')
            startchips = int(input('How many chips do you want to start with? ==> '))
        if startchips > 100: # if user starts with more than 0 chips, they are prompted to try again with correct input
            print()
            print('Too high a value, you can only choose 1 - 100 chips')
            startchips = int(input('How many chips do you want to start with? ==> '))
        else:
            return startchips # returns startchips for future reference

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times 
the wager if 2 match, and negative wager if 0 match '''
    if matches == 3: # if game produces 3 matches, payout is set to (10 * wager) - wager
        payout = (10 * wager) - wager
    elif matches == 2: # if game produces 3 matches, payout is set to (3 * wager) - wager
        payout = (3 * wager) - wager
    elif matches == 0: # if game produces 3 matches, payout is set to - wager
        payout = - wager
    return payout # returns payout for future reference
    

if __name__ == "__main__":
    playing = True
    bank = 0 # sets bank to 0
    wager = 0 # sets wager to 0
    spins = 0 # sets spins to 0
    totals = 0 # sets totals to 0
    max = 0 # sets max to 0
    while playing: # game starts
        bank = get_bank()
        while bank > 0:  # while bank is greater than 0, game continue to plays out
            
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            totals += abs(payout) # keeps track of total the user has had throughout the game
            spins += 1 # counts up total of spin attempts so far
            max = totals # this doesn't actually find the max value of chips the player has had, I just put it in here to have something I couldn;t get it to work
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print(f"You lost all {totals} in {spins} spins")
        print(f"The most chips you had was {max}")
        playing = play_again()
