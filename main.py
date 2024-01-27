from flask import Flask, render_template_string
import geopandas as gpd
import folium

gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

app = Flask(__name__)

@app.route('/')
def map():
    m = folium.Map(location=[0, 0], zoom_start=2)
    
    for _, r in gdf.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,
                               style_function=lambda x: {'fillColor': 'orange'})
        folium.Popup(r['name']).add_to(geo_j)
        geo_j.add_to(m)
    
    return m._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)