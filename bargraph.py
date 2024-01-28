import pandas as pd
import plotly.express as px

def create_bar_chart():    
    # Read data from CSV file
    file_path = 'BKW_data.csv'
    data = pd.read_csv(file_path)

    # Create a bar graph using plotly
    fig = px.bar(data, x='name', y='dollar_price', color='dollar_price', color_continuous_scale='Bluered_r',
                labels={'name': 'Country', 'dollar_price': 'Cost of Whopper (USD)'}, 
                title='The Whopper Index', hover_data=['name', 'dollar_price'])

    fig.update_layout(
        plot_bgcolor= '#262626',
        paper_bgcolor='#262626',
        font_color='White',
        font_family='Arial',
        font_size=18,
        title_font_family='Arial',
        title_font_color='black',
        title_font_size=24,
        legend_title_font_color='White',
        legend_title_font_size=20,
        legend_font_family='Arial',
        legend_font_color='White',
        legend_font_size=18,
        xaxis_title_font_family='Arial',
        xaxis_title_font_color='White',
        xaxis_title_font_size=20,
        yaxis_title_font_family='Arial',
        yaxis_title_font_color='White',
        yaxis_title_font_size=20,
    )

    graph_html = fig.to_html()

    return graph_html