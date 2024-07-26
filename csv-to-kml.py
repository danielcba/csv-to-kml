import csv
import simplekml


# Crear un objeto KML
kml = simplekml.Kml(open=1)

# Abrir el archivo CSV
with open('/mi-carpeta/coordenadas.csv') as csvfile:
    # Leer el archivo CSV usando un DictReader
    reader = csv.DictReader(csvfile)

    # Iterar a través de cada fila en el CSV
    for row in reader:
        # Obtener la latitud y longitud de la fila
        lat, lon = (row['latitud'], row['longitud'])
        pnt = kml.newpoint()  # Crear un nuevo punto en el KML
        pnt.coords = [(lon, lat)]  # Establecer las coordenadas del punto

# Guardar el archivo KML
kml.save("/mi-carpeta/puntos.kml")
