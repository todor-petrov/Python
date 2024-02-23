from project.services.base_service import BaseService


class MainService(BaseService):

    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=MainService.CAPACITY)

    def details(self):
        robots_details = [f'{self.name} Main Service:', 'Robots: ']
        if self.robots:
            robots_details[1] += ', '.join([r.name for r in self.robots])
        else:
            robots_details[1] += 'none'
