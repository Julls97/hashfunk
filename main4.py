from collections import namedtuple

text = "кириллова"
# text = "код"
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def d1():
    print("Тайные многосторонние вычисления")
    Key = namedtuple("Key", "e n d")
    Director = Key(e=5, n=91, d=29)
    Secretary = Key(e=7, n=91, d=31)
    Cleaner = Key(e=17, n=91, d=17)

    Director_salary = alphabet.find(text[0]) + 1
    Secretary_salary = alphabet.find(text[1]) + 1
    Cleaner_salary = alphabet.find(text[2]) + 1

    print(Director_salary, Secretary_salary, Cleaner_salary)

    x = 3

    c_encode = pow(Cleaner_salary + x, Secretary.e, Secretary.n)
    # print(c_encode)
    s_decode = pow(c_encode, Secretary.d, Secretary.n)
    # print(s_decode)
    s_encode = pow(Secretary_salary + s_decode, Director.e, Director.n)
    # print(s_encode)
    d_decode = pow(s_encode, Director.d, Director.n)
    # print(d_decode)
    d_encode = pow(Director_salary + d_decode, Cleaner.e, Cleaner.n)
    # print(d_encode)
    c_decode = pow(d_encode, Cleaner.e, Cleaner.n)
    # print(c_decode)
    avg_salary = (c_decode - x) / 3
    print("Средняя зарплата =", avg_salary)


def text_to_bin(text, list):
    for letter in text:
        bin_code = bin(int(letter.encode("Windows-1251").hex(), 16))[2:].zfill(8)
        list.append([letter, bin_code])


def bin_to_text(list):
    letters = []
    for item in list:
        letter = int(item[1], 2).to_bytes(1, 'little').decode("Windows-1251")
        letters.append(letter)
    return letters


gamma1_codes = []
gamma2_codes = []
gamma3_codes = []


def encode(codes):
    result = []
    for i in range(0, len(codes)):
        buff = ''
        for j in range(0, len(codes[0][1])):
            a0 = int(codes[i][1][j])
            a1 = int(gamma1_codes[i][1][j])
            a2 = int(gamma2_codes[i][1][j])
            a3 = int(gamma3_codes[i][1][j])
            a = (a0 + a1 + a2 + a3) % 2
            if a == 0:
                buff += '0'
            else:
                buff += '1'
        result.append([i, buff])
    return result


def d2():
    print("Разбиение секрета с использование гаммирования")

    secret = text[:3]
    print("Кодирование секрета – слово '", secret, "'")
    gamma1 = 'юля'
    gamma2 = 'шар'
    gamma3 = 'сук'

    secret_codes = []

    text_to_bin(secret, secret_codes)
    text_to_bin(gamma1, gamma1_codes)
    text_to_bin(gamma2, gamma2_codes)
    text_to_bin(gamma3, gamma3_codes)

    # print(tabulate(secret_codes, []))
    # print(tabulate(gamma1_codes, []))
    # print(tabulate(gamma2_codes, []))
    # print(tabulate(gamma3_codes, []))

    cipher = encode(secret_codes)
    # print(cipher)
    decode = encode(cipher)
    # print(decode)
    letters = bin_to_text(decode)
    print("Восстановленное слово -", ''.join(letters))


# import lagrange
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial


def d3():
    print("Разделение секрета по схеме Шамира")
    S = alphabet.find(text[0]) + 1
    print("S =", S)
    # S = 11
    m = 3
    n = 5
    p = 59
    a1 = 23
    a2 = 10

    y = []
    for x in range(1, n + 1):
        y.append([x, (a2 * pow(x, 2) + a1 * x + S) % p])
    # print(y)

    poly = lagrange([y[1][0], y[2][0], y[4][0]], [y[1][1], y[2][1], y[4][1]])
    S_ = int(Polynomial(poly).coef[2]) % p
    print("S_ =", S_)
    print("ok") if S == S_ else print("not ok")


def d4():
    print("Разделение секрета по схеме Асмута-Блума")
    # S = 11
    S = alphabet.find(text[0]) + 1
    print("S =", S)
    m = 3
    n = 5
    p = 13
    d = [17, 20, 23, 29, 37]

    r = 30
    if r > (d[0] * d[1] * d[3] - S) / p:
        print("Wrong r")
        return False

    S_ = S + r * p
    # print("S_ =", S_)

    y = []
    for i in range(0, len(d)):
        y.append([d[i], S_ % d[i]])
    # print(y)
    D = d[1] * d[2] * d[4]
    # print(D)
    D_ = [D / d[1], D / d[2], D / d[4]]
    # print(D_)
    D_invert = [11, 6, 7]

    S_ = (y[1][1] * D_[0] * D_invert[0] + y[2][1] * D_[1] * D_invert[1] + y[4][1] * D_[2] * D_invert[2]) % D
    print("S_ % p =", S_ % p)
    print("ok") if S == S_ % p else print("not ok")


d4()
