import math

# Função para calcular a área do triângulo
def area_triangulo(A, C):
    return A * C / 2

# Função para calcular a área do círculo
def area_circulo(C):
    return math.pi * C * C

# Função para calcular a área do trapézio
def area_trapezio(A, B, C):
    return (A + B) * C / 2

# Função para calcular a área do quadrado
def area_quadrado(B):
    return B * B

# Função para calcular a área do retângulo
def area_retangulo(A, B):
    return A * B

# Lê os valores de entrada
A, B, C = map(float, input().split())

# Calcula as áreas
area_triang = area_triangulo(A, C)
area_circ = area_circulo(C)
area_trapez = area_trapezio(A, B, C)
area_quad = area_quadrado(B)
area_ret = area_retangulo(A, B)

# Formata e imprime os resultados
print(f"TRIANGULO: {area_triang:.3f}")
print(f"CIRCULO: {area_circ:.3f}")
print(f"TRAPEZIO: {area_trapez:.3f}")
print(f"QUADRADO: {area_quad:.3f}")
print(f"RETANGULO: {area_ret:.3f}")
