import pandas as pd
import plotly.express as px

def create_bar_chart(filename):    
    # Read data from CSV file
    data = pd.read_csv(filename)

    # Create a bar graph using plotly
    fig = px.bar(data, x='name', y='dollar_price', color_discrete_sequence=['yellow'],
                labels={'Country': 'Cost of Whopper (USD)'}, title='The Whopper Index')

    fig.update_layout(
    plot_bgcolor='#262626',
    paper_bgcolor='#262626',
    font_color='white',
    font_family='Arial',
    font_size=18,
    title_font_family='Arial',
    title_font_color='white',
    title_font_size=24,
    legend_title_font_color='white',
    legend_title_font_size=20,
    legend_font_family='Arial',
    legend_font_color='white',
    legend_font_size=18,
    xaxis_title_font_family='Arial',
    xaxis_title_font_color='white',
    xaxis_title_font_size=20,
    yaxis_title_font_family='Arial',
    yaxis_title_font_color='white',
    )

    graph_html = fig.to_html()

    return graph_html