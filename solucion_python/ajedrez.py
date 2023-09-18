#introducimos los  movimientos que puede realizar el caballo desde cada casilla

movimientos={0:[6,4],1:[6,8],2:[7,9],3:[4,8],4:[3,9,0],5:[],6:[1,7,0],7:[2,6],8:[1,3],9:[2,4]}

"""para calcular el número de movientos válidos en función de los pasos que desee dar con la pieza el usuario empleamos la siguiente función"""
#movientos_restantes: número de pasos que desea dar el usuario
def contar_movientos_pasos(movientos_restantes):
        if movientos_restantes==0:
            return 0 #no se pueden hacer movimientos
        numero_movientos_totales=0 #inicializamos la variable movientos totales que acumulara el número de movientos válidos

        for casilla_inicial in range(10):
              def contar_movimientos(casilla_actual,movientos_restantes):
                    if movientos_restantes==0:
                        return 1
                    movimientos_validos=0
                    for siguiente_casilla in movimientos[casilla_actual]:
                        movimientos_validos+=contar_movimientos(siguiente_casilla,movientos_restantes-1)
                    return movimientos_validos
        numero_movientos_totales+=contar_movimientos(casilla_inicial,movientos_restantes-1)

        return numero_movientos_totales
                    

        
            