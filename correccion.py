import os

def reemplazar_cadena_en_archivo(nombre_archivo, cadena_a_buscar, cadena_a_reemplazar, cambio_1, cadena_a_buscar2, cadena_a_reemplazar2, cambio_2, cadena_a_buscar3, cadena_a_reemplazar3, cambio_3):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            nuevo_contenido = contenido

            # CAMBIO 1
            if cadena_a_buscar in nuevo_contenido:
                nuevo_contenido = nuevo_contenido.replace(cadena_a_buscar, cadena_a_reemplazar)
                with open("historial.txt", 'a') as historial:
                    historial.write("En el archivo {} se hizo el cambio: {}\n".format(nombre_archivo, cambio_1))
            
            # CAMBIO 2
            if cadena_a_buscar2 in nuevo_contenido:
                nuevo_contenido = nuevo_contenido.replace(cadena_a_buscar2, cadena_a_reemplazar2)
                with open("historial.txt", 'a') as historial:
                    historial.write("En el archivo {} se hizo el cambio: {}\n".format(nombre_archivo, cambio_2))

            # CAMBIO 3
            if cadena_a_buscar3 in nuevo_contenido:
                nuevo_contenido = nuevo_contenido.replace(cadena_a_buscar3, cadena_a_reemplazar3)
                with open("historial.txt", 'a') as historial:
                    historial.write("En el archivo {} se hizo el cambio: {}\n".format(nombre_archivo, cambio_3))

        if nuevo_contenido != contenido:
            # Escribir el contenido modificado de vuelta al archivo
            with open(nombre_archivo, 'w') as archivo:
                archivo.write(nuevo_contenido)
            print("Reemplazo completado en el archivo:", nombre_archivo)
        else:
            print("No se realizaron cambios en el archivo:", nombre_archivo)
            
    except FileNotFoundError:
        print("El archivo '{}' no se encontró.".format(nombre_archivo))
    except Exception as e:
        print("Ocurrió un error:", e)

# Definir la carpeta que contiene los archivos
carpeta = "./Febrero"

# Obtener la lista de archivos en la carpeta
archivos_en_carpeta = os.listdir(carpeta)

# Cadena que deseas buscar dentro del archivo
cadena_a_buscar = "<cbc:CustomizationID>10</cbc:CustomizationID>"

# Cadena con la que deseas reemplazar la cadena encontrada
cadena_a_reemplazar = "<cbc:CustomizationID>12</cbc:CustomizationID>"
cambio_1 = "Cambio 1"

# Cadena que deseas buscar dentro del archivo (segunda cadena)
cadena_a_buscar2 = "<cac:InvoiceLine>\n    <cbc:ID>1</cbc:ID>"
# Cadena que deseas reemplazar la segunda cadena encontrada
cadena_a_reemplazar2 = "<cac:InvoiceLine>\n    <cbc:ID schemeID=\"1\">1</cbc:ID>"
cambio_2 = "Cambio 2"

# Cadena que deseas buscar dentro del archivo (tercera cadena)
cadena_a_buscar3 = "</cac:AdditionalItemProperty>\n    </cac:Item>\n    <cac:Price>\n      <cbc:PriceAmount currencyID=\"COP\">"
# Cadena que deseas reemplazar la tercera cadena encontrada
cadena_a_reemplazar3 = "  <cbc:ValueQuantity unitCode=\"KGM\">1</cbc:ValueQuantity>\n      </cac:AdditionalItemProperty>\n    </cac:Item>\n    <cac:Price>\n      <cbc:PriceAmount currencyID=\"COP\">"
cambio_3 = "Cambio 3"

# Iterar sobre cada archivo y aplicar la función reemplazar_cadena_en_archivo
for nombre_archivo in archivos_en_carpeta:
    ruta_archivo = os.path.join(carpeta, nombre_archivo)
    reemplazar_cadena_en_archivo(ruta_archivo, cadena_a_buscar, cadena_a_reemplazar, cambio_1, cadena_a_buscar2, cadena_a_reemplazar2, cambio_2, cadena_a_buscar3, cadena_a_reemplazar3, cambio_3)
