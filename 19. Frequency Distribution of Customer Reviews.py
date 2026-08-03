from collections import Counter

reviews = """
This product is good.
This product is excellent.
Good quality product.
"""

reviews = reviews.lower()

words = reviews.split()

frequency = Counter(words)

print(frequency)
