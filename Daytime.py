def angle(time, start=360, end=1080):
    a, b = time.split(":")
    a = int(a)
    b = int(b)
    now = 60 * a + b

    if start < 0 or end > 1440 or start > end or now < 0 or now > 1440:
        raise ValueError
    if now < start or now > end:
        return ("It's night")
    return "The angle of sun above the start is " + str((now - start) / (end - start) * 180) + " degrees."


print(angle("9:10", 0, 900))


def angle2(time):
    h, m = time.split(":")
    m = int(m)
    h = int(h)

    h -= 12 * (h > 12)

    ang_m = m * 6
    ang_h = (h + m / 60) * 30

    return abs(ang_m - ang_h)


print(angle2("13:00"))
