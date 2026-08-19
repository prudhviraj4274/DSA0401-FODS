19. Scenario: You are working on a project that involves analyzing customer reviews for a product.
You have a dataset containing customer reviews, and your task is to develop a Python program that
calculates the frequency distribution of words in the reviews.
Question: Develop a Python program to calculate the frequency distribution of words in the customer
reviews dataset?

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
