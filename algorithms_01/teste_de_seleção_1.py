def main():
    A, B, C, D = (input()).split()
    somaAB=int(A)+int(B)
    somaCD=int(C)+int(D)
    positivo=(int(C))and(int(D))
    parA=(int(A)%2)
    if int(B)>int(C)and(int(D)>int(A))and(int(somaCD)>int(somaAB)and(int(positivo)>0)and(int(parA==0))):
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")
if __name__ == "__main__":        
    main()