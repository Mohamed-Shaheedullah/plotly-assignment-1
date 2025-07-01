from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px


df = pd.read_csv(r"C:\Users\conif\Documents\Projects\Python\python-data\shades.csv")

# Create a Plotly scatter plot
fig = px.scatter(
    df,
    x="V",
    y="S",
    title="V vs. S Scatter Plot",
)

# Initialize Dash app
app = Dash()

# Layout with the graph
app.layout = html.Div([
    html.H2("Shades Dataset Scatter Plot"),
    dcc.Graph(
        id='scatter-plot',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)