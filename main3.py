from tabulate import tabulate

text = "кириллова"
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
code_line = ''

def generate_code_line():
    global code_line
    for char in text:
        item = alphabet.find(char) + 1
        # print(item)
        code_line += str(item)

def c1():
    print("Биты четности")
    result = []
    for char in text:
        bin_char = bin(int(char.encode("Windows-1251").hex(), 16))[2:].zfill(8)
        # print(bin_char)
        count_1 = 0
        for bit in bin_char:
            if bit == "1":
                count_1 += 1
        result.append([char, bin_char, "1" if count_1 % 2 == 1 else "0", "1" if count_1 % 2 == 0 else "0"])

    print(tabulate(result, ["Буква", "Битовая строка", "Четный бит", "Нечетный бит"]))

def c2():
    print("Использование контрольных цифр. Луна")
    global code_line
    generate_code_line()
    # code_line = '2758620842000213'
    print("Исходный код", code_line)

    s1 = 0
    s2 = 0
    for x in range(0, len(code_line) - 1, 2):
        # print(code_line[x], " ", code_line[x+1])
        s1 += (int(code_line[x]) * 2) % 9
        s2 += int(code_line[x + 1])
    s2 -= int(code_line[len(code_line) - 1])
    # print("s1 =", s1)
    # print("s2 =", s2)
    cd = 10 - ((s1 + s2) % 10) % 10
    print("Контрольная цифра", cd)

def c3():
    print("Штрихкод по стандарту EAN - 13")
    global code_line
    generate_code_line()
    res = code_line[:13]
    # res = '5901234123457'
    print("Исходный код", res)

    s1 = 0
    s2 = 0
    for x in range(1, len(res), 2):
        # print(res[x - 1], " ", res[x])
        s1 += int(res[x - 1])
        # print(int(res[x - 1]))
        s2 += int(res[x]) * 3
        # print(int(res[x]))
    # print("s1 =", s1)
    # print("s2 =", s2)
    c = int(res[len(res) - 1])
    cd = 10 - ((s1 + s2) % 10) % 10
    print("Контрольная цифра", cd)

def c4():
    print("ИНН физического лица")
    global code_line
    generate_code_line()
    n = code_line[:12]
    print("Исходный код", n)

    r11 = 7 * int(n[0]) + 2 * int(n[1]) + 4 * int(n[2]) + 10 * int(n[3]) + 3 * int(n[4]) + 5 * int(n[5]) + 9 * int(
        n[6]) + 4 * int(n[7]) + 6 * int(n[8]) + 8 * int(n[9])
    # print(r11)
    n11 = (r11 % 11) % 10

    r12 = 3 * int(n[0]) + 7 * int(n[1]) + 2 * int(n[2]) + 4 * int(n[3]) + 10 * int(n[4]) + 3 * int(n[5]) + 5 * int(
        n[6]) + 9 * int(n[7]) + 4 * int(n[8]) + 6 * int(n[9]) + 8 * int(n[10])
    # print(r12)
    n12 = (r12 % 11) % 10

    print("Контрольная цифра n11", n11)
    print("Контрольная цифра n12", n12)

def c5():
    print("Коды станций на железнодорожном транспорте")
    global code_line
    generate_code_line()
    n = code_line[:6]
    n = '970406'
    print("Исходный код", n)

    j = 1
    n6 = c5_res(j, n)
    # print(n6)

    if n6 < 10:
        r = n6
    else:
        j = j + 2
        n6 = c5_res(j, n)
        if n6 == 10:
            r = 0
        else:
            r = n6
    print("Контрольная цифра", r)

def c5_res(j, n):
    x = 0
    for i in range(0, len(n) - 1, 1):
        x += (i + j) * int(n[i])
    return x % 11

def c6():
    print("Контрольные суммы (checksums или CRC)")
    global code_line
    generate_code_line()
    P = bin(int(code_line[:6]))[2:]
    # P = '10111'
    print("Делимое P(x)(входные данные)", P)
    n = 4
    R = P + "0" * n
    print("P(x) * xN", R)
    G = '10011'

    while len(R) >= len(G):
        for i in range(0, len(G), 1):
            R = R[:i] + str(int(R[i]) ^ int(G[i])) + R[i + 1:]
        while len(R) > 0 and R[0] == '0':
            R = R[1:]
    while len(R) != (len(G) - 1):
        R += '0'

    print("Остаток R(x)(контрольная сумма)", R)

def c7():
    print("Код коррекции ошибок (ECC)")

    x = (bin(int(text[0].encode("Windows-1251").hex(), 16))[2:] + bin(int(text[1].encode("Windows-1251").hex(), 16))[
                                                                  2:])[:11]
    # x = '10010010111'
    print('x =', x)
    XR = [int(i) for i in x]
    print('XR =', XR)

    for i in range(4):
        XR.insert(pow(2, i) - 1, 0)
    print('XR =', XR)

    N = []
    for i in range(len(XR)):
        N.append(bin(i + 1)[2:].zfill(4)[::-1])
    print('N =', N)

    r = multMatrix(XR, N)
    print('r =', r)

    XR1 = [int(i) for i in x]
    for i in range(4):
        XR1.insert(pow(2, i) - 1, r[i])
    print('XR1 =', XR1)

    pb = PB(XR1)
    print('pb =', pb)

    s = multMatrix(XR1, N)
    print('s =', s)
    print('pb` =', PB(XR1))
    print('Ошибок нет') if (pb == PB(XR1) and sum(s) == 0) else print('Ошибки есть')

    import random
    rand = random.randint(0, len(XR) - 1)
    if XR1[rand] == 0:
        XR1[rand] = 1
    else:
        XR1[rand] = 0
    s = multMatrix(XR1, N)
    print('s =', s)
    print('pb` =', PB(XR1))
    print('Ошибок нет') if (pb == PB(XR1) and sum(s) == 0) else print('Одиночная исправимая ошибка')
    binary = ''.join(map(str, s))[::-1]
    error = int(binary, 2)
    print("Номер ошибочного бита", error)

    rand1 = random.randint(0, len(XR) - 1)
    while rand == rand1:
        rand1 = random.randint(0, len(XR) - 1)
    if XR1[rand1] == 0:
        XR1[rand1] = 1
    else:
        XR1[rand1] = 0
    s = multMatrix(XR1, N)
    print('s =', s)
    print('pb` =', PB(XR1))
    print('Ошибок нет') if (pb == PB(XR1) and sum(s) == 0) else print(
        'Двойная неисправимая ошибка. Ошибки невозможно исправить')


def PB(XR):
    pb = sum(XR) % 2
    return pb


def multMatrix(XR, N):
    result = []
    for i in range(len(N[0])):
        buff = 0
        for j in range(len(N)):
            buff += XR[j] * int(N[j][i])
        result.append(buff % 2)
    return result


c7()
