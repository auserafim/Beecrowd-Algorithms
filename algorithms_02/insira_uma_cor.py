def main():
    cores = []
    cor = (input("Insira uma cor: "))
    def preenchendo_cores(cores, cor):
          cores.append(cor)
          print("você tem agora uma nova lista de cores: ",cores) 
          for i in range(2):
            (cores) 
    preenchendo_cores(cores, cor)
    cor_inserida = input("Insira uma cor nova : ")
    def checando_cores(cores, cor_inserida):
        if cor_inserida in cores:
            print("Ops parece que essa cor já existe na lista!")
            for i in range(1):
                print(i, cores[i])
        else:
            print("Parabéns, você adicionou uma nova cor à lista")
            cores.append(cor_inserida)
            for i in range(2):
                print(i, cores[i])
    checando_cores(cores, cor_inserida)    
main()