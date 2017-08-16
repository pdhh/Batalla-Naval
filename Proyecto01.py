import random
#Inicio de la clase barco
class Barco:
    def __init__(self,pTipo,pTripulantes):
        self.tipo=pTipo
        self.tripulantes=pTripulantes


    def __str__(self):
        return ("Tipo = {0}\nTripulantes = {1}".format(self.tipo,self.tripulantes))

    def hundirse(self):
       print("Se ha hundido un: ",self.tipo)

#Inicio de la clase Capitan
class Capitan:
    def __init__(self,pNombre,pPais,pPuntos,pBarcos,pMisiles):
        self.nombre=pNombre
        self.pais=pPais
        self.puntos=pPuntos
        self.cantidadBarcos=pBarcos#Cantidad de barcos
        self.misiles=pMisiles

    def __str__(self):
        return ("Nombre: {0}\nPais: {1}\nPuntos: {2}\nBarcos: {3}\nMisiles: {4}"
                .format(self.nombre,self.pais,self.puntos,self.cantidadBarcos,self.misiles))

    def fallar(self):
        print("HAS FALLADO!\n")

    def acertar(self):
        print("HAS ACERTADO!\n")

    def rendirse(self):
        print("*TE HAS RENDIDO*\n")

    def perder(self):
        return(self.nombre,"*ES EL PERDEDOR*")# El return es para escribir la cadena de caracteres en
    #Los archivos de estadísticas

    def ganar(self):
        return(self.nombre,"*ES EL GANADOR*")


def Aleatorio():#Devuelve un numero aleatorio entre 1 y 6
    numero=random.randrange(1,6)
    return (numero)

#Estos son los contructores de los campos de batalla que a su vez son matrices
campo1=[['O'for j in range(6)]for i in range (6)]
campo2=[['O' for y in range (6)]for x in range (6)]

def barcoAleatorio(barco):#Esto nos devuelve un barco cualquiera de los objetos ya creados
    if barco==1:
        return (barco1)
    if barco==2:
        return (barco2)
    if barco==3:
        return (barco3)
    if barco==4:
        return (barco4)
    if barco==5:
        return (barco5)

#Instanciamos los objetos de la clase barco
def tripulantes():#Asigará un cantidad aleatoria de tripulantes de 1 a 100
    cantTripulantes=random.randrange(1,100)
    return (cantTripulantes)

barco1=Barco("Porta Aviones",tripulantes())
barco2=Barco("Cañonero",tripulantes())
barco3=Barco("Acorazado",tripulantes())
barco4=Barco("Corbeto",tripulantes())
barco5=Barco("Submarino",tripulantes())

#Creamos los juadores de tipo Capitan
listaJugadores=[]
def datosJugadores(numerobarcos):
    nombre=input("Escriba su nombre\n")
    pais=input("Escriba el pais a la que pertenece su armada\n")
    puntos=0
    barcos=numerobarcos
    misiles=Aleatorio()#Asigna misiles aleatorios de 1 a 6
    jugador=Capitan(nombre,pais,puntos,barcos,misiles)
    listaJugadores.append(jugador)#Lo guardamos en la lista de jugadores

def llenaCampo(pCampo):#Llena el campo con una cantidad de barcos aleatoria
    j=0
    cantidadBarcos=Aleatorio()

    while j<=cantidadBarcos:
        pCampo[random.randint(0,5)][random.randint(0,5)]=barcoAleatorio(Aleatorio())
        j=j+1
    datosJugadores(cantidadBarcos)#le pasa al jugador la misma cantidad de barcos de su campo

def muestraCampo(num):#Muestra un campo de batalla
    campoAlternativo=[['O'for z in range(6)]for u in range(6)]
    if num == 1:
        for i in campo1:
            if i=='O':
                campoAlternativo.append(i)
            else:
                campoAlternativo.append('Barco')
        print("*Campo del Jugador 1*\t\n")
        for i in campoAlternativo:
            print(i)
    else:
        for i in campo2:
            if i!='O':
                campoAlternativo.append('Barco')
            else:
                campoAlternativo.append(i)

        print("*Campo del Jugador 2*\t\n")
        for i in campoAlternativo:
            print(i)

def ataque(pCampo,listaAciertos,listaErrores,jugador):#Este es el procedimiento que utilizamos para atacar
    errores=0
    print("*AVISO!*\t\n*Los paralelos y meridianos deben ser un numero entre 1 y 6\n")
    while True:
        try:
            paralelo=int(input("Digite el Paralelo\n"))
            if paralelo>0 and paralelo<=6:#Que no sea 0
                break
            else:
                print("Está fuera del Rango\n")
        except ValueError:
            print("Digite un número\n")

    while True:
        try:
            meridiano=int(input("Digite el Meridiano\n"))
            if paralelo>0 and paralelo<=6:#Que no sea 0
                break
            else:
                print("Está fuera del Rango\n")
        except ValueError:
            print("Digite un número\n")

    a=pCampo[paralelo-1][meridiano-1]#atacamos la posición
    if a == 'O':
        jugador.fallar()
        errores=errores+1
        listaErrores.append(errores)#se ingresan los errores en la lista

    else:
        print("*BARCO DESTRUIDO!*")
        jugador.acertar()
        jugador.puntos=jugador.puntos+100
        a.hundirse()
        print("Con {0} tripulantes".format(a.tripulantes))
        listaAciertos.append(a)#la cantidad de aciertos será el tamaño de la lista

#Datos del Jugador 1
listaErroresJ1=[]
listaAciertosJ1=[]#Tambien contiene los barcos destruidos por Jugador 1
#Datos del Jugador 2
listaErroresJ2=[]
listaAciertosJ2=[]#Tambien contiene los barcos destruidos por Jugador 2

def creaEstadisticas1(listaJugadores,listaAciertos):
    estadisticas = open("Estadisticas1.txt","w")
    estadisticas.write("***ESTADISTICAS***\t\n")
    obj1=listaJugadores[0]
    obj2=listaJugadores[1]
    destruidosJ1=len(listaAciertosJ1)
    fallosJ1=len(listaErroresJ1)
    destruidosJ2=len(listaAciertosJ2)
    fallosJ2=len(listaErroresJ2)
    estadisticas.write("**Jugador 1**\t\n*{0} Fué el Ganador!\n*Aciertos: {1}\n*Fallos: {2}\n*Puntos: {3}\n"
                       .format(obj1.nombre,destruidosJ1,fallosJ1,obj1.puntos))
    estadisticas.write("*Barcos Destruidos*\n*"+str(destruidosJ1)+"\t\n****************\n")
    if len(listaAciertos)>0:
        for i in listaAciertos:
            estadisticas.write("Tipo: "+i.tipo+"\n")
            estadisticas.write("Cantidad de tripulantes muertos: "+str(i.tripulantes)+"\n****************\n")
    else:
        estadisticas.write("*No Acertó ningun barco*\t\n*****************\n")
    estadisticas.write("**Jugador 2**\t\n*{0} Fué el Perdedor\n*Aciertos: {1}\n*Fallos: {2}\n*Puntos: {3}\n"
                       .format(obj2.nombre,destruidosJ2,fallosJ2,obj2.puntos))
    estadisticas.close()

def creaEstadisticas2(listaJugadores,listaAciertos):
    estadisticas = open("Estadisticas2.txt","w")
    estadisticas.write("***ESTADISTICAS***\t\n")
    obj1=listaJugadores[0]
    obj2=listaJugadores[1]
    destruidosJ2=len(listaAciertosJ2)
    fallosJ2=len(listaErroresJ2)
    destruidosJ1=len(listaAciertosJ1)
    fallosJ1=len(listaErroresJ1)
    estadisticas.write("**Jugador 2**\t\n*{0} Fué el Ganador!\n*Aciertos: {1}\n*Fallos: {2}\n*Puntos: {3}\n"
                       .format(obj2.nombre,destruidosJ2,fallosJ2,obj2.puntos))
    estadisticas.write("*Barcos Destruidos*\n*"+str(destruidosJ2)+" \t\n****************\n")
    if len(listaAciertos)>0:
        for i in listaAciertos:
            estadisticas.write("Tipo: "+i.tipo+"\n")
            estadisticas.write("Cantidad de tripulantes muertos: "+str(i.tripulantes)+"\n****************\n")
    else:
        estadisticas.write("*No Acertó ningún barco*\t\n****************\n")

    estadisticas.write("**Jugador 1**\t\n*{0} Fué el Perdedor\n*Aciertos: {1}\n*Fallos: {2}\n*Puntos: {3}\n"
                       .format(obj1.nombre,destruidosJ1,fallosJ1,obj1.puntos))
    estadisticas.close()

def leerEstadisticas1():#Lee el primer archivo de estadísticas
    estadisticas1 = open("Estadisticas1.txt","r")
    contenido1=estadisticas1.read()
    estadisticas1.close()
    print(contenido1)

def leerEstadisticas2():#Lee el segundo archivo de estadísticas
    estadisticas2 = open("Estadisticas2.txt","r")
    contenido2=estadisticas2.read()
    estadisticas2.close()
    print(contenido2)


def partida():
    print("***INICIO DEL JUEGO***\t\n")
    print("**Jugador 1**\t\n*Ingrese sus datos*")
    llenaCampo(campo1)
    print("Jugador 2**\t\n*Ingrese sus datos**")
    llenaCampo(campo2)

    obj1=listaJugadores[0]
    obj2=listaJugadores[1]
    while True:
        while True:
            try:
                turno=int(input("¿Quien Juega?\t\n1.Jugador 1\n2.Jugador 2\n"))
                if turno>0 and turno<3:
                    break
                else:
                    print("Solo hay dos opciones\n")
            except ValueError:
                print("Digite un número\n")

        if turno == 1:
            print("**Jugador 1** es:\t\n*{0}".format(obj1.nombre))
            print("1.Atacar\n2.Rendirse")
            print("Tienes {0}, misiles(turnos)".format(obj1.misiles))
            if obj1.misiles>0:
                while True:
                    try:

                        desicion=int(input("¿Qué desea hacer?\n"))
                        if desicion>0 and desicion<3:
                            break
                        else:
                            print("Esa opción no existe\n")
                    except ValueError:
                        print("Digite un número\n")
            else:
                print("*NO TE QUEDAN MISILES!*")
                print("SOLO PUEDES RENDIRTE, HAS PERDIDO!")
                desicion=2


            if desicion == 1:
                ataque(campo1,listaAciertosJ1,listaErroresJ1,obj1)
                obj1.misiles=obj1.misiles-1

            if desicion == 2:
                obj1.rendirse()
                print(obj2.ganar())
                #creaEstadisticas2(listaJugadores,listaAciertosJ1,listaErroresJ1)
                #leerEstadisticas2()
                break

        if turno == 2:
            print("**Jugador 2 es:\t\n*{0}".format(obj2.nombre))
            print("1.Atacar\n2.Rendirse")
            print("Tienes {0}, misiles (turnos)".format(obj2.misiles))
            if obj2.misiles>0:
                while True:
                    try:
                        desicion2=int(input("¿Que desea hacer?\n"))
                        if desicion2>0 and desicion2<3:
                            break
                        else:
                            print("Esa opción no existe\n")
                    except ValueError:
                        print("Digite un número\n")
            else:
                print("*NO TE QUEDAN MISILES!*")
                print("SOLO PUEDES RENDIRTE, HAS PERDIDO")
                desicion2=2

            if desicion2 == 1:
                ataque(campo2,listaAciertosJ2,listaErroresJ2,obj2)
                obj2.misiles=obj2.misiles-1

            if desicion2 == 2:
                obj2.rendirse()
                print(obj1.ganar())
                #creaEstadisticas1(listaJugadores,listaAciertosJ2,listaErroresJ2)
                #leerEstadisticas1()
                break

def limpiaListas(lista):
    cant=len(lista)
    while cant > 0:
        del lista[cant-1]
        cant=cant-1

op=0

while op!=1:
    try:
        print("*********************************")
        print("***BIENVENIDOS A BATALLA NAVAL***\t")
        print("*********************************")
        print("By Roger and Pablo S.A\t\nAll rights reserved 2017\t")
        print("***MENÚ****\t\n1.Salir\n2.Jugar\n3.*Ver Estadísticas*\n4.Borrar Estadísticas\n5.Instrucciones del Juego")
        op=int(input("Digite una opción\n"))

        if op == 2:
            partida()

        elif op == 3:
            if len(listaJugadores)>0:#Se valida que se haya juagado
                obj1 = listaJugadores[0]
                obj2 = listaJugadores[1]
                if obj1.misiles>obj2.misiles:
                    creaEstadisticas1(listaJugadores,listaAciertosJ1)
                    leerEstadisticas1()
                else:
                    creaEstadisticas2(listaJugadores,listaAciertosJ2)
                    leerEstadisticas2()

            else:
                print("*DEBE JUGAR PRIMERO PARA GENERAR ESTADÍSTICAS*\t\n")

        elif op == 4:
            if len(listaJugadores)>0:
                limpiaListas(listaJugadores)
                limpiaListas(listaAciertosJ1)
                limpiaListas(listaErroresJ1)
                limpiaListas(listaAciertosJ2)
                limpiaListas(listaErroresJ2)
            else:
                print("*NO HAY ESTADÍSTICAS PARA BORRAR AÚN*\t\n")

        elif op == 5:
            print("***INSTRUCCIONES BÁSICAS***:\t\n")
            print("1.El juego requiere de dos participantes")
            print("2.Los campos de batalla son matrices de 6x6")
            print("3.Los participante eligen quién empieza y quién sigue jugando")
            print("4.Las coordenadas están dadas por Meridianos y Paralelos")
            print("\t4.1.Los Meridianos son Columnas de la Matriz")
            print("\t4.2.Los Paralelos son Filas de la Matriz")
            print("5.Las teclas más usadas son el *1* y el *2* para jugar")
            print("6.Un acierto vale 100 pts")
            print("*Nota*\t\n*En este juego curiosamente no gana el que hunda más barcos del oponente,\nsin embargo se puede competir para saber quien tiene más puntería y hunde más barcos")
            print("*Intenta hundir todos los que puedas\n")


        if op == 0 or op > 5:#Que no sea 0 ni mayor que 5
            print("*Opción no disponible*")

    except ValueError:
        print("Digite un numero\n")

print("*GRACIAS POR JUGAR*")