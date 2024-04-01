from bakery.table.table import Table


class OutsideTable(Table):
    MIN_TABLE_NUMBER = 51
    MAX_TABLE_NUMBER = 100

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not OutsideTable.MIN_TABLE_NUMBER <= value <= OutsideTable.MAX_TABLE_NUMBER:
            raise ValueError(f"Outside table's number must be between "
                             f"{OutsideTable.MIN_TABLE_NUMBER} and {OutsideTable.MAX_TABLE_NUMBER} inclusive!")
        self.__table_number = value
