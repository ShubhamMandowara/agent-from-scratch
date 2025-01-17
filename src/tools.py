from typing import Any
import yfinance as yf
import pandas as pd
def get_parameter(symbol, parameter: str) -> Any:
    """Retrieve a value for a specific parameter from the data dictionary.

    Args:
        symbol (str): stock symbol
        parameter (str): The key representing the parameter.

    Returns:
        Any: The value of the parameter, or a message if not found.
    """
    suffix = '.NS'
    stock = yf.Ticker(symbol+suffix)
    return stock.info.get(parameter, None)

def get_address1(symbol:str) -> str:
    """Retrieve address1.
    Args:
        symbol (str): Stock symbol
    Return:
        str: address
    """
    return get_parameter(symbol, 'address1')


def get_current_price(symbol:str) -> float:
    """Retrieve the current stock price.
    Args:
        symbol (str): Stock symbol
    Return:
        float: price
    """
    return f"Current Price of {symbol} : {get_parameter(symbol, 'currentPrice')}"


def get_marketcap(symbol:str) -> float:
    """Retrieve the marketcap
    Args:
        symbol (str): Stock symbol
    Return:
        float: price
    """
    return f"MarketCap  of {symbol}: {get_parameter(symbol, 'marketCap')}"

def get_beta(symbol:str) -> float:
    """Retrieve the beta
    Args:
        symbol (str): Stock symbol
    Return:
        float: price
    """
    return f"Beta  of {symbol}:{get_parameter(symbol, 'beta')}"

def get_stock_prices(symbol:str, duration:str) -> pd.DataFrame:
    """Get stock prices from yahoo finance api
    Args:
        symbol (str): stock symbol
        duration (str): time duration
    Returns:
        pd.DataFrame: stock prices
    """
    suffix='.NS'
    durations = {'1 year': '1y', '1month': '1mo', '1 month': '1mo', '1M': '1mo', '1year': '1y'}
    if duration not in durations:
       durations[duration] = duration
    try:
            stock = yf.Ticker(symbol+suffix)
            data = stock.history(period=durations[duration])
            return data
    except Exception as e:
        return None


def current_pe_ratio(symbol:str) -> int:
   """Get current pe ratio for a stock
   Args:
    symbol (str): stock symbol
    
   Returns:
    int: current pe ratio
   """
   return f"Current PE ratio of {symbol} : {get_parameter(symbol, 'trailingPE')}"



def get_52_week_low(symbol: str) -> float:
    """Retrieve the 52 week low price
    Args:
        symbol (str): Stock symbol
    Return:
        float: 52week low price
    """
    return f"52 week low price of {symbol} : {get_parameter(symbol, 'fiftyTwoWeekLow')}"

def get_52_week_high(symbol: str):
    """Retrieve the debt-to-equity
    Args:
        symbol (str): Stock symbol
    Return:
        float: 52 week high prices
    """
    return f"52 week high price of {symbol}: {get_parameter(symbol, 'fiftyTwoWeekHigh')}"

def get_price_to_book(symbol: str):
    """Retrieve the price to book value
    Args:
        symbol (str): Stock symbol
    Return:
        float: price to book value
    """
    return f"Price to book value of {symbol} : {get_parameter(symbol, 'priceToBook')}"

def get_eps(symbol: str) -> float:
    """Retrieve the get EPS
    Args:
        symbol (str): Stock symbol
    Return:
        float: EPS
    """
    return f"EPS of {symbol} : {get_parameter(symbol, 'trailingEps')}"

def get_current_ratio(symbol: str)-> float:
    """Retrieve the current ratio
    Args:
        symbol (str): Stock symbol
    Return:
        float: current ratio
    """
    return f"Current ratio of {symbol}: {get_parameter(symbol, 'currentRatio')}"

def get_debt_to_equity(symbol: str)-> float:
    """Retrieve the debt-to-equity
    Args:
        symbol (str): Stock symbol
    Return:
        float: debt to equity
    """
    return f"Debt to equity of {symbol} : {get_parameter(symbol, 'debtToEquity')}"

def get_free_cash_flow(symbol: str):
    """Retrieve the free cash flow
    Args:
        symbol (str): Stock symbol
    Return:
        float: cashflow
    """
    return f"Free cashflow of {symbol} : {get_parameter(symbol, 'freeCashflow')}"
