def main():
    N = int(input())
    X = list(map(float, input().split()))
    menor_valor = 100
    posicao = 1
    for i in range(N):
        if X[i] < menor_valor:
            menor_valor = X[i]
            posicao = i
    print("Menor valor: {:.0f}".format(menor_valor))
    print("Posicao: {}".format(posicao))
main()
