# Conversor de CSV a KML

Este script en Python convierte un archivo CSV que contiene coordenadas geográficas (latitud y longitud) en un archivo KML (Keyhole Markup Language). El archivo KML se puede utilizar con herramientas de visualización geográfica como Google Earth, QGIS, etc.

## Requisitos

- Python 3.x
- Biblioteca `simplekml`

Puedes instalar la biblioteca `simplekml` usando pip:

```sh
pip install simplekml
```

## Uso

1. Prepara tu archivo CSV con el siguiente formato:

   ```csv
   latitud,longitud
   -31.518,-65.104
   -31.548,-65.095
   ```

2. Guarda el archivo CSV en una ubicación conocida en tu sistema.

3. Se adjunta un archivo 'coordenadas.csv' de ejemplo.

### Script: `csv_to_kml.py`

```python
import csv
import simplekml

# Crear un objeto KML
kml = simplekml.Kml(open=1)

# Abrir el archivo CSV
with open('/mi-carpeta/coordenadas.csv') as csvfile:
    reader = csv.DictReader(csvfile)  # Leer el archivo CSV usando un DictReader
    
    # Iterar a través de cada fila en el CSV
    for row in reader:
        lat, lon = (row['latitud'], row['longitud'])  # Obtener la latitud y longitud de la fila
        pnt = kml.newpoint()  # Crear un nuevo punto en el KML
        pnt.coords = [(lon, lat)]  # Establecer las coordenadas del punto

# Guardar el archivo KML
kml.save("/mi-carpeta/puntos.kml")
```

### Ejecutar el Script

1. Asegúrate de que el script y el archivo CSV estén en los directorios especificados.
2. Ejecuta el script usando Python:

   ```sh
   python csv_to_kml.py
   ```

3. El archivo KML se creará en el directorio especificado.

### Notas

- Asegúrate de que la ruta al archivo CSV en el script coincida con la ubicación real de tu archivo CSV.
- El script asume que el archivo CSV contiene columnas llamadas `latitud` y `longitud`.

### Contribuciones

¡Las contribuciones son bienvenidas! No dudes en enviar un Pull Request.

### Contacto

Si tienes alguna pregunta o sugerencia, por favor abre un issue o contacta conmigo.

### Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
