def main():
  n = int(input())
  segundos = n % 60
  horas = n// 3600
  n %= 3600
  minutos = n // 60
  print('{}:{}:{}'.format(horas, minutos, segundos))
main()