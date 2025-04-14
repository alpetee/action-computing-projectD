"""
Author: Allie Peterson
Disclaimer: This is showing a misleading story. See the 'Source of Truth' section in the README.
"""

import dash_html_components as html
import dash_core_components as dcc

def make_card(title, children):
    return html.Div(
        className="card",
        children=[
            html.H3(title),
            html.Div(className="card-content", children=children)
        ]
    )

def make_dropdown(id, label, options, value, multi=False):
    return html.Div([
        html.Label(label, htmlFor=id),
        dcc.Dropdown(
            id=id,
            options=options,
            value=value,
            multi=multi,
            clearable=not multi
        )
    ])

def make_slider(id, label, min, max, value, marks=None):
    return html.Div([
        html.Label(label, htmlFor=id),
        dcc.RangeSlider(
            id=id,
            min=min,
            max=max,
            value=value,
            marks=marks,
            step=1,
            tooltip={"placement": "bottom", "always_visible": True}
        )
    ])