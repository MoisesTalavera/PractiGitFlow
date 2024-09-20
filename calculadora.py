
def suma(numero1, numero2):
    return numero1+numero2

def resta(num1,num2):
    return num1-num2

def calculadora():
    print("Operacion a realizar:")
    print("1. Sumar")
    print("2. Restar")

    opcion=int(input("Seleccione una operacion(1/2):"))
    print("_________________________________")
    numero1= float(input("ingrese el primer numero: "))
    numero2= float(input("ingrese el segundo numero: "))
    if(opcion==1):
        return suma(numero1,numero2)
    elif(opcion==2):
        return resta( numero1,numero2)
    else:
        print("opcion no valida")
        return 0 

    
    

    
resultado = calculadora()
print("valor optenido:",resultado)
