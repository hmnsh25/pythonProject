import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from fbprophet import Prophet

# Set your Alpha Vantage API key
api_key = 'EA8U92XABP0GZ0S3'

# Set the stock symbol and time interval
stock_symbol = 'IBM'  # Replace with the desired stock symbol
interval = 'weekly'

# Make a request to Alpha Vantage API to fetch weekly stock data
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={stock_symbol}&apikey={api_key}'
response = requests.get(url)

if response.status_code == 200:
    stock_data = response.json()['Weekly Time Series']

    # Convert stock data into a DataFrame
    df = pd.DataFrame.from_dict(stock_data, orient='index', columns=['Open', 'High', 'Low', 'Close', 'Volume'])
    df.index = pd.to_datetime(df.index)

    # Resample data to weekly frequency
    df = df.resample('W').last().dropna()

    # Prepare data for AI model (example: simple moving average)
    # df['SMA'] = df['Close'].rolling(window=5).mean()

    # Perform AI model prediction (example: using SMA as a predictor)
    # Replace this section with your own AI model implementation
    # Prepare data for ARIMA model
    closing_prices = df['Close']

    # Split data into train and test sets
    train_data = closing_prices[:int(0.8 * len(closing_prices))]
    test_data = closing_prices[int(0.8 * len(closing_prices)):]

    # Fit ARIMA model
    model = ARIMA(df['Close'].astype(float), order=(1, 1, 1))
    model_fit = model.fit()

    # Generate predictions
    predictions = model_fit.predict(start=len(df), end=len(df) + 30)

    # Combine train and test predictions
    all_predictions = pd.concat([train_data, predictions])
    # Plot the actual and predicted data
    plt.figure(figsize=(12, 6))
    # plt.plot(df.index, df['Close'], label='Actual')
    # plt.plot(df.index, df['SMA'], label='Predicted')
    # plt.title(f'{stock_symbol} Stock Price Prediction')
    plt.plot(closing_prices.index, closing_prices, label='Actual')
    plt.plot(all_predictions.index, all_predictions, label='Predicted')
    plt.title(f'{stock_symbol} Stock Price Prediction using ARIMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

else:
    print(f"Error fetching stock data. Status code: {response.status_code}")
