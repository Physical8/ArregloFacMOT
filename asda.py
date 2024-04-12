import re

archivo = "./FE1 TRA 38878.XML"
patron = r'REM (\d+)'

# Contador para seguir la posición de las coincidencias
contador_coincidencias = 0

# Abrir el archivo y recorrer línea por línea
with open(archivo, 'r') as f:
    for linea in f:
        # Buscar la cadena <cbc:Description>
        if '<cbc:Description>' in linea:
            # Incrementar el contador de coincidencias
            contador_coincidencias += 1

            # Si es la segunda coincidencia, buscar el número después de 'REM'
            if contador_coincidencias == 2:
                resultado = re.search(patron, linea)
                if resultado:
                    numero_despues_rem = resultado.group(1)
                    print("Número después de 'REM' en la segunda coincidencia:", numero_despues_rem)
                    break  # Salir del bucle después de encontrar la segunda coincidencia

# Si no se encontró la segunda coincidencia, imprimir un mensaje
if contador_coincidencias < 2:
    print("No se encontró la segunda coincidencia de <cbc:Description> en el archivo.")
