def main():
    dias =int(input())
    ano = dias//365
    dias%=365 #atualiza o valor da variável
    mes = dias//30
    dias%=30
    dia = dias
    print(ano,"ano(s)")
    print(mes,"mes(es)")
    print(dia,"dia(s)")
if __name__ == "__main__":        
    main()