#introducimos los  movimientos que puede realizar el caballo desde cada casilla

movimientos={0:[6,4],1:[6,8],2:[7,9],3:[4,8],4:[3,9,0],5:[],6:[1,7,0],7:[2,6],8:[1,3],9:[2,4]}


def contar_movientos_pasos(movimientos_restantes):#movientos_restantes: número de pasos que desea dar el usuario
        if movimientos_restantes==0:
            return 0 #no se pueden hacer movimientos
        

        numero_movientos_totales=0 #inicializamos la variable movientos totales que acumulara el número de movientos válidos

        "utilizamos bucle for para ir recorriendo todas las casillas del diccionario movimientos"
        for casilla_inicial in range(10):
              "la función contar movientos se utiliza para contar las secuencias de movientos válidos desde cada casilla"
              def contar_movimientos(casilla_actual,movientos_restantes):
                    if movientos_restantes==0:
                        return 1
                    
                    movimientos_validos=0
                    "recorremos todas las casillas que se pueden alcanzar desde la inicial"
                    for siguiente_casilla in movimientos[casilla_actual]:
                        movimientos_validos+=contar_movimientos(siguiente_casilla,movientos_restantes-1)#disminuimos en 1 el número de movientos restantes cada vuelta del bucle for"
                    
                    return movimientos_validos
        numero_movientos_totales+=contar_movimientos(casilla_inicial,movimientos_restantes-1)

        return numero_movientos_totales
                    

        
#solicitar usuario el número de pasos que desea dar
movientos_deseados=int(input("Introduzca el número de movientos que quiera dar: "))

numero_movientos_totales=contar_movientos_pasos(movientos_deseados)
print("El número de movientos válidos que puede realizar el caballo en el tablero de ajedrez es: ",numero_movientos_totales) 