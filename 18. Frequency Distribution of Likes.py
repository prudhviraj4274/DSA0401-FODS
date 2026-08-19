18. Scenario: You are a data analyst working for a social media platform. As part of your analysis,
you have a dataset containing user interaction data, including the number of likes received by each
post. Your task is to develop a Python program that calculates the frequency distribution of likes among
the posts.
    
import pandas as pd

likes_data = pd.DataFrame({
    "Likes":[100,200,100,150,200,300,100,150,250,300]
})

frequency = likes_data["Likes"].value_counts()

print(frequency)
