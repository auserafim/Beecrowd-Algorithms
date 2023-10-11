def main():
     i = 0.0
     j = 1.0

     while i <= 2.1:
        if i == 0.0 or i == 1.0 or i > 1.9:
            print("I={:.0f} J={:.0f}".format(i, j + i))
            print("I={:.0f} J={:.0f}".format(i, j + 1 + i))
            print("I={:.0f} J={:.0f}".format(i, j + 2 + i))
        else:
            print("I={:.1f} J={:.1f}".format(i, j + i))
            print("I={:.1f} J={:.1f}".format(i, j + 1 + i))
            print("I={:.1f} J={:.1f}".format(i, j + 2 + i))

        i += 0.2
main()
