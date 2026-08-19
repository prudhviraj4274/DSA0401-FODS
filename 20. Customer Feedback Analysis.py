20. Scenario: You are a data analyst working for a marketing research company. Your team has
collected a large dataset containing customer feedback from various social media platforms. The
dataset consists of thousands of text entries, and your task is to develop a Python program to analyze
the frequency distribution of words in this dataset. Your program should be able to perform the
following tasks:
• Load the dataset from a CSV file (data.csv) containing a single column named "feedback" with
each row representing a customer comment.
• Preprocess the text data by removing punctuation, converting all text to lowercase, and
eliminating any stop words (common words like "the," "and," "is," etc. that don't carry
significant meaning).
• Calculate the frequency distribution of words in the preprocessed dataset.
• Display the top N most frequent words and their corresponding frequencies, where N is
provided as user input.
• Plot a bar graph to visualize the top N most frequent words and their frequencies.
Question: Create a Python program that fulfills these requirements and helps your team gain insights
from the customer feedback data.
    
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
