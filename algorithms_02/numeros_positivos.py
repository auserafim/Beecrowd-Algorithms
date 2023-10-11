def main():
  valores_positivos = 0
  for i in range(6):
    valor = float(input())
    if valor > 0:
        valores_positivos += 1
    print(valores_positivos, "valores positivos")
main()  