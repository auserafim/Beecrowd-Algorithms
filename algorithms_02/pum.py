def main():
  n = int(input().strip()) 
  num = 1
  for _ in range(n):
        print('{} {} {}'.format(num, num+1, num+2), "PUM")
        num += 4
main() 