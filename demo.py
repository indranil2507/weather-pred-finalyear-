import pandas as pd
import numpy as np
data = pd.read_csv("austin_weather.csv")

# drop (delete) the unnecessary columns in the data
data = data.drop(
    ['Events', 'Date', 'SeaLevelPressureHighInches', 'SeaLevelPressureLowInches'], axis=1)

data = data.replace('T', 0.0)
data = data.replace('-', 0.0)

# Save the data in a csv file
data.to_csv('austin_final.csv')