'''def main():
  x = []*10
  x = float(input())
  for i in range(len(x)):
    if i == 0 or i < 0:
       print(i)
main() 
'''
def main():
  x = []*10
  for i in range(10):
      z = int(input())
      x.append(z)
  for i in range(10):
     if x[i] <=0:
        x[i] = 1
  [print("X{} = {}".format([i],x[i])) for i in range(len(x))]
main() 
