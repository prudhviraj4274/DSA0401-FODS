import pandas as pd
import numpy as np
from scipy.stats import t

data = pd.read_csv("customer_reviews.csv")

ratings = data["Rating"]

n = len(ratings)
mean = np.mean(ratings)
std = np.std(ratings, ddof=1)

se = std / np.sqrt(n)
t_value = t.ppf(0.975, n - 1)

margin = t_value * se

lower = mean - margin
upper = mean + margin

print("Mean Rating:", round(mean, 2))
print("95% Confidence Interval:", round(lower, 2), "to", round(upper, 2))
