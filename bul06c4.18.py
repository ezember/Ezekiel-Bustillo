""" EZEKIEL BUSTILLO
    DATALGO Lab06
    Mar. 4, 2020
    I have neither received nor provided any help on this (lab) activity,
    nor have I concealed any violation of the Honor Code.
"""


def Vowels(letters):
    return letters.upper() in ['A', 'E', 'I', 'O', 'U']
def NoVowels(s, n):
    if (n == 1):
        return Vowels(s[n - 1])
    return (NoVowels(s, n - 1) + Vowels(s[n - 1]))

def Consonants(letters):
    letters = letters.upper()
    return not (letters == 'A' or letters == 'E'or letters == 'I'or letters == 'O'or letters == 'U')

def NoConsonants(s, n):
    if (n == 1):
        return Consonants(s[0])
    return NoConsonants(s, n - 1) + Consonants(s[n - 1])



s="EZEKIEL BUSTILLOOOOO"

print("The Word is: ",s)
if (NoConsonants(s, len(s))) > (NoVowels(s, len(s))):
    print("The Word Has Lesser Vowels Than Consonants")
else:
    print("The Word Has More Vowels Than Consonants")
