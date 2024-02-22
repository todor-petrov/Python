from rent_a_car.route import Route
from rent_a_car.user import User
from rent_a_car.vehicles.cargo_van import CargoVan
from rent_a_car.vehicles.passenger_car import PassengerCar


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
        route_id = len(self.routes) + 1
        route = self.check_route(start_point, end_point, length)
        if route == 'Route already exists!':
            return f'{start_point}/{end_point} - {length} km had already been added to our platform.'
        elif route == 'Shorter route exists!':
            return f'{start_point}/{end_point} shorter route had already been added to our platform.'
        else:
            new_route = Route(start_point, end_point, length, route_id)
            self.routes.append(new_route)
            return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = self.find_user_by_driving_license(driving_license_number)
        vehicle = self.find_vehicle_by_license_plate_number(license_plate_number)
        route = [r for r in self.routes if r.route_id == route_id][0]
        if user.is_blocked:
            return f'User {driving_license_number} is blocked in the platform! This trip is not allowed.'
        if vehicle.is_damaged:
            return f'Vehicle {license_plate_number} is damaged! This trip is not allowed.'
        if route.is_locked:
            return f'Route {route_id} is locked! This trip is not allowed.'
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

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

    def check_route(self, start_point, end_point, length):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point:
                if r.length == length:
                    return 'Route already exists!'
                elif r.length < length:
                    return 'Shorter route exists!'
                elif r.length > length:
                    r.is_locked = True
                    return 'Route have to be locked!'
        return
