from flask import Flask, render_template
import geopandas as gpd
import pandas as pd
import folium

gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# data = pd.read_csv('BKW_data.csv')

# # Get the unique countries
# countries_to_mark = data['name'].unique().tolist()

# gdf = gdf[gdf['name'].isin(countries_to_mark)]

app = Flask(__name__)

def generate_map(filename):
    data = pd.read_csv(filename)

    # Get the unique countries
    countries_to_mark = data['name'].unique().tolist()

    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    gdf = gdf[gdf['name'].isin(countries_to_mark)]

    m = folium.Map(location=[0, 0], zoom_start=1, min_zoom=2, tiles='cartodbdark_matter', max_bounds=True)

    for _, r in gdf.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,
                               style_function=lambda x: {'fillColor': 'yellow', 'color': 'yellow'},
                               tooltip=r['name'])

        geo_j.add_to(m)

    return m._repr_html_()