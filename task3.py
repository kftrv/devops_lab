def fun(a, b):
    c = bin(a ^ b)
    return c.count("1")


if __name__ == '__main__':
    print(fun(int(input()), int(input())))
