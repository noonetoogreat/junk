#--------------------
#Code Written by Kidd
#--------------------

import itertools
import string


def switch(ch):     #switch case to decide type of passwords
    if(ch == 1):
        passLet = string.ascii_uppercase
    elif(ch == 2):
        passLet = string.ascii_lowercase
    elif(ch == 3):
        passLet = string.digits
    elif(ch == 4):
        passLet = "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
    elif(ch == 5):
        passLet = string.ascii_lowercase + "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
    elif(ch == 6):
        passLet = string.ascii_uppercase + "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
    elif(ch == 7):
        passLet = string.ascii_lowercase + ascii.digits
    elif(ch == 8):
        passLet = string.ascii_uppercase + ascii.digits
    elif(ch == 9):
        passLet = string.ascii_digits + "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
    elif(ch == 10):
        passLet = string.ascii_leters
    elif(ch == 11):
        passLet = string.digits + string.ascii_letters
    elif(ch == 12):
        passLet = string.ascii_letters + "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
    elif(ch == 13):
        passLet = string.ascii_lowercase + ascii.digits+ "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
    elif(ch == 14):
        passLet = string.ascii_uppercase + ascii.digits + "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
    elif(ch == 15):
        passLet = string.digits + string.ascii_letters + "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"
    return passLet

def writeToWordlist(password):      #write all to file
    foo = open('wordlist.txt', 'a+')
    foo.write(password +'\n')
    foo.close()
    return

def genpass(passCharStr,n):  #generate the passwords
    res = itertools.product(passCharStr,repeat=n)
    for i in res: 
       password = ''.join(i)
       print password
       writeToWordlist(password)
    return

# function calls

print "\t\t[*] Menu  [*]"
print "-----Loners [n = 1]-------"
print "1.Only Uppercase"
print "2.Only Lowercase"
print "3.Only Digits"
print "4.Only Symbols"
print "-----Couples [n = 2]-------"
print "5.Lowercase and Symbols"
print "6.Uppercase and Symbols"
print "7.Lowercase and digits"
print "8.Uppercase and digits"
print "9.Digits and Symbols"
print "10.Uppercase and Lowercase"
print "-----Cheaters [n = 3]-------"
print "11.Uppercase,Lowercase and Digits"
print "12.Uppercase,Lowercase and Symbols"
print "13.lower,digits and Symbols"
print "14.Uppercase,digits and Symbols"
print "-----Groupies [n = 4]-------"
print "15.Uppercase,Lowercase,Digits and Symbols"

choice = input('Enter your choice : ')
passLetters = switch(choice)
passSize = input('Enter the size of the password : ')
genpass(passLetters,passSize)


