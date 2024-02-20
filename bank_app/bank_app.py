from clients.adult import Adult
from clients.student import Student
from loans.mortgage_loan import MortgageLoan
from loans.student_loan import StudentLoan


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
        return f'{loan_type} was successfully added.'

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in BankApp.CLIENTS:
            raise Exception('Invalid client type!')
        if len(self.clients) == self.capacity:
            return 'Not enough bank capacity.'
        new_client = BankApp.CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f'{client_type} was successfully added.'

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_client_by_id(client_id)
        loan = self.find_loan_by_loan_type(loan_type)
        if not client.LOAN_TYPE == loan_type:
            raise Exception('Inappropriate loan type!')
        self.loans.remove(loan)
        client.loans.append(loan)
        return f'Successfully granted {loan_type} to {client.name} with ID {client_id}.'

    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)
        if client is None:
            raise Exception('No such client!')
        if client.loans:
            raise Exception('The client has loans! Removal is impossible!')
        client_name = client.name
        self.clients.remove(client)
        return f'Successfully removed {client_name} with ID {client_id}.'
