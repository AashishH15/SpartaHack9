import pandas as pd
import plotly.express as px

def create_bar_chart(filename):    
    data = pd.read_csv(filename)

    fig = px.bar(data, x='name', y='dollar_price', color='dollar_price', color_continuous_scale='YlOrRd',
                labels={'Country': 'Cost of Whopper (USD)'}, title='The Whopper Index')

    fig.update_traces(marker_line_width=1.5, marker_line_color='rgb(8,48,107)')

    fig.update_layout(
        plot_bgcolor="#262626",
        paper_bgcolor='#262626',
        font_color='white',
        font_family='Arial, sans-serif',
        font_size=18,
        title_font_family='Arial, sans-serif',
        title_font_color='white',
        title_font_size=24,
        legend_title_font_color='white',
        legend_title_font_size=20,
        legend_font_family='Arial, sans-serif',
        legend_font_color='white',
        legend_font_size=18,
        xaxis_title_font_family='Arial, sans-serif',
        xaxis_title_font_color='white',
        xaxis_title_font_size=20,
        yaxis_title_font_family='Arial, sans-serif',
        yaxis_title_font_color='white',
        yaxis_title_font_size=20,
        coloraxis_colorbar=dict(
            title="Price",
            thicknessmode="pixels", thickness=50,
            lenmode="pixels", len=200,
            yanchor="top", y=1,
            ticks="outside", ticksuffix=" USD",
            dtick=5
        )
    )

    graph_html = fig.to_html()

    return graph_html