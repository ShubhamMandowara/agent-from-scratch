from ollama import chat
from ollama import ChatResponse
import yfinance as yf
import pandas as pd
import streamlit as st


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


def current_pe_ratio(symbol:str,) -> int:
   """Get current pe ratio for a stock
   Args:
    symbol (str): stock symbol
    
   Returns:
    int: current pe ratio
   """
   suffix = '.NS'
   stock = yf.Ticker(symbol+suffix)
   return stock.info.get('trailingPE', None)



st.title('AI Stock Data Retriever')
st.write("Enter a query, and the AI agent will find the stock name and retrieve its data and PE ratio")
user_query = st.text_input("Enter your query about a stock: get 1 year stock prices of TCS")

if st.button('Query'):
    if user_query:
        with st.spinner("Analyzing query..."):
            messages = [{'role': 'user', 'content': user_query}]
            print('Prompt:', messages[0]['content'])

            available_functions = {
            'get_stock_prices': get_stock_prices,
            'current_pe_ratio': current_pe_ratio,
            }

            response: ChatResponse = chat(
            'llama3.2:1b',
            messages=messages,
            tools=[get_stock_prices, current_pe_ratio],
            )

            if response.message.tool_calls:
                # There may be multiple tool calls in the response
                for tool in response.message.tool_calls:
                    # Ensure the function is available, and then call it
                    if function_to_call := available_functions.get(tool.function.name):
                        print('Calling function:', tool.function.name)
                        print('Arguments:', tool.function.arguments)
                        output = function_to_call(**tool.function.arguments)
                        if type(output) == pd.DataFrame:
                            st.dataframe(output)
                        else:
                            st.write(output)
                        print('Function output:', output)
                    else:
                        print('Function', tool.function.name, 'not found')

            # Only needed to chat with the model using the tool call results
            if response.message.tool_calls:
                # Add the function response to messages for the model to use
                messages.append(response.message)
                messages.append({'role': 'tool', 'content': str(output), 'name': tool.function.name})

                # Get final response from model with function outputs
                final_response = chat('llama3.2:1b', messages=messages)
                print('Final response:', final_response.message.content)

            else:
                print('No tool calls returned from model')