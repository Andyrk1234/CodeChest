__author__ = 'Paarth Bhasin'

'''
Function: encode(filename1, filename2)

    Author: Paarth Bhasin and Huy Vu

    Preconditions: filename1 and filename2 have been provided.
    Postconditions: The Morse-Code Encoding of each letter in filename1 is written in filename2.

    VALID INPUTS: None

    INVALID INPUTS: None

    COMPLEXITY:
        Best Case: O(N), where N is the number of characters in filename1.
        Worst Case: O(N),  where N is the number of characters in filename1.

Function: decode(filename1, filename2)

    Author: Paarth Bhasin and Huy Vu

    Preconditions: filename1 and filename2 have been provided.
    Postconditions: The Morse-Code Encoding in filename1 is converted into normal text and written in filename2.

    VALID INPUTS: None

    INVALID INPUTS: None

    COMPLEXITY:
        Best Case: O(N), where N is the number of letters(in morse-code) in filename1.
        Worst Case: O(N),  where N is the number of letters(in morse-code) in filename1.


Function: main()

    Author: Paarth Bhasin and Huy Vu

    Preconditions: None
    Postconditions: Menu commands:
                    e inputfile outputfile: Encodes inputfile into Morse Code and writes the encoding in outputfile.
                    d inputfile outputfile: Translates inputfile from Morse Code to its actual text and writes the
                    translation in output file.
                    c inputfile: Compares the length of ASCII Code Representation of the text in inputfile to that of
                    Morse Code representation of text in the inputfile
                    q: Quits the program
                    Based on the command the user enters.
    VALID INPUTS: None

    INVALID INPUTS: None

    COMPLEXITY:
        Best Case: O(1)
        Worst Case: O(1)

'''

import re

from Task1 import number_of_characters
from Task3 import write_ascii

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }


def encode(inputfile, outputfile):
    f1 = open(inputfile, 'r')
    f2 = open(outputfile, 'w')
    lines = f1.readlines()  # So lines = ["sos sos", "pqr sos", "abc sos", "stu sos"]
    for line in lines:  # Iteration1: line = "sos sos", Iteration2: line = "pqr sos", Iteration3: line = "abc stu"
        # Iteration4: line = "stu sos"
        # print(line)
        words = line.split()  # Iteration1: words = ["sos", "sos"], Iteration2: words = ["pqr", "sos"],
        final = ""  # Iteration3: words = ["abc", "stu"], Iteration4: words = ["stu", "sos"]
        for word in words:  # word = "sos" and "sos", then "pqr" and "sos", then "abc" and "stu", then "stu" and "sos"
            code = ""
            # print(word)
            for i in range(len(word)):
                if word[i].isalpha():
                    # print(word[i])
                    morse = str(CODE[word[i].upper()])
                    # print(morse)
                    if '.' in morse:  # why does it remove the -(hyphens)?
                        morse = re.sub("\.", "10", morse)
                        # print(morse)
                        # print("hi1")
                    if '-' in morse:
                        morse = re.sub("-", "1110", morse)
                        # print(morse)
                        # print("hi2")
                    morse = morse[:-1]  # Index 0 to last - 1. So we leave the last element.
                    morse += "000"
                    # print("\?")
                    code += morse
                    # print(code)
            # print(code)
            final += code + " "
            # print("this")
            # print(final)
            # print(line)
        f2.write(final + '\n')
    f1.close()
    f2.close()


def decode(inputfile, outputfile):
    f1 = open(inputfile, 'r')
    f2 = open(outputfile, 'w')
    lines = f1.readlines()
    # print(lines)
    for line in lines:
        words = line.split()  # words = [101010001110111011100010101000] in this case
        decodedfinal = ""  # the decoded message will be kept here.
        for word in words:
            decoded = ""
            # print(word)  # 101010001110111011100010101000
            word = re.sub("000", " ", word)  # 10101 11101110111 10101 (s + o + s = sos)
            # print(word)  # 10101 11101110111 10101 (s + o + s = sos)
            newline = word.split()  # newline = [10101, 11101110111, 10101] in this case
            # Iteration 1: word = 10101, Iteration 2: word = 11101110111, Iteration 3: word = 10101
            for newword in newline:
                newword = re.sub("1110", "-", newword)
                newword = re.sub("10", ".", newword)
                newword = re.sub("111", '-', newword)
                newword = re.sub("1", '.', newword)
                # After Iteration1 : newword = ...,
                decoded += newword + " "  # After Iteration2: newword = ... ---,
                # After Iteration3: newword = ... --- ...
                # print(decoded)

            # We need to combine all these Morse Codes into a single Morse Code Symbol
            # representation. And this would be for one word. We need to do this for
            # all words in a line. And then for all lines in the text file.
            # After for loop ends, decode = "... --- ..."
            d = decoded.split()
            decoded = ""
            # print(d)

            for value in d:
                for key in CODE:
                    if CODE[key] == value:
                        value = re.sub(value, key, value)
                        # print(value)
                        decoded += str(value)
            decodedfinal += decoded + " "
            # Introduce a space after the word has been decoded to differentiate between other words.

        # print(decodedfinal)
        print(decodedfinal.lower())
        f2.write(decodedfinal.lower() + '\n')

    f1.close()
    f2.close()


def main():
    quitted = False
    while not quitted:
        print("Menu commands:")
        print("e inputfile outputfile: Encodes inputfile into Morse Code and writes the encoding in outputfile.")
        print("d inputfile outputfile: Translates inputfile from Morse Code to its actual text and writes the "
              "translation in output file.")
        print("c inputfile: Compares the length of ASCII Code Representation of the text in inputfile to that of Morse "
              "Code representation of text in the inputfile")
        print("q: Quits the program")
        command = input("Enter command: ")
        words = command.split()
        if words[0] == "e":
            inputfile = str(words[1]) + ".txt"
            outputfile = str(words[2]) + ".txt"
            encode(inputfile, outputfile)

        elif words[0] == "d":
            inputfile = str(words[1]) + ".txt"
            outputfile = str(words[2]) + ".txt"
            decode(inputfile, outputfile)

        elif words[0] == "c":
            inputfile = str(words[1]) + ".txt"
            encode(inputfile, "comparison.txt")
            morse_length = number_of_characters("comparison.txt")
            write_ascii(inputfile, "comparison.txt")
            ascii_length = number_of_characters("comparison.txt")
            print("Length of ASCII Encoding of " + inputfile + ": " + str(ascii_length))
            print("Length of Morse Encoding of " + inputfile + ": " + str(morse_length))

        elif words[0] == "q":
            quitted = True
        else:
            print("Invalid Command.")


if __name__ == "__main__":
    main()
