def crearArchi():
    archi=open('lectura.txt', 'w')
    archi=open('repeticiones.txt', 'w')
    archi.close()


def grabarArchi():
    archi=open('lectura.txt', 'a')
    archi.write(IngresarLectura()+"\n\n")
    archi.close()

def leerArchi():
    archi=open('lectura.txt', 'r')
    linea=archi.readline()
    while linea!="":
        return linea
    archi.close()

def IngresarLectura():
    print("ingrese el texto a grabar")
    texto=input()
    return texto

def grabarRepeticiones():
    archi=open('repeticiones.txt', 'a')
    archi.write(conteo(leerArchi())+"\n")


def conteo(texto):
    print("Ingrese la palabra de la que desea conocer las repeticiones")
    palabra=str(input())
    repeticiones= str(texto.count(palabra))
    print(palabra+": "+repeticiones)
    return palabra+": "+repeticiones


#crearArchi()

print("Seleccione una opcion")
print("1. Si desea escribir un texto")
print("2. Si desea saber el numero de repeticiones de una palabra")
opcion=int(input())
if opcion == 1:
    grabarArchi()
elif opcion == 2:
    grabarRepeticiones()
else:
    print("Opcion Invalida")
