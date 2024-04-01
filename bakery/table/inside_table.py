from bakery.table.table import Table


class InsideTable(Table):

    MIN_TABLE_NUMBER = 1
    MAX_TABLE_NUMBER = 50

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)
        
    @property
    def table_number(self):
        return self.__table_number
    
    @table_number.setter
    def table_number(self, value):
        if not InsideTable.MIN_TABLE_NUMBER <= value <= InsideTable.MAX_TABLE_NUMBER:
            raise ValueError(f"Inside table's number must be between "
                             f"{InsideTable.MIN_TABLE_NUMBER} and {InsideTable.MAX_TABLE_NUMBER} inclusive!")
        self.__table_number = value
