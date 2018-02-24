# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def getIntialWords(word):
    initialList = ''
    for c in word:
         initialList = initialList + '_'
    return initialList

def checkGuesscorrect(word,previousword,guess):
    if word.find(guess) != -1:
        index = word.find(guess)
        if previousword[index] == guess:
            return False
        else:
            return True
    else:
        return False


def changeChar(word,previousword,guess):
    result = ''
    index = word.index(guess)
    if index != -1:
        i = 0
        for c in previousword:
            if i == index:
                result = result + guess
            else:
                result = result + previousword[i]

            i += 1
        return result
    else:
        return previousword
        

def hangman():
     word = choose_word(load_words())
     guessingList = getIntialWords(word)
     guess = 8
     

     print word
     print 'Welocme to the game, Hangman!'
     print 'I am thinking of a word that is ',len(word),' letters '
     

     ## gamne
     ## starts
     ## here
     while guess > 0:
         print '-------------------------------------'
         print 'You have ',guess,' guesses left.'
         guessChar = raw_input('Please guess a letter: ')
         print guessChar[0]
         if checkGuesscorrect(word,guessingList,guessChar[0]):
             guessingList = changeChar(word,guessingList,guessChar[0])
             print 'Good guess: ',guessingList
             if guessingList == word:
                 print 'Congratulations, you won!'
                 break
         else:
             guess -= 1
             print 'Oops! That letter is not in my word: ',guessingList
    
    
      
hangman()
