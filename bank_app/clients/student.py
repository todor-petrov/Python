from project.clients.base_client import BaseClient


class Student(BaseClient):

    INTEREST = 2.0
    INTEREST_RATE_INCREASE = 1.0
    LOAN_TYPE = 'StudentLoan'

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=Student.INTEREST)

    def increase_clients_interest(self):
        self.interest += Student.INTEREST_RATE_INCREASE
