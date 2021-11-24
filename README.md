# qgis-xyz-sources
A simple script to add multiple XYZ tile sources to QGIS.

![XYZ Tiles in QGIS](/tiles.png)

The [script](/qgis_xyz_sources.py) should be copied and pasted into the QGIS python console (Plugins > Python Console) or `Ctrl + Alt + P`. Sources from Mapbox can be added by uncommenting the relevant section of the script and populating the `mapbox_key` variable with your API key.

This script was modified from the original by [Klas Karlsson](https://github.com/klakar/QGIS_resources/blob/master/collections/Geosupportsystem/python/qgis_basemaps.py) to include additional Mapbox sources.