import pandas as pd

likes_data = pd.DataFrame({
    "Likes":[100,200,100,150,200,300,100,150,250,300]
})

frequency = likes_data["Likes"].value_counts()

print(frequency)
