from pycoingecko import CoinGeckoAPI
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd

cg = CoinGeckoAPI()

# Function to fetch Bitcoin data
def fetch_bitcoin_data():
    bitcoin_data = cg.get_coin_market_chart_by_id(id="bitcoin", vs_currency="usd", days=30)
    bitcoin_price = bitcoin_data["prices"]
    df = pd.DataFrame(bitcoin_price, columns=["TimeStamp", "Price"])
    df["date"] = pd.to_datetime(df["TimeStamp"], unit="ms")
    
    # Resample the data to 15-minute intervals
    df.set_index("date", inplace=True)
    df = df.resample("15T").agg({"Price": ["first", "max", "min", "last"]}).dropna()
    df.reset_index(inplace=True)
    
    # Keep only the latest 100 candles
    df = df.tail(100)
    
    return df

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='live-candlestick-chart'),
    dcc.Interval(
        id='interval-component',
        interval=6 * 1000,  # Update every 6 seconds
        n_intervals=0
    )
])

@app.callback(Output('live-candlestick-chart', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_candlestick_chart(n):
    df = fetch_bitcoin_data()
    
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                     open=df["Price"]["first"],
                     high=df["Price"]["max"],
                     low=df["Price"]["min"],
                     close=df["Price"]["last"],
                     increasing_line_color='green',  # Color for increasing candles
                     decreasing_line_color='red',  # Color for decreasing candles
                     line_width=5  # Width of the candlestick lines
                    )])

    fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Time',
                      yaxis_title='Price (USD $)', title='Live Bitcoin Candlestick Chart (Latest 100 Candles)')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
