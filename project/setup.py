import json
import pandas as pd

from project.functionality import (all_cars,
                                   unique_cars,
                                   average_horse_power,
                                   most_heaviest_cars,
                                   cars_made_by_each_manufacturer,
                                   number_of_cars_made_by_each_manufacturer,
                                   number_of_cars_made_each_year,
                                   save_dataset_to_a_csv_file)

with open("cars.json") as datafile:
    data = json.load(datafile)
df = pd.DataFrame(data)


print(all_cars(df))
print(unique_cars(df))
print(average_horse_power(df))
print(most_heaviest_cars(df))
print(number_of_cars_made_by_each_manufacturer(df))
print(number_of_cars_made_each_year(df))
save_dataset_to_a_csv_file(df)
