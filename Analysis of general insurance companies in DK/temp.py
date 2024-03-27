import pandas as pd
import yfinance as yf

# Specify the stock you want to analyze (e.g., Medco)
MEDC = yf.Ticker("ALMB.CO")
print(MEDC.financials)