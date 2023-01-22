
num1=int(input("Dame un número: "))
x= 0

def multi(x):
    while x<10:
        x =x+1
        print("El resultado de la multiplicación es: {} * {} = {}".format(num1,x,(num1*x)))
multi(x)