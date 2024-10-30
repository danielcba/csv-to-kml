# CSV to KML Converter

This Python script converts a CSV file containing geographic coordinates (latitude and longitude) into a KML file (Keyhole Markup Language). The KML file can be used with geographic visualization tools such as Google Earth, QGIS, etc.

## Requirements

- Python 3.x
- `simplekml` library

You can install the `simplekml` library using pip:

```sh
pip install simplekml
```

## Usage

1. Prepare your CSV file with the following format:

   ```csv
   latitude,longitude
   -31.518,-65.104
   -31.548,-65.095
   ```

2. Save the CSV file in a known location on your system.

3. An example file 'coordinates.csv' is attached.

### Script: `csv_to_kml.py`

```python
import csv
import simplekml

# Create a KML object
kml = simplekml.Kml(open=1)

# Open the CSV file
with open('/my-folder/coordinates.csv') as csvfile:
    reader = csv.DictReader(csvfile)  # Read the CSV file using a DictReader
    
    # Iterate through each row in the CSV
    for row in reader:
        lat, lon = (row['latitude'], row['longitude'])  # Get latitude and longitude from the row
        pnt = kml.newpoint()  # Create a new point in the KML
        pnt.coords = [(lon, lat)]  # Set the point's coordinates

# Save the KML file
kml.save("/my-folder/points.kml")
```

### Run the Script

1. Ensure that the script and the CSV file are in the specified directories.
2. Run the script using Python:

   ```sh
   python csv_to_kml.py
   ```

3. The KML file will be created in the specified directory.

### Notes

- Make sure the CSV file path in the script matches the actual location of your CSV file.
- The script assumes the CSV file contains columns named `latitude` and `longitude`.

### Contributions

Contributions are welcome! Feel free to submit a Pull Request.

### Contact

If you have any questions or suggestions, please open an issue or contact me.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.
