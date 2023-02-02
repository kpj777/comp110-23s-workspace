"""One Shot Wordle; give player one shot at guessing secert word"""

__author__ = "730605045"

secert_word: str = "pythonnn"

#emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#Input guess
guess: str = input(f"What is your 6-letter guess? ")

#Do not move on until length of guess is equal to 6
while len(guess) != 6:
    guess: str = input(f"That was not 6 letters! Try again: ")


#index of the word your are checking
word_idx: int = 0
#establish a variable to store the resulting emoji of guess
emoji_idx: str = ""

#print emoji string
while word_idx < len(secert_word):
    #green box check
    guess_idx: str = (guess[word_idx])
    secert_idx: str = (secert_word[word_idx])
    if (guess_idx == secert_idx):
        emoji_idx = emoji_idx + GREEN_BOX + " "
    else:
        search_word: bool = False 
        search_idx: int = 0
        #yellow box check
        while (search_word == False) and (search_idx < len(secert_word)):
            search: str = (secert_word[search_idx])
            if (guess_idx == search):
                search_word: bool = True
            else:
                search_idx = search_idx + 1   
        if (search_word == True):
            emoji_idx = emoji_idx + YELLOW_BOX + " "
        else:
            #white box if no yellow or white
             emoji_idx = emoji_idx + WHITE_BOX + " "
    #repeat
    word_idx = word_idx + 1
print(emoji_idx)

#Once length equals six, test if that is secert word
if (guess == secert_word):
    print(f"Woo! You got it ")
    quit()
else:
    print(f"Not quite. Play again soon! ")
    quit()



