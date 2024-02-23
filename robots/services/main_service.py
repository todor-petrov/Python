from robots.services.base_service import BaseService


class MainService(BaseService):

    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=MainService.CAPACITY)

    def details(self):
        service_details = [f'{self.name} Main Service:', 'Robots: ']
        if self.robots:
            service_details[1] += ' '.join([r.name for r in self.robots])
        else:
            service_details[1] += 'none'

        return '\n'.join(service_details)
