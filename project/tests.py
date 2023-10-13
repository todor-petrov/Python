from unittest import TestCase, main
import pandas as pd
import json

from functionality import CarDataProcessor


class TestCarDataProcessor(TestCase, CarDataProcessor):
    def setUp(self):
        self.test_data = [
            {
                "Name": "Toyota Camry",
                "Miles_per_Gallon": 20,
                "Cylinders": 4,
                "Displacement": 307,
                "Horsepower": 200,
                "Weight_in_lbs": 3000,
                "Acceleration": 6,
                "Year": "2020-01-01",
                "Origin": "Japan",
            },
            {
                "Name": "Ford F-150",
                "Miles_per_Gallon": 30,
                "Cylinders": 8,
                "Displacement": 400,
                "Horsepower": 300,
                "Weight_in_lbs": 4500,
                "Acceleration": 10,
                "Year": "2022-06-06",
                "Origin": "USA",
            },
            {
                "Name": "Honda Civic",
                "Miles_per_Gallon": 40,
                "Cylinders": 6,
                "Displacement": 250,
                "Horsepower": 150,
                "Weight_in_lbs": 2700,
                "Acceleration": 8,
                "Year": "2015-08-20",
                "Origin": "Japan",
            },
        ]
        self.test_json_file = 'test_car_data.json'
        self.test_csv_file = 'test_car_data_output.csv'

        with open(self.test_json_file, 'w') as f:
            json.dump(self.test_data, f)

        # Initialize the CarDataProcessor with test data
        self.df = pd.DataFrame(self.test_data)
        self.processor = CarDataProcessor(self.test_json_file)

    # def tearDown(self):
    #     # Clean up, delete the test JSON file and CSV file
    #     import os
    #     os.remove(self.test_json_file)
    #     os.remove(self.test_csv_file)

    def test_unique_cars_count(self):
        self.assertEqual(self.processor.unique_cars_count(), 3)

    def test_average_horsepower(self):
        self.assertAlmostEqual(self.processor.average_horsepower(), 216.66666666666666, places=2)

    def test_top_heaviest_cars(self):
        expected = pd.DataFrame(self.test_data).nlargest(5, "Weight_in_lbs")
        self.assertTrue(self.processor.top_heaviest_cars().equals(expected))

    def test_cars_by_manufacturer(self):
        self.df['Manufacturer'] = self.df['Name'].str.split(' ').str[0]
        expected_result = self.df.groupby(['Manufacturer']).size()
        result = self.processor.cars_by_manufacturer()
        self.assertTrue(expected_result.equals(result))

    # def test_cars_by_year(self):
    #     expected = pd.Series([1, 1, 1], index=[2015, 2020, 2022])
    #     self.assertTrue(self.test_car_processor.cars_by_year().equals(expected))

    def test_save_to_csv(self):
        # Save the data to a test CSV file
        self.processor.save_to_csv(self.test_csv_file)

        # Load the saved CSV and compare it with the original data
        df = pd.read_csv(self.test_csv_file)
        self.assertTrue(df.equals(pd.DataFrame(self.test_data)))


if __name__ == '__main__':
    main()
