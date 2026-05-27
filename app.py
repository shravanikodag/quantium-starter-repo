import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df=pd.read_csv('data/final_result.csv')

df["date"] = pd.to_datetime(df["date"])

df= df.sort_values("date")

sales_by_date = df.groupby("date")["sales"].sum().reset_index()

fig = px.line(sales_by_date,x="date",y="sales",title="Pink Morsel Sales Over Time",
              labels={"date":"Date","sales":"Sales"})

app = Dash(__name__)

app.layout = html.Div([
    html.H1("DATA VISUALIZATION"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
