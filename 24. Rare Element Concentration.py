import pandas as pd
import numpy as np
from scipy.stats import t

data = pd.read_csv("rare_elements.csv")

n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level: "))
precision = float(input("Enter desired precision: "))

sample = data.iloc[:n, 0]

mean = np.mean(sample)
std = np.std(sample, ddof=1)
se = std / np.sqrt(n)

alpha = 1 - confidence / 100
t_value = t.ppf(1 - alpha / 2, n - 1)

margin = t_value * se
lower = mean - margin
upper = mean + margin

print("Sample Mean:", mean)
print("Confidence Interval:", lower, "to", upper)
print("Margin of Error:", margin)
