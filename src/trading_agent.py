from ollama import chat
from ollama import ChatResponse
import pandas as pd
import streamlit as st
import plotly.express as px
from tools import (get_address1, get_beta, get_marketcap, get_current_price, get_stock_prices, current_pe_ratio, get_52_week_high,
                    get_52_week_low,get_current_ratio, get_debt_to_equity, get_free_cash_flow, get_eps, get_price_to_book)


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
            'get_current_price': get_current_price,
            'get_marketcap': get_marketcap,
            'get_beta': get_beta,
            'get_address': get_address1,
            'get_52_week_high':get_52_week_high,
            'get_52_week_low':get_52_week_low,
            'get_current_ratio':get_current_ratio,
            'get_debt_to_equity':get_debt_to_equity,
            'get_free_cash_flow':get_free_cash_flow,
            'get_eps':get_eps, 
            'get_price_to_book':get_price_to_book

            }

            response: ChatResponse = chat(
            'llama3.2:1b',
            messages=messages,
            tools=[get_stock_prices, current_pe_ratio, get_current_price, get_marketcap, get_beta, get_address1, get_52_week_high, get_52_week_low,
                    get_current_ratio, get_debt_to_equity, get_free_cash_flow, get_eps, get_price_to_book]
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
                            output.reset_index(inplace=True)
                            fig = px.line(output, x="Date", y="Close")
                            fig.update_yaxes(range=[output['Close'].min(), output['Close'].max()]) 
                            st.plotly_chart(fig)
                            st.dataframe(output)
                        else:
                            st.write(output)
                        print('Function output:', output)
                        messages.append(response.message)
                        messages.append({'role': 'tool', 'function output:': str(output), 'name': tool.function.name})

                        # Get final response from model with function outputs
                        final_response = chat('llama3.2:1b', messages=messages)
                        st.write(final_response.message.content)
                        print('Final response:', final_response.message.content)
                    else:
                        print('Function', tool.function.name, 'not found')