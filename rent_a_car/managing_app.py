from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VEHICLES_TYPES = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.find_user_by_driving_license(driving_license_number)
        if user in self.users:
            return f'{driving_license_number} has already been registered to our platform.'
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f'{first_name} {last_name} was successfully registered under DLN-{driving_license_number}'

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VEHICLES_TYPES:
            return f'Vehicle type {vehicle_type} is inaccessible.'
        if self.find_vehicle_by_license_plate_number(license_plate_number) is not None:
            return f'{license_plate_number} belongs to another vehicle.'
        vehicle = ManagingApp.VEHICLES_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f'{brand} {model} was successfully uploaded with LPN-{license_plate_number}.'

    def allow_route(self, start_point: str, end_point: str, length: float):
        ...

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        ...

    def repair_vehicles(self, count: int):
        ...

    def users_report(self):
        ...

    def find_user_by_driving_license(self, driving_license_number):
        user = [u for u in self.users if u.driving_license_number == driving_license_number]
        return user[0] if user else None

    def find_vehicle_by_license_plate_number(self, license_plate_number):
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number]
        return vehicle[0] if vehicle else None
