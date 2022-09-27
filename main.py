import math


# funguje len z 10 na To, zatiaľ
def conversion(x, To, From=10):
    res = str(To) + "/"
    if To ** math.floor(math.log(x, To)) == x:
        return res + "1" + x * "0"

    for i in range(math.floor(math.log(x, To)), -1, -1):
        res += str(1 * (To ** i <= x))
        x -= To ** i * (To ** i <= x)
    return res


print(conversion(156, 2))


def to_dec(x, From):
    res = 0
    been = 0

    for i in x:
        been += 1 * (i == "/")
        i *= been
    x[0] = ""

    exp = len(x)  # exponent will immediately get decremented by one in for loop

    for i in x:
        exp -= 1  # the last digit would represent its value * base, not its value, if the decrement took place after
        res += int(x[i]) * From ** exp
    return res
