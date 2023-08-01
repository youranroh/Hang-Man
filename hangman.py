# download the randomwords pip from below to run the Hangman game 
# https://pypi.org/project/Random-Word/


#import the package
from random_word import RandomWords
r = RandomWords()

# methods to use
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

# Create a random word
word = r.get_random_word()
#print(word)

# create a life. This is the hang man
life = 6

# creat an array that will hold the characters
answer = []
usedChars = []

#print("Guessing chances remaining: " + str(life))

for underbars in word:
    answer.append("_")
# for loop

hangman = []
hangman.append('_________')
hangman.append('|       |')      # hangman[1]
hangman.append('|')       # hangman[2]
hangman.append('|')       # hangman[3]
hangman.append('|')       # hangman[4]
hangman.append('|')       # hangman[5]
hangman.append('|')       

print('\n'.join(hangman))

while True:
    if life > 0 and "_" in answer:
        # print the current status of the answers
        print('')
        print(' '.join(map(str, answer))) 
        print("Guessing chances remaining: " + str(life))
        
        # ask the user for an input
        userInput = input("Guess a character!\n>>> ")
        
        if len(userInput) == 1: # the user input must be a one letter character   
            if userInput in usedChars:
                print("\n\nThe character is already used.")
            # -------- if statement
            else:
                if userInput in word:   # if the input is in the word,
                    index = find(word, userInput)   # get the index of the char in the word
                    for i in index:
                        answer[i] = userInput   # and fill in the answer
                    usedChars.append(userInput)
                    # ------- if statement
                else:   # if the input is not contained in the String,
                    print("\n\nThe character " + userInput + " does not exist in this word.")
                    life-=1     # deduct a life.
                    usedChars.append(userInput)
                    if life == 5:
                        hangman[2] = '|       O'
                    elif life == 4:
                        hangman[3] = '|       |'
                        hangman[4] = '|       |'
                    elif life == 3:
                        hangman[3] = '|      \\|'
                    elif life == 2:
                        hangman[3] = '|      \\|/'
                    elif life == 1:
                        hangman[5] = '|      /'
                    elif life == 0:
                        hangman[5] = '|      / \\'    
                # ------- else statement
        else :
            print("Invalid input! Try again.")
        # -------- else statement
        print('\n'.join(hangman))
    elif "_" not in answer:
        print("You win!!")
        break
    # --------- elif
    else:
        print("You lose!!")
        break
    # --------- elif

print("The word was: " + word)