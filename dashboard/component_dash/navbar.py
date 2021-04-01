""" Module name

Created by Antony Correia
Python Docstring
"""

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

search_bar = dbc.Row(
    [
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


