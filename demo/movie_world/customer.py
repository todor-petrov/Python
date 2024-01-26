class Customer:

    def __init__(self, name: str, age: int, customer_id: int):
        self.name = name
        self.age = age
        self.id = customer_id
        self.rented_dvds = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} has "
                f"{len(self.rented_dvds)} rented "
                f"DVD's ({', '.join(dvd.name for dvd in self.rented_dvds)})")
