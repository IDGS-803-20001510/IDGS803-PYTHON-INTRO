
print("***********Bienvenido al menu de operaciones*********")


def suma(num1, num2):
    print("El resultado de la suma es: {} + {}  = {}".format(num1, num2, (num1+num2)))
    eleccion()


def resta(num1, num2):
    print("El resultado de la resta es: {} - {}  = {}".format(num1, num2, (num1-num2)))
    eleccion()


def multiplicación(num1, num2):
    print("El resultado de la multiplicación es: {} * {}  = {}".format(num1, num2, (num1*num2)))
    eleccion()


def division(num1, num2):
    print("El resultado de la división es: {} / {}  = {}".format(num1, num2, (num1/num2)))
    eleccion()


def eleccion():
    opc = int(input("Que operación quieres hacer \n 1 para Suma \n 2 para  Resta \n 3 para multiplicación \n 4 para División \n 5 para Salir \n "))
    main(opc)


def main(opc):
    if(opc == 5):
        print("Gracias por usar nuestra calculadora")
        quit()
    if(opc !=5):
        print("El número que ingresaste no esta registrado")
        quit()
    num1 = int(input("Dame un número: "))
    num2 = int(input("Dame otro número: "))
    if (opc == 1):
        suma(num1, num2)
    elif (opc == 2):
        resta(num1, num2)
    elif (opc == 3):
        multiplicación(num1, num2)
    elif (opc == 4):
        division(num1, num2)


opc = int(input("Que operación quieres hacer \n 1 para Suma \n 2 para  Resta \n 3 para multiplicación \n 4 para División \n 5 para Salir \n "))

if __name__ == "__main__":
    main(opc)
