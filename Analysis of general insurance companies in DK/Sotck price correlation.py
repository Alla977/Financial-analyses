

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

start = dt.datetime(2018,1,1)
end = dt.datetime.now()

tickers = ["ALMB.CO","TRYG.CO","SAMPO.HE","TOP.CO"]
colnames = []

for ticker in tickers:
    data = yf.download(ticker,start = start, end = end)
    data = data.rename(columns={'Adj Close': ticker})
    if len(colnames) == 0:
        combined = data[[ticker]].copy()
        colnames.append(ticker)
    else:
        combined = combined.join(data[[ticker]])

for ticker in tickers:
    plt.plot(combined[ticker], label=ticker)
    plt.yscale("log")
plt.legend(loc = "upper right")
plt.show()

corr_data = combined.pct_change().corr(method='pearson')
sns.heatmap(corr_data,annot=True,cmap="coolwarm")
plt.show()