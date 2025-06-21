from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

df = pd.read_csv(r"C:\Users\conif\Documents\Projects\Python\python-data\shades.csv")
my_group = df['group'].unique().tolist()
my_group.sort()


# Create a Dash application
# and add a dropdown component to select a brand
app = Dash()
app.layout = html.Div([
    dcc.Dropdown(df.brand.unique(),'Revlon', id='demo-dropdown'),
    html.Div(id='dd-output-container'),
    dcc.RadioItems(options=my_group, id='radio-items')
])

@callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value'),
    Input('radio-items', 'value')
)
def update_output(dropdown_value, radio_value):
    return f'You have selected brand: {dropdown_value} and group: {radio_value}'



if __name__ == '__main__':
    app.run(debug=True)