import dash
from dash import Dash, html, dcc, callback 
from dash.exceptions import PreventUpdate
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime as dt
from datetime import date
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os
from dotenv import load_dotenv

from credentials import sql_engine_string_generator

print ('plotting High Park')

# register this as a page in the app
dash.register_page(__name__,
    requests_pathname_prefix="/webapp-SWAPIT/",
    routes_pathname_prefix="/webapp-SWAPIT/"
)

# set the sql engine string
sql_engine_string=sql_engine_string_generator('DATAHUB_PSQL_SERVER','DATAHUB_SWAPIT_DBNAME','DATAHUB_PSQL_USER','DATAHUB_PSQL_PASSWORD')
sql_engine=create_engine(sql_engine_string)


# sql query
sql_query="""
SET TIME ZONE 'GMT';
SELECT DISTINCT ON (datetime) * FROM (
	SELECT date_trunc('minute',datetime) AS datetime, no_r AS no, nox_r AS nox, tempa AS temp, press as press
	FROM hig__airp_v0
	WHERE no_r IS NOT NULL
	AND datetime >= '2024-03-01' AND datetime < '2024-03-01 01:00:00'
) AS airp
ORDER BY datetime;
"""

# create the dataframe from the sql query
airp_output_df=pd.read_sql_query(sql_query, con=sql_engine)

# print (airp_output_df)

airp_output_df.set_index('datetime', inplace=True)
airp_output_df.index=pd.to_datetime(airp_output_df.index)
beginning_date=airp_output_df.index[0]
ending_date=airp_output_df.index[-1]
today=dt.today().strftime('%Y-%m-%d')
# print(beginning_date, ending_date)
# use specs parameter in make_subplots function
# to create secondary y-axis


# plot a scatter chart by specifying the x and y values
# Use add_trace function to specify secondary_y axes.
def create_figure(df_index, species_1, species_2, plot_title, y_title_1, y_title_2):
    fig_1 = make_subplots(specs=[[{"secondary_y": True}]])
    fig_1.add_trace(
        go.Scatter(x=df_index, y=species_1, name="NO"),
        secondary_y=False)
    
    fig_1.add_trace(
        go.Scatter(x=df_index, y=species_2, name="NOx"),
        secondary_y=True,)

    # set axis titles
    fig_1.update_layout(
        template='simple_white',
        title=plot_title,
        xaxis_title="Date",
        yaxis_title=y_title_1,
        yaxis2_title=y_title_2,
        legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    )   
    )
    return fig_1

# set up the app layout
layout = html.Div(children=
                    [
                    html.H1(children=['SWAPIT High Park Airpointer Dashboard']),
                    html.Div(children=['Airpointer NOx plot display with date picker']),

                    dcc.DatePickerRange(
                        id='my-date-picker-range',
                        min_date_allowed=beginning_date,
                        max_date_allowed=ending_date
                    ),
                    dcc.Graph(id='airp-nox_plot',figure=create_figure(airp_output_df.index,airp_output_df['no'],airp_output_df['nox'],'UTSC AirP NO&NOx','NO (ppbv)','NOx (ppbv)')),
                    html.Div(className='gap',style={'height':'10px'}),
                    html.Div(children=['Airpointer Met plot display with date picker']),

                    dcc.DatePickerRange(
                        id='my-date-picker-range',
                        min_date_allowed=beginning_date,
                        max_date_allowed=ending_date
                    ),
                    dcc.Graph(id='airp-met_plot',figure=create_figure(airp_output_df.index,airp_output_df['temp'],airp_output_df['press'],'UTSC AirP Met','Temp (C)','Press (Pa)')),

                    ] 
                    )

# @app.callback(
#     Output('graph_2', 'figure'),
#     [Input('date-picker', 'start_date'),
#     Input('date-picker', 'end_date')],
#     [State('submit_button', 'n_clicks')])

@callback(
    Output('airp-nox_plot', 'figure'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))

def update_output(start_date, end_date):
    print (start_date, end_date)
    if not start_date or not end_date:
        raise PreventUpdate
    else:
        output_selected_df = airp_output_df.loc[
            (airp_output_df.index >= start_date) & (airp_output_df.index <= end_date), :
        ]
        return create_figure(output_selected_df)


# if __name__=='__main__':
#     app.run(debug=True)
