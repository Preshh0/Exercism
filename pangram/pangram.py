'''
#Wrong Code
def is_pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for word in alphabet:
        if word == alphabets:
            return True
        else:
            return False
'''       


def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True
