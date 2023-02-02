"""Ask User for a number, goes until they get it right"""

SECERT: int = 4
guess: int = int(input("Guess a number! "))

playing: bool = True

while playing:
    if guess == SECERT:
        print("Yay? you got it right.")
        playing = False
    else:
        print("Wrong number. :( ")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd. The answer is even.")
        if guess > SECERT:
                print("Your guess is too high! ")
        else: #guess is < secert
            print("your guess is too low. ")
        guess = int(input("Make another guess! "))
quit()

    




