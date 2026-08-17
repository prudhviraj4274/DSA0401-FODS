import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

control = np.array([120, 118, 125, 122, 119, 121, 124, 117])
treatment = np.array([110, 108, 112, 105, 109, 107, 111, 106])

t, p = ttest_ind(control, treatment)

print("p-value:", round(p, 4))

if p < 0.05:
    print("Significant effect")
else:
    print("No significant effect")

plt.boxplot([control, treatment],
            tick_labels=["Control", "Treatment"])

plt.title("Treatment vs Placebo")
plt.ylabel("Blood Pressure")
plt.show()
