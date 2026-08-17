import numpy as np
from scipy.stats import t

drug = np.array([12,10,15,11,13,14,16,12,15,13])
placebo = np.array([5,6,4,7,5,6,5,4,7,6])

def confidence_interval(data):
    mean = np.mean(data)
    se = np.std(data, ddof=1) / np.sqrt(len(data))
    margin = t.ppf(0.975, len(data)-1) * se
    return mean-margin, mean+margin

print("Drug Group CI:", confidence_interval(drug))
print("Placebo Group CI:", confidence_interval(placebo))
