def a1():
    print("алгоритм RSA")
    e = 5
    n = 91
    d = 29

    k = 11
    r = pow(k, e) % n
    # print(r)
    new_k = pow(r, d) % n
    # print(new_k)
    print("ok") if k == new_k else print("not ok")


def a2():
    print("алгоритм Клауса Шнорра")
    p = 23
    q = 11
    x = 8
    g = 3
    y = 4
    k = 10
    r = pow(g, k) % p
    # print(r)
    e = 4
    s = (k + x * e) % q
    # print(s)
    new_r = (pow(g, s) * pow(y, e)) % p
    # print(new_r)
    print("ok") if r == new_r else print("not ok")


def a3():
    import random
    print("алгоритм Клауса Шнорра")
    p = 5
    q = 7
    n = 35
    v = 16
    s = 9
    r = 18
    z = pow(r, 2) % n
    # print(z)
    b = random.randint(0, 1)
    if b != 0:
        y = (r * s) % n
        # print(y)
        new_z = (pow(y, 2) * v) % n
    else:
        new_z = pow(r, 2) % n
    # print(new_z)
    print("ok") if z == new_z else print("not ok")
