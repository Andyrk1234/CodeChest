import re

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    p = re.compile("(([a-z]*[A-Z]+[a-z]*)+|([A-Z]+[a-z]*))+")
    password = re.findall(p, S)
    
    if len(password) > 0:
        # print password.group(1)
        array = [x[0] for x in password]
        array.sort(key = len)
        array.reverse()
        return len(array[0])
    else:
        return -1
        
print solution("a0bchdhhD091abcbddDdhdhdqQ")
