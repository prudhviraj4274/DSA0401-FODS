from collections import Counter

text = open("sample_text.txt", "r").read().lower()

words = text.split()

frequency = Counter(words)

print(frequency)
