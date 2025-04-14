"""
Author: Allie Peterson
Disclaimer: This is showing a misleading story. See the 'Source of Truth' section in the README.
"""
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from utils.data_loader import load_and_process_data
from utils.figures import create_bar_chart, create_male_part_time_chart, create_male_unemployment_chart

app = dash.Dash(__name__)
server = app.server

# Load and process data
df = load_and_process_data()

# Get available years
available_years = sorted(df['Year'].unique())

app.layout = html.Div([
    html.Div(
        className="banner",
        children=[
            html.H1("Women Poaching Jobs in the US"),
            html.P("Visualizing gender employment metrics | Allie Peterson")
        ]
    ),

    html.Div(
        className="container",
        children=[
            html.Div(
                className="controls",
                children=[
                    html.Div(
                        className="year-selector-container",  # New container class
                        children=[
                            html.H3("Year Selection", className="year-selector-title"),
                            dcc.Dropdown(
                                id='year-selector',
                                options=[{'label': str(year), 'value': year} for year in available_years],
                                value=available_years[-1],
                                clearable=False,
                                className='dark-dropdown compact-dropdown'  # Added compact class
                            )
                        ]
                    )
                ]
            ),

            html.Div(
                className="graphs",
                children=[
                    dcc.Graph(id="industry-wage-comparison"),
                    dcc.Graph(figure=create_male_part_time_chart(df)),
                    dcc.Graph(figure=create_male_unemployment_chart(df))
                ]
            )
        ]
    )
])


@app.callback(
    Output("industry-wage-comparison", "figure"),
    [Input("year-selector", "value")]
)
def update_bar_chart(selected_year):
    return create_bar_chart(df, selected_year)


if __name__ == "__main__":
    app.run_server(debug=True)