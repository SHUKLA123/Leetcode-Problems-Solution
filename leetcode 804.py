# Problem Id : 804 Problem Statement: Unique Morse Code Words

# Description : Return the number of different transformations among all words we have.

words = ["gin", "zen", "gig", "msg"]

def uniqueMorseRepresentations(words):
    d = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    l = []
    for i in words:
        i = i.lower()
        s = ""
        for j in i:
            if j == " ":
                s = s + " "
            else:
                s = s + d[j]
        l.append(s)
    return len(set(l))

print(uniqueMorseRepresentations(words))