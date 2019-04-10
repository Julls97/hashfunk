import random
import re
from itertools import starmap, cycle

alphabet = 'abcdefghijklmnopqrstuvwxyz'
lenght = len(alphabet)

dictionary = [
    "over",
    "the",
    "lazy",
    "dogs",
    "apple",
    "avocado",
    "akee",
    "araza",
    "alibertia",
    "apricot",
    "blueberry",
    "blackberry",
    "barberry",
    "banana",
    "bignay",
    "biriba",
    "breadfruit",
    "bilberry",
    "boysenberry",
    "balckcurrant",
    "champedak",
    "chalta",
    "calabash",
    "clementine",
    "cherry",
    "cantaloupe",
    "casaba",
    "crenshaw",
    "charantais",
    "cranberry",
    "currants",
    "cucumber",
    "date",
    "durian",
    "feijoa",
    "fig",
    "gandaria",
    "genipap",
    "granadilla",
    "guava",
    "grapefruit",
    "galia",
    "pepper",
    "grape",
    "hogplum",
    "honeydew",
    "jackfruit",
    "jaboticaba",
    "kepel",
    "ketupa",
    "kechapi",
    "kiwi",
    "kiwano",
    "kumquat",
    "lychee",
    "loquat",
    "lucuma",
    "lemon",
    "lime",
    "loganberry",
    "mango",
    "melon",
    "sapote",
    "morinda",
    "mangosteen",
    "mandarin",
    "bread",
    "minneola",
    "nance",
    "nangka",
    "nectarine",
    "gooseberry",
    "orange",
    "olive",
    "pineapple",
    "persimmon",
    "papaya",
    "roseapple",
    "pitahaya",
    "pomegranate",
    "pummelo",
    "pear",
    "plum",
    "peach",
    "quince",
    "rambutan",
    "rambai",
    "raspberry",
    "sansapote",
    "nut",
    "soncoya",
    "sweetsop",
    "soursop",
    "fruit",
    "sala",
    "salak",
    "santoli",
    "sapodilla",
    "satsuma",
    "sharlyn",
    "strawberry",
    "satsuma",
    "tangerine",
    "tangelo",
    "tomato",
    "ugli",
    "voavanga",
    "tamarind",
    "watermelon",
    "xigua",
    "zuchini"
]

a = ord('a')
z = ord('z')
space = ord(' ')


def vigenere_encipherment(message, key):
    # message = filter(str.isalpha, message.upper())
    message = re.sub('[!?;:,]', '', message)

    def enc(c, k):
        return chr(((ord(k) + ord(c) - 2 * ord('A')) % 26) + ord('A'))

    return message_decipherment(enc, key, message)
    # return ' '.join(starmap(enc, zip(list[0], cycle(key))))


def message_decipherment(func, key, message):
    list = re.split(r'\s', message.upper())
    res = []
    for word in list:
        new_word = ''.join(starmap(func, zip(word, cycle(key))))
        res.append(new_word)
    return ' '.join(res)


def vigenere_decipherment(message):
    def dec(c, k):
        return chr(((ord(c) - ord(k) - 2 * ord('A')) % 26) + ord('A'))

    # return ''.join(starmap(dec, zip(message, cycle(key))))
    for key in dictionary:
        isFind = True
        # new_string = ' '.join(starmap(dec, zip(message, cycle(key))))
        new_string = message_decipherment(dec, key, message)
        list = re.split(r'\s', new_string.lower())
        for word in list:
            if word not in dictionary:
                isFind = False
                break
        if isFind: break
    if not isFind: return 'No matches found. Try another decipherment.'
    res = ' '.join(list)
    print('key = ', key)
    return res


def caesar_decipherment(string):
    for i in range(0, lenght):
        isFind = True
        new_string = caesar(string, i)
        # print(new_string)
        list = re.split(r'\s', new_string)
        for word in list:
            if word not in dictionary:
                isFind = False
                break
        if isFind: break
    if not isFind: return 'No matches found. Try another decipherment.'
    res = ' '.join(list)
    return res


def caesar(string, shift, decode=True):
    if decode: shift = lenght - shift
    res = ''
    for i in string:
        if ord(i) == space:
            res += i
        if ord(i) >= a and ord(i) <= z:
            res += chr((ord(i) - a + shift) % lenght + a)
    return res


# input_string = input()
input_string = 'over the lazy dogs'
n = random.randint(0, 1)
if n:
    string = caesar(input_string, 13, False)
else:
    key = random.choice(dictionary)
    print('vigenere key =', key)
    string = vigenere_encipherment(input_string, key)

print('input string =', string.lower())
res = caesar_decipherment(string)
print('caesar:', res)
res1 = vigenere_decipherment(string)
print('vigenere:', res1)
