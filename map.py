from flask import Flask, render_template
import geopandas as gpd
import pandas as pd
import folium

gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# countries_to_mark = ['United States of America', 'China', 'Germany', 'India', 'Japan']
# data = pd.read_csv('BKW_data.csv')

# Get the unique countries
# countries_to_mark = data['name'].unique().tolist()

# gdf = gdf[gdf['name'].isin(countries_to_mark)]

app = Flask(__name__)

def generate_map(filename):
    data = pd.read_csv(filename)  # Load data based on the selected filename
    color = "#DD1423"
    ntitle = "Big Mac"
    print(filename)
    if filename == "BKW_data.csv":
        color = "#ED7903"
        ntitle = "Whopper"
    elif filename == "SWAY_data.csv":
        color = "#FFC919"
        ntitle = "Footlong"
    elif filename == "STBUCKS_data.csv":
        color = "#0C421A"
        ntitle = "Tall Latte"

    countries_to_mark = data['name'].unique().tolist()

    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    gdf = gdf[gdf['name'].isin(countries_to_mark)]

    # Merge gdf with data to include dollar_price
    gdf = gdf.merge(data, on='name')

    m = folium.Map(location=[0, 0], zoom_start=1, min_zoom=2, tiles='cartodbdark_matter', max_bounds=True)

    for _, r in gdf.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,
                               style_function=lambda x: {'fillColor': 'transparent', 'color': color},
                               tooltip=f"{r['name']}\n {ntitle}: ${r['dollar_price']}")

        geo_j.add_to(m)

    return m._repr_html_()