import time 
def main():
    n = int(input())
    tempo = time.strftime("%H:%M:%S", time.gmtime(n))
    print(tempo)
if __name__ == "__main__":
    main()  


 
