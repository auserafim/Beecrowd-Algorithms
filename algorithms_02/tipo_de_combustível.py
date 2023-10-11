def main():
  álcool = 0
  gasolina =0 
  diesel = 0
  while True:
    codigo = int(input())
    if codigo == 1:
      álcool +=1
    elif codigo == 2:
      gasolina += 1
    elif codigo == 3:
       diesel +=1
    elif codigo == 4:
      break
    else:
      continue
  print("MUITO OBRIGADO") 
  print("Alcool:", álcool) 
  print("Gasolina:", gasolina) 
  print("Diesel:", diesel) 
main()  


#tomar 4 valores de entrada
#para cada vez que 1 for tomado de entrada, somar 1 ao total de clientes com álcool
#mas caso o número 4 seja fornecido, o programa deve acabar 