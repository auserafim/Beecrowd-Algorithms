"""
def main():
  colors = ["red", "blue", "green"]
  colors.append("dark blue")
  i = 0
  while i < len(colors):
    print (colors[i]) 
    i +=1
main()

"""
def main():
 
 def append_to_list(cores, cor):
  if cor not in cores:
   cores.append(cor)
  else:
   print("a cor", cor, "já existia na lista") 
  
  cores = ["Branco", "Azul", "Preto"]
  cor = input("Insira uma cor: ")
  append_to_list(cores, cor)

main()

