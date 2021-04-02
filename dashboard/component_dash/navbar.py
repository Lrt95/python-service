""" Module name

Created by Antony Correia
Python Docstring
"""

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

PLOTLY_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

select = dbc.Select(
    id="select",
    options=[
        {"label": "5 minutes", "value": "5m"},
        {"label": "15 minutes", "value": "15m"},
        {"label": "1 hour", "value": "1h"},
        {"label": "3 hours", "value": "3h"},
        {"label": "6 hours", "value": "6h"},
        {"label": "12 hours", "value": "12h"},
        {"label": "24 hours", "value": "24h"},
        {"label": "2 days", "value": "2d"}
    ],
)

search_bar = dbc.Row(
    [
        dbc.Col(select),
        dbc.Col(dbc.Input(type="search", placeholder="Agent", id='input_agent')),
        dbc.Col(
            dbc.Button("Ok", color="primary", className="ml-2", id='button_agent'),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)



navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Dash Board Python-Service", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            )
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)


