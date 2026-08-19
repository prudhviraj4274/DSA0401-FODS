13. Scenario: You are a data analyst working for a finance company. Your team is interested in
analyzing the variability of stock prices for a particular company over a certain period. The company's
stock data includes the closing prices for each trading day of the specified period.

import pandas as pd
import numpy as np

stock_data = pd.DataFrame({
    "Close":[100,105,110,108,115,120]
})

mean_price = np.mean(stock_data["Close"])
std_price = np.std(stock_data["Close"])

print("Mean Price:", mean_price)
print("Standard Deviation:", std_price)
