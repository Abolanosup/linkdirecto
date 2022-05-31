import random


def crypt_char(char):
    map = '@./=#$%&:,;_-|0123456789abcd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0
    for ch in map:
        if ch == char:
            return map[len(map) - 1 - i]
        i+=1
    return char

def encrypt(text):
    i = 0
    cryptText = ''
    for char in text:
        rnd = random.randrange(1,9,1)
        cryptText += crypt_char(char) + crypt_char(str(rnd))
        i+=1
    return cryptText

def decrypt(text):
    i = 0
    decryptText = ''
    while i < len(text):
        decryptText += crypt_char(text[i])
        i+=2
    return decryptText


def tokenize(args):
    token = ''
    i=0
    for item in args:
        end = ''
        if i<len(args)-1:
           end = '|'
        token += encrypt(str(item)+end)
        i+=1
    return token

def parsetoken(token):
    patoken = decrypt(token)
    return str(patoken).split('|')


#token = tokenize(['obysoft','Obysoft2001@'])
#data = parsetoken(token)
#print('finish')
#proxy = encrypt('152.206.201.33:4545')
#print(proxy)