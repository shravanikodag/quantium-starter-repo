import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df=pd.read_csv('data/final_result.csv')
df["region"] = df["region"].str.lower()

df["date"] = pd.to_datetime(df["date"])

df= df.sort_values("date")
# CREATE APP
app = Dash(__name__)

app.layout = html.Div(
    style = {
        'backgroundColor': '#333837',
        'padding':'20px',
        'fontFamily':'roboto',
        'textAlign':'left',
    },
    children = [
    html.H1("SOUL FOODS SALES DASHBOARD",style={'textAlign':'center'}),
    html.Div([html.Label("selecting Region:",style={'font-weight':'bold','font-size':'20px'}),
    dcc.RadioItems(id='region',options=[ {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},],
                   value="all",
                   inline=True,
                   style={
                    "marginTop": "10px",
                    "marginBottom": "20px"
                    }
                )

]),
    dcc.Graph(id="sales-chart")

])
@app.callback(
    Output("sales-chart","figure"),
    Input("region","value"),
)
def update_graph(selected_region):

    # Filter region
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Group by date
    sales_by_date = filtered_df.groupby("date")["sales"].sum().reset_index()

    # Create chart
    fig = px.line(
        sales_by_date,
        x="date",
        y="sales",
        title=f"Sales Trend - {selected_region.title()} Region",
        labels={
            "date": "Date",
            "sales": "Total Sales"
        }
    )

    # Add price increase marker
    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red",
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)
