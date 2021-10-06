import random

def aleatorio():
    numAleatorio = random.randint(1, 500)
    # print(f'funcion aleatorio {numAleatorio}')
    return numAleatorio

def empezar():
    print('--- Bienvenido a frio y caliente ---')
    numAleatorio = aleatorio()
    i=0

    try:
        numIntentos = int(input('Ingrese el numero de intentos:  '))
        if numIntentos<1:
            raise ValueError(f'Debe ser mayor a cero')
    except:
        print('Numero invalido')
    else:
        while i < numIntentos:
            print(f'intento {i+1}')
            try:
                numUsuario = int(input('que numero cree que es:  '))
            except:
                print('Numero invalido')
            else:
                
                diferencia = numAleatorio-numUsuario
                if diferencia == 0:
                    print('Haz ganado')
                    break
                elif diferencia> 0:
                    print('frio')
                else:
                    print('caliente')


            i+=1
    finally:
        if diferencia!=0:
            print('Perdio intente nuevamente')
        print('Haz finalizado')


def iniciarJuego():
    jugar = 'si'
    while jugar == 'si':
        
        empezar()

        jugar = input('De sea jugar si o no:  ')

iniciarJuego()