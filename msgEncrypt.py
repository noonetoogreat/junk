#--------------------
#Code Written by Kidd
#--------------------

def caesars(clearText,key):      #caesar's encryption
    i = 0
    cipher = ""
    x = len(key)
    for letter in clearText:
        if(i >= x):
            i = 0
        cipher += chr(ord(letter) + ord(key[i]))
        i = i + 1
    return cipher

def caesars_decrypt(cipherText,key):      #caesar's decryption
    i = 0
    clear = ""
    x = len(key)
    for letter in cipherText:
        if(i >= x):
            i = 0
        clear += chr(ord(letter) - ord(key[i]))
        i = i + 1
    return clear

# function calls

inEmail = raw_input('[*] Enter the message content of the email. [*]\n')
passPhrase = raw_input('[*] Enter the passphrase [*]\n')

cipherText = caesars(inEmail,passPhrase)
print cipherText

decryptText = caesars_decrypt(cipherText,passPhrase)
print decryptText
