from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    LOANS = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}
    CLIENTS = {'Student': Student, 'Adult': Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.LOANS:
            raise Exception('Invalid loan type!')
        self.loans.append(BankApp.LOANS[loan_type]())
        return f'"{loan_type} was successfully added.'

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        ...

    def grant_loan(self, loan_type: str, client_id: str):
        ...

    def remove_client(self, client_id: str):
        ...

    def increase_loan_interest(self, loan_type: str):
        ...

    def increase_clients_interest(self, min_rate: float):
        ...

    def get_statistics(self):
        ...
