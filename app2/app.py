from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

df = pd.read_csv(r"C:\Users\conif\Documents\Projects\Python\python-data\shades.csv")

app = Dash()


grid = dag.AgGrid(
    id="get-started-example-basic",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    columnSize="sizeToFit",
    dashGridOptions={"pagination": True, "paginationAutoPageSize": True},
)

app.layout = html.Div([grid])

if __name__ == "__main__":
    app.run(debug=True)
