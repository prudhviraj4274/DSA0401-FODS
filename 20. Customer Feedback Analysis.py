import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string

data = pd.DataFrame({
    "feedback":[
        "Good product and good quality",
        "Excellent service and good support",
        "Product quality is excellent"
    ]
})

text = " ".join(data["feedback"]).lower()

text = text.translate(str.maketrans("", "", string.punctuation))

stop_words = {"the","and","is","a","an","of","to"}

words = [word for word in text.split() if word not in stop_words]

frequency = Counter(words)

N = int(input("Enter Top N: "))

top_words = frequency.most_common(N)

print(top_words)

x = [i[0] for i in top_words]
y = [i[1] for i in top_words]

plt.bar(x, y)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top Frequent Words")
plt.show()
