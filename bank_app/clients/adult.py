from clients.base_client import BaseClient


class Adult(BaseClient):

    INTEREST = 4.0
    INTEREST_RATE_INCREASE = 2.0
    LOAN_TYPE = 'MortgageLoan'

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=Adult.INTEREST)

    def increase_clients_interest(self):
        self.interest += Adult.INTEREST_RATE_INCREASE
