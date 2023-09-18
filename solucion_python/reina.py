"dos reinas no pueden estar ni en la misma fila ni en la misma columna ni en la misma diagonal "
"para comprobar que no esten en la misma fila  ni columna comprobamos los indices de las filas ,sin embargo para las diagonales es más dificil .Esto se debe hacer calculando la resta de los indices de las filas y columnas de las reinas y comprobando que no sean iguales"
"la función se pueden comer realiza todos esos cálculos"
def seguirdad_moviento(tablero,fila,columna):
    #comprobamos que no esten en la misma fila ni columna 
    for i in range (fila):
        if tablero[i]==columna:
            return "se pueden comer"
    #comprobamos que no esten en la misma diagonal
    for i in range (fila):
        if abs(fila-columna)==abs(tablero[fila]-tablero[columna]):
            return " se pueden comer"
    
    return "el moviento es seguro"

def tablero_n(n):
    tablero=[-1]*n # en un principio se utiliza el -1 en el vecto para indicar que no hay ninguna reina en el tablero
    tablero_colocado=[]
    
    def colocar_reinas(fila):
        if fila==n:
            tablero_colocado.append(tablero[:])
            return
        else:
            for columna in range(n):
              if seguirdad_moviento(tablero,fila,columna)=="el moviento es seguro":
                tablero[fila]=columna
                colocar_reinas(fila+1)#llamamos a la función colocar reinas para la siguiente fila
                tablero[fila]=-1#si no se puede colocar la reina en la casilla se vuelve a poner el -1

    colocar_reinas(0)#llamamos a la función colocar reinas para la primera fila
    return tablero_colocado