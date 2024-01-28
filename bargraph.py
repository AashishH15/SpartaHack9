import pandas as pd
import plotly.express as px

def create_bar_chart():    
    # Read data from CSV file
    file_path = './info.csv'
    data = pd.read_csv(file_path)

    # Create a bar graph using plotly
    fig = px.bar(data, x='Country', y='Population (millions)', color='Currency',
                labels={'Population (millions)': 'Population (Millions)'}, title='Population of Countries')

    # Convert the plot to HTML
    graph_html = fig.to_html()

    return graph_html