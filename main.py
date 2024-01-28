from flask import Flask, render_template, send_file, request, jsonify
from map import generate_map
from bargraph import create_bar_chart
from flask import send_from_directory
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<filename>')
def update_content(filename):
    generate_map(filename)
    create_bar_chart(filename)

@app.route('/map-content')
def map_content():
    filename = request.args.get('filename', 'MCD_data.csv')
    map_html = generate_map(filename)
    return map_html

@app.route('/info.csv')
def serve_csv():
    return send_file('info.csv', mimetype='text/csv')

@app.route('/bar-graph-content')
def bar_graph_content():
    filename = request.args.get('filename', 'MCD_data.csv')
    bar_graph_html = create_bar_chart(filename)
    return bar_graph_html

@app.route('/download-gdp-data')
def download_gdp_data():
    return send_from_directory('.', 'gdp.json', as_attachment=True)

@app.route('/download-BKW-data')
def download_BKW_data():
    return send_from_directory('.', 'BKW.json', as_attachment=True)

@app.route('/download-MCD-data')
def download_MCD_data():
    return send_from_directory('.', 'MCD.json', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)