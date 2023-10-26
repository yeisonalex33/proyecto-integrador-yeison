import os
from readchar import readkey

#definir la funcion para limpiar la terminal
def clean():
    os.system('cls' if os.name=='nt' else 'clear')


#definimos la variable de tipo entero que almacenará el numero que va aumentando
number = 0

print("digita la tecla 'n' para iniciar el conteo")

#realizamos el bucle
while True:
    key = readkey()

    if key == 'n':
        number += 1
        clean()
        print(f"digita la tecla '{key}' {number} veces de 50 posibles, sigue así")

        if number == 50:
            clean()
            print(f"Felicitaciones, has digitado exitosamente la tecla 'n' {number} veces")
            break

    else:
        print(f"Has digitado la tecla {key} en lugar de 'n', intentalo de nuevo")        