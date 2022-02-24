

def divisor(num):

    divisor=[]

    for i in range(1, num+1):
        if num % i==0:
            divisor.append(i)

    return divisor

def run():
    num = int(input("ingrese un valor: "))
    print(divisor(num))
    print("termino el ciclo")

if __name__ == "__main__":
    run()