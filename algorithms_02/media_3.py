def main():
    a, b, c, d = map(float, input().split())

    media = (a*2 + b*3 + c*4 + d*1) / 10.0
    print("Media: {:.1f}".format(media))

    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        e = float(input())
        print("Nota do exame: {:.1f}".format(e))
        if (media + e) / 2.0 >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print("Media final: {:.1f}".format((media + e) / 2.0))

main()