import re

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    p = re.compile("(([a-z]*[A-Z]+[a-z]*)+|([A-Z]+[a-z]*))+")
    password = p.search(S)

    if password != None:
        return len(password.group(1))
    else:
        return -1
        

print solution("a0bchdhhD")