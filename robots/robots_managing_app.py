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

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type not in RobotsManagingApp.ROBOTS:
            raise Exception('Invalid robot type!')

        robot = RobotsManagingApp.ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)
        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._find_robot_by_name(robot_name)
        service = self._find_service_by_name(service_name)

        if not RobotsManagingApp.SERVICES_ROBOTS[service.__class__.__name__] == robot.__class__.__name__:
            return 'Unsuitable service.'

        if service.capacity == len(service.robots):
            raise Exception('Not enough capacity for this robot!')

        self.robots.remove(robot)
        service.robots.append(robot)
        return f'Successfully added {robot_name} to {service_name}.'

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = self._find_service_by_name(service_name)
        robot = [r for r in service.robots if r.name == robot_name]

        if not robot:
            raise Exception('No such robot in this service!')

        service.robots.remove(robot[0])
        self.robots.append(robot[0])
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name: str):
        service = self._find_service_by_name(service_name)

        for robot in service.robots:
            robot.eating()

        return f'Robots fed: {len(service.robots)}.'

