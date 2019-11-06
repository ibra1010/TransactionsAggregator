class Transaction:
    def __init__(self, way, amount, toAccount, fromAccount):
        self.way = way
        self.amount = amount
        self.toAccount = toAccount

class TransactionHistoryInput:
    def __init__(self, bank, transactions):
        self.bank = bank
        self.transactions = transactions
class TransactionHistoryOutput:
    def __init__(self, dictionaryBankTransactions):
        self.dictionaryBankTransactions = dictionaryBankTransactions
    def __eq__(self, versusObject):
        if self.__class__!= versusObject.__class__:
            return False
        selfToListDictionary = {x: self.dictionaryBankTransactions[x].values.tolist() 
                                         for x in self.dictionaryBankTransactions}
        versusObject = {x: versusObject.dictionaryBankTransactions[x].values.tolist() 
                                         for x in versusObject.dictionaryBankTransactions}
        return selfToListDictionary == versusObject