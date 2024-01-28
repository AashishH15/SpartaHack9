from flask import Flask, render_template
import geopandas as gpd
import pandas as pd
import folium
from branca.colormap import linear

# 
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# countries_to_mark = ['United States of America', 'China', 'Germany', 'India', 'Japan']
data = pd.read_csv('BKW_data.csv')

# Get the unique countries
countries_to_mark = data['name'].unique().tolist()

gdf = gdf[gdf['name'].isin(countries_to_mark)]

# Assuming 'cost' column is available in the 'data' DataFrame
cost_col = 'dollar_price'

# Create a linear colormap based on the cost column
colormap = linear.YlOrRd_09.scale(data[cost_col].min(), data[cost_col].max())

# Set up Flask app
app = Flask(__name__)

#

def generate_map():
    m = folium.Map(location=[0, 0], zoom_start=1, min_zoom=2, tiles='cartodbdark_matter', max_bounds=True)

    for _, r in gdf.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()

        # Use the cost value to determine the color
        cost_value = data.loc[data['name'] == r['name'], cost_col].values[0]
        color = colormap(cost_value)

        geo_j = folium.GeoJson(data=geo_j,
                               style_function=lambda x: {'fillColor': red, 'color': yellow},
                               tooltip=f"{r['name']} - Cost: {cost_value}")

        geo_j.add_to(m)

    colormap.add_to(m)  # Add the colormap to the map for reference

    return m._repr_html_()
