from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):

    INTEREST_RATE = 3.5
    AMOUNT = 50000.0
    RATE_INCREASING = 0.5

    def __init__(self):
        super().__init__(interest_rate=MortgageLoan.INTEREST_RATE, amount=MortgageLoan.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += MortgageLoan.RATE_INCREASING
