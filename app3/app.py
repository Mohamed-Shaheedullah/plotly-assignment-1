from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv(r"C:\Users\conif\Documents\Projects\Python\python-data\shades.csv")



app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.RangeSlider(df['L'].min(), df['L'].max(), 1, value=[5, 55], id='my-range-slider'),
    html.Div(id='output-container-range-slider')
])

@callback(
    Output('output-container-range-slider', 'children'),
    Input('my-range-slider', 'value'))
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run(debug=True)
