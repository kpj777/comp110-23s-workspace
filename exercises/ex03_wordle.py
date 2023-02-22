"Full Working version of wordle using structure functions"

__author__ = 730604045



def contains_char(chr_word: str, chr: str) -> bool:
    # search if the single character of the second string is in first string)
    assert len(chr) == 1
    # index of the word your are checking
    chr_idx: int = 0
    while chr_idx < len(chr_word):
        # chr check
        secert_idx: str = (chr_word[chr_idx])
        if (chr == secert_idx):
         return True
        else:
            search_word = False 
            search_idx: int = 0
            # character check
            while (search_word is False) and (search_idx < len(chr_word)):
                search: str = (chr_word[search_idx])
                if (chr == search):
                    search_word = True
                else:
                    search_idx = search_idx + 1   
            if (search_word is True):
                return True
            else:
                # no character matches
                return False


def emojified(guess: str, secert_word: str) -> str:
    #call a color of emoji if search is true, return string of colored emoji boxes
    # emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secert_word)
    result: str = ""
    guess_idx: int = 0
    while guess_idx < len(secert_word):
        #searches if the guess is at guess index automatically, if not then it goes through contains_char to search for all possible variables
        if guess[guess_idx] == secert_word[guess_idx]:
            result += GREEN_BOX
        else:
            if contains_char(secert_word, guess[guess_idx]) is True:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        guess_idx += 1
    return result
            
def input_guess (length: int) -> str:
    #This is the check to see if the length of word is  the length of the guess
    while True:
        guess = input(f"Enter a {length} character word: ")
        if len(guess) == length:
            return guess
        else:
         print(f"That wasn't {length} chars! Try again.")

def main() -> None:
    """The entrypoint of the program and main game loop."""
    #these are the variables, turn being what turn it is, secert_word being the secert word of the day, and won being the playing boolian variable
    turn: int = 1
    secert_word: str = "codes"
    won = False
    while turn <= 6 and not won:
        #while less than or equal to 6 turns
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secert_word))
        result = emojified(guess, secert_word)
        print(result)
        if secert_word == guess:
            won = True
        else:
            turn += 1
    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
            






    

            
            

    
    


    




