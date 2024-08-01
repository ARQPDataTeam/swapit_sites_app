from dash import html
import dash_bootstrap_components as dbc


def create_navbar():
    print ('loading navbar')
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink("Map", active=True, href="/map", target="_blank")
                ),

            dbc.NavItem(
                dbc.NavLink("UTSC", active=True, href="/utsc", target="_blank")
                ),

            dbc.NavItem(
                dbc.NavLink("High Park", active=True, href="/high_park", target="_blank")
                ),

            dbc.NavItem(
                dbc.NavLink("Evergreen Brickworks", active=True, href="/evb", target="_blank")
                ),

            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="fa-brands fa-linkedin"),  # Font Awesome Icon
                        " "  # Text beside icon
                    ],
                    href="[YOUR LINKEDIN PROFILE URL]",
                    target="_blank"
                )

            ),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                children=[  # Add as many menu items as you need
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Map", href='/map'),
                    dbc.DropdownMenuItem("UTSC", href='/utsc'),
                    dbc.DropdownMenuItem("High Park", href='/high_park'),
                    dbc.DropdownMenuItem("Evergreen Brickworks", href='/evb'),
                ],
            ),
        ],
        brand='Home',
        brand_href="/",
        # sticky="top",  # Uncomment if you want the navbar to always appear at the top on scroll.
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar