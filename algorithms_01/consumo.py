def main():
  x = int(input()) 
  entrada = input()
  valores = entrada.split(" ")
  y = (valores[0])
  consumo = (int(x)/(float(y))) #transformar uma lista em um valor real
  print("{:.3f}".format(consumo), "km/l")
if __name__ == "__main__":
   main()