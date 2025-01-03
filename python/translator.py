import sys

alphatobraille = { 
    "a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..", "e" : "O..O..",
    "f" : "OOO...", "g" : "OOOO..", "h" : "O.OO..", "i" : ".OO...", "j" : ".OOO..",
    "k" : "O...O.", "l" : "O.O.O.", "m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.",
    "p" : "OOO.O.", "q" : "OOOOO.", "r" : "O.OOO.", "s" : ".OO.O.", "t" : ".OOOO.",
    "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO", "y" : "OO.OOO",
    "z" : "O..OOO", " " : "......", "cap" : ".....O" 
}

brailletoalpha = { 
    "O....." : "a", "O.O..." : "b", "OO...." : "c", "OO.O.." : "d", "O..O.." : "e",
    "OOO..." : "f", "OOOO.." : "g", "O.OO.." : "h", ".OO..." : "i", ".OOO.." : "j",
    "O...O." : "k", "O.O.O." : "l", "OO..O." : "m", "OO.OO." : "n", "O..OO." : "o",
    "OOO.O." : "p", "OOOOO." : "q", "O.OOO." : "r", ".OO.O." : "s", ".OOOO." : "t",
    "O...OO" : "u", "O.O.OO" : "v", ".OOO.O" : "w", "OO..OO" : "x", "OO.OOO" : "y",
    "O..OOO" : "z", "......" : " ", ".....O" : "cap"
    
}

digitstobraile = {
    "0" : ".OOO..", "1" : "O.....", "2" : "O.O...", "3" : "OO....", "4" : "OO.O..",
    "5" : "O..O..", "6" : "OOO...", "7" : "OOOO..", "8" : "O.OO..", "9" : ".OO...",
}

brailetodigits = {
    ".OOO.." : "0", "O....." : "1", "O.O..." : "2", "OO...." : "3", "OO.O.." : "4",
    "O..O.." : "5", "OOO..." : "6", "OOOO.." : "7", "O.OO.." : "8", ".OO..." : "9",
    "......" : " ", ".O.OOO" : "number follows"
}

symbolstobraile = {
    "!" : "..OOO.", "'" : "..O...", "?" : "..O.OO", "-" : "....OO"
}

# Check if the input is a valid braille string
def check_braille(s):
    if len(s) % 6 != 0:
        return False
    for i in range(0, len(s), 6):
        str = s[i:i+6]
        if s[i:i+6] not in brailletoalpha and s[i:i+6] not in brailetodigits:
            return False
    return True

# Convert the input string to braille
def alpha_to_braille(s):
    result = ""
    numberfollows = ".O.OOO"
    # Check if the input is a number
    number = False

    for char in s:
        if(char.isupper()):
            result += alphatobraille["cap"]
            char = char.lower()
            result += alphatobraille[char]

        elif char.isdigit():
            # Check if number follows
            if not number:
                result += numberfollows
                number = True
            result += digitstobraile[char]

        # Check if the character is a space
        elif char == " ":
            result += alphatobraille[char]
            # Reset the number flag if the space is followed by a number, number ends when space is encountered
            number = False

        # Check if the character is a symbol
        elif char in symbolstobraile:
            result += symbolstobraile[char]

        else:
            result += alphatobraille[char]

    return result


# Convert the input braille string to alpha
def braille_to_alpha(s):
    result = ""
    capital = False # Flag to check if the character is capital
    number = False # Flag to check if the character is a number

    for i in range(0, len(s), 6):
        str = s[i:i+6]

        #Check if the string is a valid braille character and not a number
        if str in brailletoalpha and not number:

            # Check if the character is a capital letter
            if str != alphatobraille["cap"]:
                if capital:
                    result += brailletoalpha[str].upper()
                    capital = False
                else:
                    result += brailletoalpha[str]
            
            elif str == alphatobraille["cap"]:
                capital = True
                result += ""

        # Check if the character is a number
        elif str in brailetodigits or number:
            # Check if number follows
            if str == ".O.OOO":
                number = True
            else:
                result += brailetodigits[str]
        
        # Check if the character is a space
        elif str == "......" :
            number = False
            result += " "

    return result


def main(): 
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: python translator.py <text>")
        sys.exit(1)
    
    input = " ".join(args)
    
    #Check if all the characters in the text are either 'O' or '.'
    #if all(char in 'O.' for char in input): 
    if check_braille(input):
        print(braille_to_alpha(input)) 
    else: 
        print(alpha_to_braille(input)) 
    

if __name__ == "__main__":
    main()