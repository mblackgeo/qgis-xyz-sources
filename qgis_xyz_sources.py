# flake8: noqa
"""
This script should be run from the Python console inside QGIS:
It adds online sources to the QGIS Browser under XYZ Tiles.
Plugins > Python Console (Ctrl + Alt + P)

Optionally can add XYZ tiles from Mapbox by uncommenting the section below
and populating with your Mapbox API key.

Original script by Klas Karlsson.
Sources from https://qms.nextgis.com/.
Modified to include Mapbox tiles.
"""
from dataclasses import dataclass


# -----------------------------------------------------------------------------
# Data placeholders
# -----------------------------------------------------------------------------
@dataclass
class XYZSource:
    name: str
    url: str
    zmin: str = "0"
    zmax: str = "19"
    tilePixelRatio: str = "1"


sources = []

# -----------------------------------------------------------------------------
# Add Mapbox sources
# Uncomment this section and populate mapbox_key to include Mapbox XYZ tiles
# -----------------------------------------------------------------------------
# mapbox_key = "pk.abcdef..."
# styles = [
#     "streets-v11",
#     "outdoors-v11",
#     "light-v10",
#     "dark-v10",
#     "satellite-v9",
#     "satellite-streets-v11",
# ]

# for style in styles:
#     map_url = f"https://api.mapbox.com/styles/v1/mapbox/{style}/tiles/{{z}}/{{x}}/{{y}}?access_token={mapbox_key}"
#     sources.append(XYZSource(name="Mapbox {}".format(style), zmax="20", tilePixelRatio="2", url=map_url))


# -----------------------------------------------------------------------------
# Other XYZ sources
# e.g. Google, OSM, ESRI, etc.
# -----------------------------------------------------------------------------
sources.extend(
    [
        XYZSource(
            name="Google Maps",
            url="https://mt1.google.com/vt/lyrs=m&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D",
        ),
        XYZSource(
            name="Google Satellite",
            url="https://mt1.google.com/vt/lyrs=s&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D",
        ),
        XYZSource(
            name="Google Terrain",
            url="https://mt1.google.com/vt/lyrs=t&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D",
        ),
        XYZSource(
            name="Google Terrain Hybrid",
            url="https://mt1.google.com/vt/lyrs=p&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D",
        ),
        XYZSource(
            name="Google Satellite Hybrid",
            url="https://mt1.google.com/vt/lyrs=y&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D",
        ),
        XYZSource(
            name="Stamen Terrain",
            zmax="20",
            url="http://tile.stamen.com/terrain/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="Stamen Toner",
            zmax="20",
            url="http://tile.stamen.com/toner/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="Stamen Toner Light",
            zmax="20",
            url="http://tile.stamen.com/toner-lite/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="Stamen Watercolor",
            zmax="18",
            url="http://tile.stamen.com/watercolor/%7Bz%7D/%7Bx%7D/%7By%7D.jpg",
        ),
        XYZSource(
            name="Wikimedia Map",
            zmax="20",
            zmin="1",
            url="https://maps.wikimedia.org/osm-intl/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="Wikimedia Hike Bike Map",
            zmax="17",
            zmin="1",
            url="http://tiles.wmflabs.org/hikebike/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="Esri Boundaries Places",
            zmax="20",
            url="https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="Esri Gray (dark)",
            zmax="16",
            url="http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="Esri Gray (light)",
            zmax="16",
            url="http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="Esri National Geographic",
            zmax="12",
            url="http://services.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="Esri Ocean",
            zmax="10",
            url="https://services.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="Esri Satellite",
            zmax="17",
            url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="Esri Standard",
            zmax="17",
            url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="Esri Terrain",
            zmax="13",
            url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="Esri Transportation",
            zmax="20",
            url="https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="Esri Topo World",
            zmax="20",
            url="http://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D",
        ),
        XYZSource(
            name="OpenStreetMap Standard",
            zmax="19",
            url="http://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="OpenStreetMap H.O.T.",
            zmax="19",
            url="http://tile.openstreetmap.fr/hot/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="OpenStreetMap Monochrome",
            zmax="19",
            url="http://tiles.wmflabs.org/bw-mapnik/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="Strava All",
            zmax="15",
            url="https://heatmap-external-b.strava.com/tiles/all/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="Strava Run",
            zmax="15",
            url="https://heatmap-external-b.strava.com/tiles/run/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png?v=19",
        ),
        XYZSource(
            name="Open Weather Map Temperature",
            zmax="19",
            url="http://tile.openweathermap.org/map/temp_new/%7Bz%7D/%7Bx%7D/%7By%7D.png?APPID=1c3e4ef8e25596946ee1f3846b53218a",
        ),
        XYZSource(
            name="Open Weather Map Clouds",
            zmax="19",
            url="http://tile.openweathermap.org/map/clouds_new/%7Bz%7D/%7Bx%7D/%7By%7D.png?APPID=ef3c5137f6c31db50c4c6f1ce4e7e9dd",
        ),
        XYZSource(
            name="Open Weather Map Wind Speed",
            zmax="19",
            url="http://tile.openweathermap.org/map/wind_new/%7Bz%7D/%7Bx%7D/%7By%7D.png?APPID=f9d0069aa69438d52276ae25c1ee9893",
        ),
        XYZSource(
            name="CartoDb Dark Matter",
            zmax="20",
            url="http://basemaps.cartocdn.com/dark_all/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="CartoDb Positron",
            zmax="20",
            url="http://basemaps.cartocdn.com/light_all/%7Bz%7D/%7Bx%7D/%7By%7D.png",
        ),
        XYZSource(
            name="Bing VirtualEarth",
            zmax="19",
            zmin="1",
            url="http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1",
        ),
    ]
)

# -----------------------------------------------------------------------------
# Add sources to XYZ Tiles list in the QGIS browser
# -----------------------------------------------------------------------------
for src in sources:
    base = f"qgis/connections-xyz/{src.name}"
    QSettings().setValue(f"{base}/authcfg", "")
    QSettings().setValue(f"{base}/password", "")
    QSettings().setValue(f"{base}/referer", "")
    QSettings().setValue(f"{base}/url", src.url)
    QSettings().setValue(f"{base}/username", "")
    QSettings().setValue(f"{base}/zmax", src.zmax)
    QSettings().setValue(f"{base}/zmin", src.zmin)
    QSettings().setValue(f"{base}/tilePixelRatio", src.tilePixelRatio)

# Update GUI
iface.reloadConnections()
