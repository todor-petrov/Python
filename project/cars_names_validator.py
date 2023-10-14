import os
import json


def cars_names_validator(line):
    if os.path.isfile('D:/Python-Projects/Python/project/renamed_car_names_report.txt'):
        with open('renamed_car_names_report.txt', 'w'):
            pass

    incorrect_names = {
        'vw': 'volkswagen',
        'vokswagen': 'volkswagen',
        'toyouta': 'toyota',
        'mercedes': 'mercedes-benz',
        'maxda': 'mazda',
        'chevy': 'chevrolet',
        'chevroelt': 'chevrolet',
        'capri': 'mercury capri'
    }

    count = 0
    for car in line:
        car_name_details = car['Name'].split(' ')

        if car_name_details[0] in incorrect_names:
            count += 1
            old_name = car['Name']
            car_name_details[0] = incorrect_names[car_name_details[0]]
            car['Name'] = ' '.join(car_name_details)
            new_name = car['Name']

            with open('renamed_car_names_report.txt', 'a') as note:
                note.write(f'{count}. In row {line.index(car) + 1} {old_name} has been renamed to {new_name}\n')

    return line


# with open('cars.json', 'r') as cars:
#     d = json.load(cars)
# for el in d:
#     print(el['Name'])
