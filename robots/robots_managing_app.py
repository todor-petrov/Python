from robots.robots.female_robot import FemaleRobot
from robots.robots.male_robot import MaleRobot
from robots.services.main_service import MainService
from robots.services.secondary_service import SecondaryService


class RobotsManagingApp:

    SERVICES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    ROBOTS = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}
    SERVICES_ROBOTS = {'MainService': 'MaleRobot', 'SecondaryService': 'FemaleRobot'}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in RobotsManagingApp.SERVICES:
            raise Exception('Invalid service type!')

        service = RobotsManagingApp.SERVICES[service_type](name)
        self.services.append(service)
        return f'{service_type} is successfully added.'
