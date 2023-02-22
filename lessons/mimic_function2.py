"""Write a mimic function, input a string and return the letter of that index"""

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return("too high of a index")
#if we made it here, that means the letter_idx is valid
    return my_words[letter_idx]

print(mimic_letter("fornite",3))
