# import requests
# api_key = 'EA8U92XABP0GZ0S3'
#
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}'
# r = requests.get(url)
# data = r.json()
#
# print(data)


import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Get your Alpha Vantage API key from https://www.alphavantage.co/
API_KEY = "EA8U92XABP0GZ0S3"

# Set the symbol of the stock you want to get data for
SYMBOL = "IBM"

# Set the time frame for the data you want to get
TIME_FRAME = "5min"

# Create the URL for the API request
URL = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey={}".format(SYMBOL, API_KEY)

# Make the API request
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Get the data from the response
    data = response.json()
    print(data)
    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data['Weekly Time Series'])
    print(df)
    print(df.keys())
    # Plot the stock price over time
    plt.plot(df['Close'])

    # Create a model to predict future values
    model = ARIMA(df['Close'], order=(5, 1, 1))
    model.fit()

    # Predict the future values
    predictions = model.predict(start=len(df), end=len(df) + 30)

    # Plot the predictions
    plt.plot(predictions, 'r')

    # Show the plot
    plt.show()
else:
    print("Error: {} {}".format(response.status_code, response.reason))