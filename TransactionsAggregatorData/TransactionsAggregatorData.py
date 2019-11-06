from abc import ABC, abstractmethod
class TransactionsAggregatorDataWrapper(ABC):
    
    @abstractmethod
    def GetTransactionHistoryInput(self, location):
        """parse single data source"""
        pass
    @abstractmethod
    def GetTransactionHistoryInputs(self, location):
        """parse all the data sources"""
        pass
    @abstractmethod
    def SerializeTransactionHistoryOutput(self, location):
        """parse all the data sources"""
        pass
