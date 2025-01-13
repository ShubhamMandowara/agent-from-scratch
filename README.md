## AI Stock Data Retriever

### Overview
The **AI Stock Data Retriever** is a Streamlit application that integrates with the `llama3.2:1b` model (via the Ollama library) and Yahoo Finance API. This app processes natural language queries to retrieve stock data, including historical prices and the Price-to-Earnings (PE) ratio.

### Features
- **Natural Language Query Handling**: Users can input queries like "Get 1 year stock prices of TCS," and the AI processes the query to determine the stock symbol and required data.
- **Stock Price Retrieval**: Fetch historical stock prices for a specified duration using the Yahoo Finance API.
- **PE Ratio Retrieval**: Get the current Price-to-Earnings ratio of a stock.
- **Streamlit Integration**: A user-friendly interface for query input and displaying results.

---

### Setup Instructions

#### Prerequisites
1. **Python 3.7+**
2. Required libraries:
   - `ollama`
   - `yfinance`
   - `pandas`
   - `streamlit`

#### Installation
1. Clone the repository or save the script to your local machine.
2. Install the required dependencies:
   ```bash
   pip install ollama yfinance pandas streamlit
   ```

#### Starting the App
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the provided URL in your browser to interact with the app.

---

### Code Details

#### Key Components
1. **`get_stock_prices(symbol: str, duration: str) -> pd.DataFrame`**:
   - Fetches historical stock prices for a given symbol and duration.
   - Uses Yahoo Finance API to query data.

2. **`current_pe_ratio(symbol: str) -> int`**:
   - Retrieves the current Price-to-Earnings ratio of a stock using Yahoo Finance.

3. **AI Integration**:
   - The `llama3.2:1b` model processes the user's query and determines the required data.
   - The model calls the appropriate Python functions (`get_stock_prices` or `current_pe_ratio`) using function calling capabilities provided by the Ollama library.

4. **Streamlit Interface**:
   - Accepts user input and displays the results interactively.

---

### How It Works
1. **User Query**: The app accepts a natural language query about a stock.
2. **AI Processing**: The query is passed to the `llama3.2:1b` model via the Ollama library.
3. **Function Execution**:
   - Based on the AI’s response, the appropriate function (`get_stock_prices` or `current_pe_ratio`) is executed.
4. **Result Display**:
   - If the function returns a DataFrame (e.g., stock prices), it is displayed in a table.
   - For single values (e.g., PE ratio), the result is shown as text.

---

### Example Queries
- "Get 1 year stock prices of TCS."
- "What is the current PE ratio of Infosys?"
- "Fetch 1 month stock prices for Reliance."

---

### Troubleshooting
1. **Ollama Connection Issues**:
   - Ensure Ollama is running locally.
   - Verify the `llama3.2:1b` model is available and loaded in Ollama.
2. **Yahoo Finance API Errors**:
   - Confirm the stock symbol and duration are valid.
   - Check your internet connection for API requests.

---

### Future Enhancements
- Add support for multiple stock exchanges and suffixes.
- Implement error handling for invalid queries or symbols.
- Extend functionality to include other stock metrics, such as dividends or EPS.

Let me know if you need further customization or clarification!