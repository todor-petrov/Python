from movie_world.customer import Customer
from movie_world.dvd import DVD


class MovieWorld:

    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def find_customer(self, customer_id):
        return [c for c in self.customers if c.id == customer_id][0]

    def find_dvd(self, dvd_id):
        return [d for d in self.dvds if d.id == dvd_id][0]

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_customer(customer_id)
        dvd = self.find_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_customer(customer_id)
        dvd = self.find_dvd(dvd_id)
        if dvd not in customer.rented_dvds:
            return f'{customer.name} does not have that DVD'
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f'{customer.name} has successfully returned {dvd.name}'

    def __repr__(self):
        movie_world_data = [c.__repr__() for c in self.customers]
        movie_world_data.extend([dvd.__repr__() for dvd in self.dvds])
        return f'\n'.join(movie_world_data)
