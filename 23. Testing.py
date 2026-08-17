import numpy as np
from scipy.stats import ttest_ind

A = np.array([12,15,14,16,15,17,18,14,16,15])
B = np.array([10,11,12,13,12,11,10,12,13,11])

t_stat, p_value = ttest_ind(A, B)

print("t-value:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Significant Difference")
else:
    print("No Significant Difference")
