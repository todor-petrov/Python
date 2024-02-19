from loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):

    INTEREST_RATE = 1.5
    AMOUNT = 2000.0
    RATE_INCREASING = 0.2

    def __init__(self):
        super().__init__(interest_rate=StudentLoan.INTEREST_RATE, amount=StudentLoan.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += StudentLoan.RATE_INCREASING
