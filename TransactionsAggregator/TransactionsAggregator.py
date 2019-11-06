from Common import *
from TransactionsAggregatorDataCSV import *
from TransactionsAggregatorAbstract import * 
class TransactionsAggregator(TransactionsAggregatorAbstract):
    
    def ToTransactionHistoryOutput(self, inputListOfTransactionHistoryInput) ->TransactionHistoryOutput:
        """Transformation service"""
        dictionary = dict()
        for item in inputListOfTransactionHistoryInput:
            dictionary[item.bank] = item.transactions
        
        res = TransactionHistoryOutput(dictionary)
        return res
