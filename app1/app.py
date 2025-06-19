from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

df = pd.read_csv(r"C:\Users\conif\Documents\Projects\Python\python-data\shades.csv")
print(df.head())
