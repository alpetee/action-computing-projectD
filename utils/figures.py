import plotly.express as px
import pandas as pd

# Color scheme
MALE_COLOR = '#2d77bb'  # Blue
FEMALE_COLOR = '#ae2901'  # Red

# Font settings
LARGE_FONT = dict(
    family="Arial, sans-serif",
    size=24,  # Increased from default
    color="white"
)

AXIS_TITLE_FONT = dict(
    family="Arial, sans-serif",
    size=20,  # Increased from default
    color="white"
)

TICK_FONT = dict(
    family="Arial, sans-serif",
    size=18,  # Increased from default
    color="white"
)

def create_bar_chart(df, selected_year):
    year_data = df[df['Year'] == selected_year].iloc[0]

    # Use exact column names from your data
    male_industry_col = 'Employment in industry, male (% of male employment) (modeled ILO estimate)'
    female_wage_col = 'Wage and salaried workers, female (% of female employment) (modeled ILO estimate)'

    comparison_df = pd.DataFrame({
        'Metric': [male_industry_col, female_wage_col],
        'Value': [year_data[male_industry_col], year_data[female_wage_col]],
        'Gender': ['Male', 'Female']
    })

    fig = px.bar(
        comparison_df,
        x='Gender',
        y='Value',
        color='Gender',
        color_discrete_map={'Male': MALE_COLOR, 'Female': FEMALE_COLOR},
        title=f"Gender Distribution in the Workforce ({selected_year})",
        labels={'Value': 'Percentage (%)'}
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Percentage (%)",
        showlegend=False,
        yaxis_range=[0, 100],
        plot_bgcolor='#031e40',
        paper_bgcolor='#031e40',
        font=LARGE_FONT,  # Apply large font to all text
        title_font=LARGE_FONT,  # Specifically for title
        xaxis=dict(
            title_font=AXIS_TITLE_FONT,
            tickfont=TICK_FONT
        ),
        yaxis=dict(
            title_font=AXIS_TITLE_FONT,
            tickfont=TICK_FONT
        )
    )

    fig.update_traces(
        texttemplate='%{y:.1f}%',
        textposition='inside',
        insidetextanchor='middle',
        textfont_size=168,  # Increased bar label size
        textfont_color='white',
        marker_line_width=2,
        marker_line_color='black',
        width=0.7
    )

    return fig


def create_male_part_time_chart(df):
    filtered = df[(df['Year'] >= 2009) & (df['Year'] <= 2019)]
    male_part_time_col = 'Part time employment, male (% of total male employment)'

    min_value = filtered[male_part_time_col].min()
    max_value = filtered[male_part_time_col].max()
    y_min = max(0, min_value * 0.95) if min_value > 0 else 0
    y_max = max_value * 1.05 if max_value > 0 else 5

    fig = px.line(
        filtered,
        x='Year',
        y=male_part_time_col,
        title="Male Employment (2009-2019)",
        color_discrete_sequence=[MALE_COLOR]
    )

    fig.update_layout(
        yaxis_title="Percentage (%)",
        yaxis_range=[y_min, y_max],
        margin=dict(t=40, b=40),
        plot_bgcolor='#031e40',
        paper_bgcolor='#031e40',
        font=LARGE_FONT,
        title_font=LARGE_FONT,
        xaxis=dict(
            title_font=AXIS_TITLE_FONT,
            tickfont=TICK_FONT
        ),
        yaxis=dict(
            title_font=AXIS_TITLE_FONT,
            tickfont=TICK_FONT
        )
    )
    fig.update_traces(line_width=15)

    return fig


def create_male_unemployment_chart(df):
    filtered = df[(df['Year'] >= 2019) & (df['Year'] <= 2020)]
    male_unemployment_col = 'Unemployment, male (% of male labor force) (national estimate)'

    min_value = filtered[male_unemployment_col].min()
    max_value = filtered[male_unemployment_col].max()
    y_min = max(0, min_value * 0.95) if min_value > 0 else 0
    y_max = max_value * 1.05 if max_value > 0 else 5

    fig = px.line(
        filtered,
        x='Year',
        y=male_unemployment_col,
        title="Male Unemployment (2019-2020)",
        color_discrete_sequence=[MALE_COLOR]
    )

    fig.update_layout(
        yaxis_title="Percentage (%)",
        yaxis_range=[y_min, y_max],
        margin=dict(t=40, b=40),
        plot_bgcolor='#031e40',
        paper_bgcolor='#031e40',
        font=LARGE_FONT,
        title_font=LARGE_FONT,
        xaxis=dict(
            title_font=AXIS_TITLE_FONT,
            tickfont=TICK_FONT
        ),
        yaxis=dict(
            title_font=AXIS_TITLE_FONT,
            tickfont=TICK_FONT
        )
    )
    fig.update_traces(line_width=15)

    return fig