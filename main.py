from flask import Flask, render_template
import geopandas as gpd
import folium

gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

countries_to_mark = ['United States of America', 'China', 'Germany', 'India', 'Japan']

gdf = gdf[gdf['name'].isin(countries_to_mark)]

app = Flask(__name__)

def generate_map():
    m = folium.Map(location=[0, 0], zoom_start=2, tiles='OpenStreetMap', min_zoom=2)

    for _, r in gdf.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,
                               style_function=lambda x: {'fillColor': 'orange'})

        folium.Marker(
            location=[r['geometry'].centroid.y, r['geometry'].centroid.x],
            popup=folium.Popup(r['name']),
            icon=folium.Icon(color="black", icon="cutlery")
        ).add_to(m)

        geo_j.add_to(m)

    return m._repr_html_()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map-content')
def map_content():
    map_html = generate_map()
    return map_html

if __name__ == '__main__':
    app.run(debug=True)