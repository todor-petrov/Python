import pandas as pd
import logging
import json
import csv

from cars_names_validator import cars_names_validator


class CarDataProcessor:
    def __init__(self, json_file):
        self.data = self.load_data(json_file)
        self.df = pd.DataFrame(self.data)

    @staticmethod
    def load_data(json_file):

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
                new_data = cars_names_validator(data)
            return new_data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f'Error loading JSON data: {str(e)}')
            return []

    def unique_cars_count(self):
        return len(self.df['Name'].unique())

    def average_horsepower(self):
        return self.df['Horsepower'].mean()

    def top_heaviest_cars(self, n=5):
        return self.df.nlargest(n, 'Weight_in_lbs')

    def cars_by_manufacturer(self):
        self.df['Manufacturer'] = self.df['Name'].str.split(' ').str[0]
        return self.df.groupby(['Manufacturer']).size()

    def cars_by_year(self):
        return self.df['Year'].value_counts()
        # self.df['Year'] = pd.to_datetime(self.df['Year'])
        # return self.df.groupby(self.df['Year'].dt.year).size()

    def save_to_csv(self, output_csv):
        self.df.to_csv(output_csv, index=False)


if __name__ == '__main__':
    logging.basicConfig(filename='car_data_processor.log', level=logging.INFO)

    # Input and output file paths
    input_json = 'cars.json'
    output_csv = 'car_data_output.csv'

    car_processor = CarDataProcessor(input_json)

    # Task 1: Print the number of unique cars
    unique_car_count = car_processor.unique_cars_count()
    print(f'Number of unique cars: {unique_car_count}')

    # Task 2: Print the average horsepower
    avg_horsepower = car_processor.average_horsepower()
    print(f'Average horsepower of all cars: {avg_horsepower}')

    # Task 3: Print the top 5 heaviest cars
    top_heaviest_cars = car_processor.top_heaviest_cars()
    print('Top 5 heaviest cars:')
    print(top_heaviest_cars)

    # Task 4: Print the number of cars made by each manufacturer
    cars_by_manufacturer = car_processor.cars_by_manufacturer()
    print('Number of cars by manufacturer:')
    print(cars_by_manufacturer)

    # Task 5: Print the number of cars made each year
    cars_by_year = car_processor.cars_by_year()
    print('Number of cars by year:')
    print(cars_by_year)

    # Task 6: Save the dataset to a CSV file
    car_processor.save_to_csv(output_csv)
    print(f'Data saved to {output_csv}')
