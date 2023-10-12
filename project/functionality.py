import pandas as pd


def all_cars(dataframe):
    return len(dataframe)


def unique_cars(data_frame):
    return f"Number of unique cars: {len(data_frame['Name'].unique())}"


def average_horse_power(data_frame):
    return f"Average horsepower of all cars: {data_frame['Horsepower'].mean()}"


def most_heaviest_cars(data_frame):
    number_of_most_heaviest_cars = 5
    return ("Top 5 heaviest cars:\n"
            f"{data_frame.nlargest(number_of_most_heaviest_cars, 'Weight_in_lbs', keep='first')}")


def number_of_cars_made_by_each_manufacturer(data_frame):
    data_frame['Manufacturer'] = data_frame['Name'].str.split(' ').str[0]
    return data_frame.groupby(['Manufacturer']).size()


def cars_made_by_each_manufacturer(data_frame):
    data_frame['Manufacturer'] = data_frame['Name'].str.split(' ').str[0]
    return data_frame['Manufacturer'].groupby(data_frame['Manufacturer']).count()


def number_of_cars_made_each_year(data_frame):
    data_frame['Year'] = pd.to_datetime(data_frame['Year'])
    data_frame['YearOfManufacture'] = data_frame['Year'].dt.year
    return data_frame.groupby(data_frame['YearOfManufacture']).size()


def save_dataset_to_a_csv_file(data_frame):
    dataframe = pd.DataFrame(data_frame)
    dataframe.to_csv('Cars.csv', index=False)