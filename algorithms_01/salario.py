def main():
  vendedor = input()
  salario = float(input())
  totalDeVendas = float(input())
  total = (totalDeVendas*(0.15) + salario)
  print("TOTAL = R${:.2f}".format(total))
if __name__ == "__main__":
  main()