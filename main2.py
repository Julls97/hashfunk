def b1():
    print("Протокол на базе алгоритма RSA")
    e = 5
    n = 91
    d = 29
    h = 11
    s = pow(h, d, n)
    print(s)
    new_h = pow(s, e, n)
    print("ok") if h == new_h else print("not ok")


def b2():
    print("ГОСТ 34.10-94")
    p = 79
    q = 13
    a = 8
    x = 4
    y = pow(a, x, p)
    h = 10
    k = 11
    w = pow(a, k, p)
    w_ = w % q
    s = (x * w_ + k * h) % q
    print("s = ", s)
    v = pow(h, q - 2, q)
    print("v = ", v)
    z1 = (s * v) % q
    print("z1 = ", z1)
    z2 = ((q - w_) * v) % q
    print("z2 = ", z2)
    u = ((pow(a, z1) * pow(y, z2)) % p) % q
    print("u = ", u)
    print("ok") if w_ == u else print("not ok")


##################################################################################
# from collections import namedtuple
# Point = namedtuple("Point", "x y")
#
# P = Point(7, 17)
# Q = Point(36, 20)
#
# p = 15733
#
# dydx = (Q.y - P.y) * pow(Q.x - P.x, p-2, p)
# x = (dydx**2 - P.x - Q.x) % p
# y = (dydx * (P.x - x) - P.y) % p
# result = Point(x, y)
# print(result)

##################################################################################
def pk(x, y, A, B, n, k):
    λ = ((3 * x * x + A) // (2 * y)) % n
    xi = (λ * λ - 2 * x) % n
    yi = (λ * (xi - x) - y) % n
    for i in range(k):
        if (xi - x == 0): break

        λi = (yi - y // xi - x) % n
        xi = (λi * λi - x - xi) % n
        yi = (λi * (x - xi) - y) % n
    return xi, yi


def b3():
    print("ГОСТ 34.10-2001")
    h = 18  # беру свою цифру 3 буквы
    n = 10  # hz
    q = 47
    e = h % q
    print("e = ", e)
    k = 11
    x_c, y_c = pk(7, 17, 3, 7, 10, 11)  ######################################### вот тут мне не понятно как делать
    r = x_c % q
    s = (r * d + k * e) % q
    print("s = ", s)

    v = h % q
    print("v = ", v)
    z1 = (s * v) % q
    print("z1 = ", z1)
    z2 = ((q - r) * v) % q
    print("z2 = ", z2)
    x_c_, y_c = pk()  #########################################
    r_ = x_c_ % q
    print("r_ = ", r_)
    print("ok") if r == r_ else print("not ok")
