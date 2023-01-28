
class menu():

    print("***********Bienvenido al menu de operaciones*********")

    def menu(self,a,b):
        self.num1=a
        self.num2=b
        return a+b
    def suma(self):
       return self.num1+self.num2
    def resta(self):
        return self.num1-self.num2
    def multiplicacion(self):
        return self.num1*self.num2
    def division(self):
        return self.num1/self.num2

def eleccion():
        opc = int(input("Que operación quieres hacer \n 1 para Suma \n 2 para  Resta \n 3 para multiplicación \n 4 para División \n 5 para Salir \n "))
        main(opc)

def main(opc):
    obj  = menu()
    if(opc == 5):
        print("Gracias por usar nuestra calculadora")
        quit()    
    obj.num1 = int(input("Dame un número: "))
    obj.num2 = int(input("Dame otro número: "))
    if (opc == 1):
        print(obj.suma())
        eleccion()
    elif (opc == 2):
        print(obj.resta())
        eleccion()
    elif (opc == 3):
        print(obj.multiplicacion())
        eleccion()
    elif (opc == 4):
        print(obj.divison())
        eleccion()


opc = int(input("Que operación quieres hacer \n 1 para Suma \n 2 para  Resta \n 3 para multiplicación \n 4 para División \n 5 para Salir \n "))

if __name__ == "__main__":
    main(opc)