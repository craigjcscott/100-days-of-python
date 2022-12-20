import pandas as pd

squirrels = pd.read_csv("squirrel_census.csv")

fur_colors = squirrels["Primary Fur Color"]
fur_color_counts = fur_colors.value_counts()

fur_color_counts.to_csv("fur_color_counts.csv")
