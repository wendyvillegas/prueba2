
def conteo (frase, palabra):
    num= frase.count(palabra)
    print(palabra+" = "+ str(num ))


#prueba= "el amor es una locura que el cura lo cura si el cura lo cura seria una locura del cura";
#print(prueba)
#print("el numero de repeticiones de locura es: "+ str(prueba.count("locura")))

frase= input("Ingrese una frase: ")
print("su frase es: "+frase)
palabra=input("ingrese la palabra que desea saber el numero de repeticiones: ")
conteo(frase, palabra)

