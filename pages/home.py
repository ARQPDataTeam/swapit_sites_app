from dash import html, register_page  #, callback # If you need callbacks, import it here.


register_page(
    __name__,
    name='SWAPIT HOME PAGE',
    top_nav=True,
    path='/',
    requests_pathname_prefix="/webapp-SWAPIT/",
    routes_pathname_prefix="/webapp-SWAPIT/"

)


def layout():
    layout = html.Div([
        html.H1(
            [
                "Home Page"
            ]
            ),
        html.Div(html.H4("""Welcome to the Data Team SWAPIT 
                            test data display dashboard home page.  
                            Below are the available data sets 
                            that can be visualized by following
                            the links above."""
                        )
                ),
        html.Div(className='gap',style={'height':'10px'}),
        html.Div([
            html.Div(children="""University of Toronto Scarborough Site""",className="box1",
                        style={
                        'backgroundColor':'aqua',
                        'color':'black',
                        'height':'100px',
                        'margin-left':'10px',
                        'width':'45%',
                        'text-align':'center',
                        'display':'inline-block'
                        }
                    ),
            html.Img(src='assets/utsc.jpg', alt='UTSC Site Photo'),
                ]),
        html.Div(className='gap',style={'height':'10px'}),
        html.Div([
            html.Div(children="""High Park Site""",className="box1",
                        style={
                        'backgroundColor':'aqua',
                        'color':'black',
                        'height':'100px',
                        'margin-left':'10px',
                        'width':'45%',
                        'text-align':'center',
                        'display':'inline-block'
                        }
                    ),
            html.Img(src='assets/high_park.jpg', alt='High Park Site Photo'),
                ]),
        html.Div(className='gap',style={'height':'10px'}),
        html.Div([
            html.Div(children="""Evergreen Brickworks Site""",className="box1",
                        style={
                        'backgroundColor':'aqua',
                        'color':'black',
                        'height':'100px',
                        'margin-left':'10px',
                        'width':'45%',
                        'text-align':'center',
                        'display':'inline-block'
                        }
                    ),
            html.Img(src='assets/evb.jpg', alt='Evergreen Brickworks Site Photo'),
                ]),            
            ])
    return layout