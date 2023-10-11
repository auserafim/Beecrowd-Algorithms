def main():
  
    cores = ["azul", "Amarelo", "verde", "amarelo"]
    cor = (input("Insira uma cor: "))
    if cor in cores:
        print("a cor", cor, "está na posição: ", cores.index(cor))
    else:
        print("a cor", cor, "não está na lista") 
    for i in range(len(cores)):
        print(i, cores[i])       
    nova_lista = sorted(cores)
    print("a nova lista é: ", nova_lista)
"""def preenchendo_cores(cores, cor):
          cores.append(cor)
          cores.sort()
          for i in range(len(cores)):
               print(i, cores[i])
    preenchendo_cores(cores, cor)
"""
    
main()