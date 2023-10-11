def main():
    x = [0.0] * 100  
    n = float(input())
    x[0] = n

    for i in range(1, 100): 
        n /= 2
        x[i] = n

    for i in range(100):
        print("N[{}] = {:.4f}".format(i, x[i]))


main()
