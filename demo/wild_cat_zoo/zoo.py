from animal import Animal
from worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif len(self.animals) < self.__animal_capacity and self.__budget < price:
            return 'Not enough budget'
        else:
            return 'Not enough space for animal'

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        amount = sum([w.salary for w in self.workers])
        if amount <= self.__budget:
            self.__budget -= amount
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        amount = sum([a.money_for_care for a in self.animals])
        if amount <= self.__budget:
            self.__budget -= amount
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_summary = [f'You have {len(self.animals)} animals']
        lions = [a.__repr__() for a in self.animals if a.__class__.__name__ == 'Lion']
        if lions:
            animals_summary.append(f'----- {len(lions)} Lions:')
            animals_summary.extend(lions)
        tigers = [a.__repr__() for a in self.animals if a.__class__.__name__ == 'Tiger']
        if tigers:
            animals_summary.append(f'----- {len(tigers)} Tigers:')
            animals_summary.extend(tigers)
        cheetahs = [a.__repr__() for a in self.animals if a.__class__.__name__ == 'Cheetah']
        if cheetahs:
            animals_summary.append(f'----- {len(cheetahs)} Cheetahs:')
            animals_summary.extend(cheetahs)
        return '\n'.join(animals_summary)

    def workers_status(self):
        workers_summary = [f'You have {len(self.workers)} workers']
        keepers = [w.__repr__() for w in self.workers if w.__class__.__name__ == 'Keeper']
        if keepers:
            workers_summary.append(f'----- {len(keepers)} Keepers:')
            workers_summary.extend(keepers)
        caretakers = [w.__repr__() for w in self.workers if w.__class__.__name__ == 'Caretaker']
        if caretakers:
            workers_summary.append(f'----- {len(caretakers)} Caretakers:')
            workers_summary.extend(caretakers)
        vets = [w.__repr__() for w in self.workers if w.__class__.__name__ == 'Vet']
        if vets:
            workers_summary.append(f'----- {len(vets)} Vets:')
            workers_summary.extend(vets)
        return '\n'.join(workers_summary)
