# https://medium.com/@alamashad507/extracting-stock-data-using-python-yfinace-module-815cebfef6d9

import yfinance as yf
import pandas as pd
apple = yf.Ticker("AAPL")
apple_share_price = apple.history(period="max")
apple_share_price.reset_index(inplace=True)
apple_share_price.head()

apple_share_price.plot(x="Date", y="Open")

apple_dividends = apple.dividends.to_frame()
apple_dividends.reset_index(inplace=True)
apple_dividends.head()