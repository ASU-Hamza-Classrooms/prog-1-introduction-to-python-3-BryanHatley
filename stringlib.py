#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#

def reverseStr(s):
    return s[::-1]

def containsWord(containingStr, containedStr):
    if containedStr in containingStr:
        return "Yes"
    else:
        return "No"

def isPalindrome(s):
    sl = s.lower()
    p = sl[::-1]
    if p in sl:
        return "Yes"
    else:
        return "No"

def upperCaseStr(s):
    return s.upper()