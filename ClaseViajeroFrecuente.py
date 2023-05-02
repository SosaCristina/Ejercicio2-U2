
class Viajero:
    __numero=int
    __dni= ""
    __nombre=""
    __apellido=""
    __millas_acum=int
    
    def __init__ (self,num=None,doc=None,nomb=None,apell=None,millas=None):
        self.__numero=num
        self.__dni=doc
        self.__nombre=nomb
        self.__apellido=apell
        self.__millas_acum=millas

    def getNumero (self):
        return self.__numero    


    def cantidadTotalMillas (self):
        return self.__millas_acum

    def acumularMillas (self, cant_millas):
        self.__millas_acum+=cant_millas
        return self.__millas_acum

    def canjearMillas (self, cant_canjear):
        if (cant_canjear <= self.__millas_acum):
            self.__millas_acum-=cant_canjear
        else:
            print("Error al canjear millas, cantidad ingresada incorrecto") 

        return  self.__millas_acum       

    def __str__(self):
        return 'Numero:{},dni:{},nombre:{},apellido:{},millas:{}'.format(self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)      