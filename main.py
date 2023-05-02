from ClaseViajeroFrecuente import Viajero
import csv



if __name__=='__main__':
    listaViajero=[]
    archivo=open('C:\\Users\\chili\\viajeros.csv') #C:\Users\chili\OneDrive\Escritorio\FACULTAD\POO\ej2\ 
    reader=csv.reader(archivo,delimiter=",")
    for fila in reader:
        numero=int(fila[0])
        dni=fila[1]
        nombre=fila[2]
        apellido=fila[3]
        millas_acum=int(fila[4])
        unViajero=Viajero(numero,dni,nombre,apellido,millas_acum)
        listaViajero.append(unViajero)
    archivo.close()

    for i in  range (len(listaViajero)):

        print(listaViajero[i])

    numero_v=int(input("Ingrese numero de viajero:"))
    i=0
    otroViajero=listaViajero[i]
    num=int(otroViajero.getNumero())
    while ((i<=(len(listaViajero)-1))and(numero_v!=num)):
        i+=1
        otroViajero=listaViajero[i]
        num=int(otroViajero.getNumero())
    








    opcion=0
    def menu():
       opc=int(input("Menu Principal\n"+
       "1)Consultar Millas\n"+
       "2)Acumular Millas \n"+
       "3)Canjear Millas\n"+
       "4)Finalizar\n"+
       "Seleccione una opcion\n"))
       return opc
    while opcion!=4:
       opcion=menu()
       if opcion==1:
        print("La cantidad total de millas es:{}".format(otroViajero.cantidadTotalMillas()))
       if opcion==2:
        cant=int(input("Ingresar cantidad de millas para acumular:"))
        otroViajero.acumularMillas(cant)
        print("La cantidad total de millas actualizado es:{}".format(otroViajero.cantidadTotalMillas()))
       if opcion==3:
        cant2=int(input("Ingresar cantidad de millas para canjear:"))
        otroViajero.canjearMillas(cant2)
        print("La cantidad total de millas actualizado es:{}".format(otroViajero.cantidadTotalMillas()))



                    

    
        



