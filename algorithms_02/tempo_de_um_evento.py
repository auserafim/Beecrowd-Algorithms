def main():
    d = int(input().split()[1])
    h, m, s = map(int, input().split(" : "))
    dm = int(input().split()[1])
    hh, mm, ss = map(int, input().split(" : "))

    s = ss - s
    m = mm - m
    h = hh - h
    d = dm - d

    if s < 0:
        s += 60
        m -= 1

    if m < 0:
        m += 60
        h -= 1

    if h < 0:
        h += 24
        d -= 1

    print("{} dia(s)".format(d))
    print("{} hora(s)".format(h))
    print("{} minuto(s)".format(m))
    print("{} segundo(s)".format(s))
main()
