from flask import Flask, render_template_string
import geopandas as gpd
import folium

# Load a GeoDataFrame
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

app = Flask(__name__)

@app.route('/')
def map():
    # Create a map
    m = folium.Map(location=[0, 0], zoom_start=2)
    
    # Add the GeoDataFrame to the map
    for _, r in gdf.iterrows():
        # Simplify the geometry if it's too complex. Otherwise, the browser may struggle to render it
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,
                               style_function=lambda x: {'fillColor': 'orange'})
        folium.Popup(r['name']).add_to(geo_j)
        geo_j.add_to(m)
    
    # Return the map as an HTML
    return m._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)