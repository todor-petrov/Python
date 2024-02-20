from project.user import User


class ManagingApp:

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
        ...

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
