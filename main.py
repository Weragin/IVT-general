from EXCEPT import EXCEPT

fzvo = ["P","L", "C", "H","F"]
jozo = fzvo[1:3]


def pal2(str):

    try:
        if str == str[::-1]:
            return True
        return False
    except TypeError:
        return EXCEPT(str)


print(pal2(3.1415926536))
