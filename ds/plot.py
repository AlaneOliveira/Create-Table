import yfinance as yf
import plotly.express as px

def plot_price(ticker):

    """_sumary

    return 
    """
    data = yf.download(
        ticker,
        multi_level_index= False
    )
    fig = px.line(
        data.reset_index(),
        x = 'Date', y= ['Close'],
    )

    return fig