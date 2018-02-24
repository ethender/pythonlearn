from ps3a import *
import time
from perm import *

import random


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    words = get_perms(hand,len(hand))
    if len(words) != 0:
        ##return words[0]
        ranNum = random.randint(0,len(words))
        return words[ranNum]
    else:
        return None

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed. 

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...

    
    score = 0
    while len(hand) != 0:
        display_hand(hand)
        word = comp_choose_word(hand,word_list)
        if word != None:
            thisScore = get_word_score(word,len(hand))
            update_hand(hand,word)
            score += thisScore
            print '"',word,'" earned',thisScore,' points. Total: ',score
        else:
            break

    print 'Total score: ',score
            
        
        

    
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    prevHand = None
    while True:
        playOptions()
        playOption = raw_input("Enter An Option For Game: ")
        if playOption == 'e':
            break
        elif playOption == 'n':
            playerOptions()
            playerOption = raw_input("Enter An Option For Player: ")
            if playerOption == 'u':
                ranNum = random.randint(0,len(word_list))
                hand = get_frequency_dict(word_list[ranNum])
                prevHand = hand
                play_hand(hand,word_list)
            elif playerOptions == 'c':
                ranNum = random.randint(0,len(word_list))
                hand = get_frequency_dict(word_list[ranNum])
                prevHand = hand
                comp_play_hand(hand,word_list)
        elif playOption == 'r':
            playerOptions()
            playerOption = raw_input("Enter An Option For Player: ")
            if playerOption == 'u':
                ranNum = random.randint(0,len(word_list))
                if prevHand == None:
                    hand = get_frequency_dict(word_list[ranNum])
                    prevHand = hand
                else:
                    hand = prevHand
                
                play_hand(hand,word_list)
            elif playerOptions == 'c':
                ranNum = random.randint(0,len(word_list))
                if prevHand == None:
                    hand = get_frequency_dict(word_list[ranNum])
                    prevHand = hand
                else:
                    hand = prevHand
                comp_play_hand(hand,word_list)


##
## Game Options
##
def playOptions():
    print 'Prees "n", For Play New Game.'
    print 'Press "r", For Play Last Game.'
    print 'Press "e", For Exit The Game.'

##
## player Options
##
def playerOptions():
    print 'Press "u", For User Play'
    print 'Press "c", For Computer Play'
    

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
