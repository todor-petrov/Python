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

    def increase_loan_interest(self, loan_type: str):
        loans = [loan for loan in self.loans if loan.__class__.__name__ == loan_type]
        for loan in loans:
            loan.increase_interest_rate()
        return f'Successfully changed {len(loans)} loans.'

    def increase_clients_interest(self, min_rate: float):
        clients = [c for c in self.clients if c.interest < min_rate]
        for client in clients:
            client.increase_clients_interest()
        return f'Number of clients affected: {len(clients)}.'

    def get_statistics(self):

        total_clients_income = sum([c.income for c in self.clients])
        loans_count_granted_to_clients = sum([len(c.loans) for c in self.clients])
        granted_sum = 0
        for client in self.clients:
            for loan in client.loans:
                granted_sum += loan.amount

        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([a.amount for a in self.loans])
        avg_client_interest_rate = 0
        if self.clients:
            avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)

        bank_statistics = [f'Active Clients: {len(self.clients)}',
                           f'Total Income: {total_clients_income:.2f}',
                           f'Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}',
                           f'Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}',
                           f'Average Client Interest Rate: {avg_client_interest_rate:.2f}']
        return '\n'.join(bank_statistics)

    def find_client_by_id(self, client_id):
        client = [c for c in self.clients if c.client_id == client_id]
        return client[0] if client else None

    def find_loan_by_loan_type(self, loan_type):
        loan = [loan for loan in self.loans if loan.__class__.__name__ == loan_type]
        return loan[0] if loan else None
