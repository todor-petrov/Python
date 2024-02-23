from project.services.base_service import BaseService


class SecondaryService(BaseService):

    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=SecondaryService.CAPACITY)

    def details(self):
        service_details = [f'{self.name} Secondary Service:', 'Robots: ']
        if self.robots:
            service_details[0] += ' '.join(r.name for r in self.robots)
        else:
            service_details[0] += 'none'
