def main():
  A, B, C = map(float, input().split())
  π = 3.14159
  triangulo = ((A*C)/2)
  circulo = (π*(C**2))
  trapezio = (((A+B)/2)*C)
  quadrado = (B**2)
  retangulo = (A*B)
  print("TRIANGULO: {:.3f}".format(triangulo))
  print("CIRCULO: {:.3f}".format(circulo))
  print("TRAPEZIO: {:.3f}".format(trapezio))
  print("QUADRADO: {:.3f}".format(quadrado))
  print("RETANGULO: {:.3f}".format(retangulo))
if __name__ == "__main__":
    main()
