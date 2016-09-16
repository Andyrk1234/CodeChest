__author__ = 'Paarth Bhasin'
__title__ = "Assignment-1 FIT2070: Operating Systems"
__tutor__ = "Hasanul Ferdaus"
__StartDate__ = '22/8/2016'
__studentID__ = 26356104
__LastModified__ = '31/8/2016'


'''We import os and subprocess for us to able to run the linux commands from command line in python shell.'''

import os
import subprocess as sp
import sys
import psutil
import signal

'''
function: cmd_cd(path)

    Author: Paarth Bhasin

    Preconditions: Path to change has been provided as an argument to the function.

    Postconditions: The current working directory (cwd) is changed from what it currently is to the directory specifiied in the path
                    argument. If no path is provided, the cwd is changed to the home directory.


    VALID INPUTS: Any directory path that exists or any special symbol values for going up and down the cwd.

        Input: path = ../
        Output: The cwd goes one directory up.


        Input: path = ../../
        Output: Go two directories up from the cwd

        
        Input: path = .
        Output: Remain in the same directory

        Input: path = None
        Output: Go the home directory

    INVALID INPUTS: A path which doesn't exist would give an error.

        Input: path = %#$!%#$
        Output: The directory you want to change to does not exist

    COMPLEXITY:

        O(1), Best and Worst



function: cmd_clear()

    Author: Paarth Bhasin

    Preconditions: None

    Postconditions: The shell/terminal screen is cleared of any output.


    VALID INPUTS: all

    INVALID INPUTS: None


    COMPLEXTIY:

        O(1), Best and Worst



function: copy(file1, file2)

    Author: Paarth Bhasin

    Preconditions: file1 and file2 have been passed as an argument.

    Postconditions: Contents of file1 are written in file2. If file2 doesn't exist, it is created. If it exists and contains some data,
                    it is overwritten and the data is lost.


    VALID INPUTS: file1 is a text file and it exists, and file2 is a text file which may or may not exist.

        Inputs: file1 = readme.txt, file2 = abc.txt
        Output: Contents of readme.txt are written down in abc.txt

    INVALID INPUTS: file1 doesn't exist, or file2 is not a text file.

        Inputs: file1 = asdfghj.txt, file2 = abc.txt
        Output: asdfghj.txt doesn't exist

        Input: file1 = abc.txt, file2 = abc.hgte
        Output: Error opening file abc.hgte

    COMPLEXITY:

        Best Case: O(1), when function exits with an error message.
        Worst Case: O(N), where N is the number of lines in file1.



function: cmd_dir()

    Author: Paarth Bhasin

    Preconditions: None

    Postconditions: The contents of the current working directory are output.

    VALID INPUTS: all

    INVALID INPUTS: None

    COMPLEXTITY:
        O(1), Best and Worst



function: cmd_echo(words="")

    Author: Paarth Bhasin

    Preconditions: None

    Postconditions: The comment passed as an arugmument (if any) to the function, is output.

    VALID INPUTS: all

    INVALID INPUTS: None

    COMPLEXTITY:
        Best Case: O(1), if argument contains only one word
        Worst Case: O(N), where N is the number of words in the argument.



function: cmd_run(program)

    Author: Paarth Bhasin

    Preconditions: A program name is passed as an argument to this function, and is present in the current working directory.

    Postconditions: The program is run as a subprocess of this program.

    VALID INPUTS: A program which is present in the cwd.

        Input: program = readme.txt
        Output: readme.txt is run/opened, while CommandLine.py is running concurrently with it.

    INVALID INPUTS: A program which is not present in the cwd.

        Input: Program = ViceCity.exe
        Output: Error opening the ViceCity.exe


    COMPLEXTITY:

        Best Case: O(1)
        Worst Case: O(1)



function: cmd_quit()

    Author: Paarth Bhasin

    Preconditions: None

    Postconditions: CommandLine.py is terminated.

    VALID INPUTS: all

    INVALID INPUTS: None

    COMPLEXITY: O(1), Best and Worst.



function: cmd_halt(filename)

    Author: Paarth Bhasin

    Preconditions: filename is passed as an argument to the function

    Postconditions: Program 'filename' is terminated.

    VALID INPUTS: all

    INVALID INPUTS: None

    COMPLEXITY: 

        O(1), Best and Worst



function: cmd_find(char, file)

    Author: Paarth Bhasin

    Preconditions: char and file are passed as arguments

    Postconditions: The number of occurences of character char in filename file is output.

    VALID INPUTS: file is exists.

        Inputs: char = a, file = readme.txt
        Output: 80

    INVALID INPUTS: file does not exist.

        Input: char = a, file =asdfghj.txt
        Output: Error. File doesn't exist.

    COMPLEXITY:

        Best Case: O(1), when file doesn't exist and function exits with an error message.
        Worst Case: O(N), where N is the number of characters in file.



function: cmd_pause()

    Author: Paarth Bhasin

    Preconditions: None

    Postconditions: CommandLine.py is paused until Enter key is pressed.

    VALID INPUTS: all

    INVALID INPUTS None

    COMPELXITY:

        O(1), Best and Worst


function: cmd_create(filname)

    Author: Paarth Bhasin

    Preconditions: filename is passed as an argument and can be opened.

    Postconditions: File filename is created.

    VALID INPUTS: filename can be opened.

        Input: filename = abc.txt
        Output: abc.txt is created.

    INVALID INPUTS: filename cannot be opened.

        Input: filename = abc.jhk
        Output: abc.jhk cannot be opened.

    COMPLEXITY: 
        
        O(1), Best and Worst



function: cmd_help()

    Author: Paarth Bhasin

    Preconditions: None

    Postconditions: The user help file is output to stdout.

    VALID INPUTS: all

    INVALID INPUTS: None

    COMPLEXITY:
        
        O(N), Best and Worst, where N is the number of words in readme.txt



function: main()

    Author: Paarth Bhasin

    Preconditions: None

    Postconditions: A command is executed from the list of possible commands.

    VALID INPUTS: cd path(path should exist), run program(program should exist), help, quit, pause, halt program, dir, echo comment, new file, cp file1 file2, clear,
                  find char file.

        Input: cd /home/usr/Desktop/
        Output: cwd is changed to /home/usr/Desktop/

        Input: quit
        Output: CommandLine.py is terminated.

        Input: echo This program works.
        Output: This program works.

        Input: new file.txt
        Output: file.txt is created.

        Input: cp readme.txt abc.txt
        Output: Contents of readme.txt is written into abc.txt

        Input: clear
        Output: Shell screen is cleared.

    INVALID INPUTS: Invalid command or invalid argument of valid command.

        Input: ckd
        Output: Invalid Command

        Input: cd abc/ytyry/either
        Output: Directory doesn't exist.


    COMPLEXITY:

        O(1), Best and Worst

'''
def cmd_cd(path=""):
    if len(path) > 0:
        if os.path.exists(path):
            os.chdir(path)
            print("1")
            # print('\n')
        else:
            print("The directory you want to change to, doesn't exist.")
            print('\n')
    else:
        path = os.path.expanduser('~')
        os.chdir(path)
        print('\n')


# The .chdir(path) function takes us (changes ~ ch) from the current directory to the directory(~dir) provided in path.

def cmd_clear():
    sp.call('clear', shell=True)


# The .call('cls', shell=True) function of the module subprocess, clears the command line screen.

def copy(file1, file2):
    path = "./" + file1
    if not os.path.isfile(path): # Checking whether file1 exists.
        print(file1, end=" ")
        print("doesn't exist.")
    else:
        f1 = open(file1, 'r')
        lines = f1.readlines()
        f2 = open(file2, 'w')
        for line in lines:
            f2.write(line)
        f1.close()
        f2.close()


def cmd_dir():
    print(os.getcwd())
    path = os.getcwd() + '/'
    for files in os.listdir(path):
        print(files)
    print('\n')


# The .listdir(path) function of the os module, lists/prints all the directories/files present in the file whose
# path is represented by the 'path' argument.

def cmd_environ():
    for key in os.environ.keys():
        print("%30s %s \n" % (key, os.environ[key]))
    print('\n')


# The .environ.keys() function of the os module, holds all the environment keys. And the .environ[key] function
# of the os module, represents the name of each environment variable.


def cmd_echo(words=""):
    comment = ""
    for word in words:
        comment += word + " "
    print(comment)
    print('\n')


# This function simply prints the comment on the shell/command line output screen without using either of the two
# modules, viz. os and subprocess.


def cmd_run(filename):
    # os.execl(filename, "")
    # os.startfile(filename)
    opener ="open" # if sys.platform == "darwin" else "xdg-open"
    sp.call(['xdg-open', filename])
    # sp.Popen(filename)

# The .execl(filename) of the os module, runs the file named 'filename' in the current directory.


def cmd_quit():
    exit()


def cmd_halt(program):
    process = program
    
    pid = 0
 
    for line in os.popen("ps ax | grep " + process + " | grep -v grep"):
        # ^Taking all processes, finding the ones which have process in their name, and removing the process with name grep.
        fields = line.split()
        pid = fields[0]
        os.kill(int(pid), signal.SIGKILL)
        break


# This function simply exits the shell scripting program without using any of the two modules, viz: os and subprocess.

def find(char, file):
    f = open(file, 'r')
    path = "./" + file
    if not (os.path.isfile(path)):
        # ^Checking if file exists or not.
        print("Error. File doesn't exist.")
    else:
        count = 0
        lines = f.readlines()
        f.close()
        for line in lines:
            words = line.split()
            for word in words:
                for i in range(len(word)):
                    if word[i] == char:
                        count += 1
        print(count)


def cmd_pause():
    input("Press Enter to continue.")


# This function simply pauses the shell scripting program without using any of the two modules, viz: os and subprocess.

def cmd_create(file):
    f1 = open(file, 'w')
    f1.close()


def cmd_top(args):
    sp.call(args, shell=True)


# The .call("top") function of the subprocess module, runs the inbuilt top program found in linux OS.

def cmd_help():
    path = os.getcwd()
    fin = open("readme.txt", 'r')
    pager = sp.Popen(['less'], stdin=fin, stdout=sys.stdout)
    # ^Uses the less program to display the user manual. We can also use more instead of less.
    pager.wait()
    # print('\n')


# The .getcwd() method of the os module returns the current working directory (cwd) of the process we are currently
# running and opens the readme.txt file in it, if it exists. Otherwise, it does nothing.


def main():
    quit = False

    while not quit:
        print("$-", end=" ")
        words = input().split()

        if words[0] == "cd":

            if len(words) > 1:
                path = ""
                pathlist = words[1:]
                for i in pathlist:
                    path += i 
                # ^Forming a path
                print(path)
                cmd_cd(path)
            else:
                cmd_cd()

        elif words[0] == "clear":
            cmd_clear()

        elif words[0] == "dir":
            cmd_dir()

        elif words[0] == "cp":
            file1 = "./" + words[1]
            file2 = "./" + words[2]
            # ^Making sure the files open up in the cwd.
            copy(file1, file2)

        elif words[0] == "environ":
            cmd_environ()

        elif words[0] == "new":
            file = words[1]
            cmd_create(file)

        elif words[0] == "echo":
            comment = words[1:]
            cmd_echo(comment)

        elif words[0] == "find":
            char = words[1]
            file = words[2]
            find(char, file)

        elif words[0] == "run":
            program = words[1]
            cmd_run(program)

        elif words[0] == "top":
            args = words[0]
            cmd_top(args)

        elif words[0] == "quit":
            quit = True
            cmd_quit()

        elif words[0] == "help":
            cmd_help()

        elif words[0] == "halt":
            program = words[1]
            cmd_halt(program)

        elif words[0] == "pause":
            cmd_pause()
        else:
            print("Invalid command")
            print('\n')


if __name__ == "__main__":

    # ^This line ensures that this program is being run from itself and not being run from some other file/not being
    # imported and run from some other file.
    main()
