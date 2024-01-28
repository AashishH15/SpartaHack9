from flask import Flask, render_template
from map import generate_map

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map-content')
def map_content():
    map_html = generate_map()
    return map_html

if __name__ == '__main__':
    app.run(debug=True)