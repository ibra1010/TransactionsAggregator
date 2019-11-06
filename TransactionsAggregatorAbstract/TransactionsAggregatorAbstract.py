from abc import ABC, abstractmethod
from Common import *
from Transaction import *
class TransactionsAggregatorAbstract(ABC):
    
    @abstractmethod
    def ToTransactionHistoryOutput(self, input:TransactionHistoryInput) ->TransactionHistoryOutput:
        """parse single data source"""
        pass
