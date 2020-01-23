# Solution 1
# O(n) time O(n) space

def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)

# helper that uses unicode val to get the new letter.
# rememeber: 122 is last letter z, 96 is a. 26 letters in alphabet
def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122
    else chr(96 + newLetterCode % 122)


# Solution 2
# O(n) time O(n) space

def caesarCipherEncryptor(string, key):
    newletters = []
    newKey = key % 26
    alphabet = list("abcdefhijklmnopqrstuvwxyz")
    for letter in string:
        newletters.append(getNewLetter, newKey, alphabet)
    return "".join(newletters)

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode <= 25
    else alphabet[-1 + newLetterCode % 25]