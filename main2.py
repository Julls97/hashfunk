import random

text = "кириллова"
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

from collections import namedtuple

Point = namedtuple("Point", "x y")

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def b1():
    print("Протокол на базе алгоритма RSA")

    PublicKey = namedtuple("PublicKey", "e n")
    PrivateKey = namedtuple("PrivateKey", "d")

    Key = PublicKey(5, 91)
    KeyC = PrivateKey(29)

    # h - исходное сообщение, h = 12
    h = alphabet.find(text[0]) + 1
    print("Исходное сообщение h =", h)

    # Выработка цифровой подписи s = hd mod n, где
    # d – закрытый ключ отправителя A, n – часть открытого ключа отправителя A.
    s = pow(h, KeyC.d, Key.n)
    print("Цифровая подпись s =", s)

    # Вычисление хеш-образа из цифровой подписи h = se mod n, где e и n – открытый ключ отправителя A.
    h_ = pow(s, Key.e, Key.n)
    print("Полученное сообщение h =", h)

    print("ok") if h == h_ else print("not ok")

def b2():
    print("ГОСТ 34.10-94")

    PbKey = namedtuple("PublicKey", "p q a")
    PPbKey = namedtuple("PersonalPublicKey", "y")
    PrKey = namedtuple("PrivateKey", "x")

    PbKey = PbKey(79, 13, 8)

    # Выбор закрытого ключа х - числа, меньшего q, x = 4
    x = random.randint(0, PbKey.q)
    PrKey = PrKey(x)

    # y - персональный открытый ключ для одного пользователя, y = 67
    y = pow(PbKey.a, x, PbKey.p)
    PPbKey = PPbKey(y)

    # Вычисление хеш-образа h, h = 10
    h = alphabet.find(text[1]) + 1
    # print("h = ", h)

    s = 0
    while s == 0:
        w_ = 0
        while w_ == 0:
            # Выбор k - любого числа, меньшего q, k = 11
            k = random.randint(0, PbKey.q)

            w = pow(PbKey.a, k, PbKey.p)
            w_ = w % PbKey.q
        s = (x * w_ + k * h) % PbKey.q

    # print("w_ = ", w_)
    # print("s = ", s)

    v = pow(h, PbKey.q - 2, PbKey.q)
    # print("v = ", v)
    z1 = (s * v) % PbKey.q
    # print("z1 = ", z1)
    z2 = ((PbKey.q - w_) * v) % PbKey.q
    # print("z2 = ", z2)
    u = ((pow(PbKey.a, z1) * pow(y, z2)) % PbKey.p) % PbKey.q
    # print("u = ", u)
    print("ok") if w_ == u else print("not ok")


def generatorPKey():
    Key = namedtuple("Key", "A B P Q n q d")
    n = 41
    # n = random.choice(prime_numbers)
    A = 3
    B = 7
    P = Point(7, 17)
    q = 47
    # q = random.choice(prime_numbers)
    d = random.randint(0, q)
    # print("d =", d)
    Q = ec_mult(P, d, A, n)
    # print("Q =", Q)
    PKey = Key(A, B, P, Q, n, q, d)
    return PKey


def inv_mod_p(x, n):
    return pow(x, n - 2, n)


def ec_add(P, Q, A, n):
    if P == Q:
        dydx = (3 * P.x ** 2 + A) * inv_mod_p(2 * P.y, n)
    else:
        dydx = (Q.y - P.y) * inv_mod_p(Q.x - P.x, n)

    x = (dydx ** 2 - P.x - Q.x) % n
    y = (dydx * (P.x - x) - P.y) % n
    result = Point(x, y)
    return result


def ec_mult(P, x, A, n):
    for i in range(1, x + 1):
        if i == 1:
            R = P
        else:
            R = ec_add(R, P, A, n)
    return R

def b3():
    print("ГОСТ 34.10-2001")
    h = alphabet.find(text[2]) + 1
    # h = 7
    print("h = ", h)

    Key = generatorPKey()

    # Вычисление e = h mod q, где q – часть открытого ключа отправителя A, q = 47
    e = h % Key.q
    # print("e = ", e)

    s = 0
    # Если s = 0, выбрать другое значение числа k.
    while s == 0:
        r = 0
        # Если r = 0, выбрать другое значение числа k.
        while r == 0:
            # Выбор k - любого числа, меньшего q
            k = random.randint(0, Key.q)

            # Определение точки эллиптической кривой C(xc, yc) = k*P(xp, yp),
            # где P(xp, yp) – часть открытого ключа отправителя A
            C = ec_mult(Key.P, k, Key.A, Key.n)

            r = C.x % Key.q

        s = (r * Key.d + k * e) % Key.q

    # print("k =", k)
    # print("C =", C)
    # print("s = ", s)
    print("r = ", r)

    v = mulinv(e, Key.q)
    # print("v =", v)
    z1 = (s * v) % Key.q
    # print("z1 = ", z1)
    z2 = ((Key.q - r) * v) % Key.q
    # print("z2 = ", z2)

    # Определение точки эллиптической кривой C’(xc’, yc’) = z1 P(xp, yp) + z2 Q(xq, yq),
    # где Q(xq, yq) – часть открытого ключа отправителя A.
    P_ = ec_mult(Key.P, z1, Key.A, Key.n)
    Q_ = ec_mult(Key.Q, z2, Key.A, Key.n)
    C_ = ec_add(P_, Q_, Key.A, Key.n)
    # print("C_ =", C_)

    r_ = C_.x % Key.q
    print("r_ = ", r_)

    print("ok") if r == r_ else print("not ok")


def mulinv(a, b):
    # return x such that (x * a) % b == 1
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b


def xgcd(a, b):
    # return (g, x, y) such that a*x + b*y = g = gcd(a, b)
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


b3()
