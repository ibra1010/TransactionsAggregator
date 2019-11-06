import unittest
from unittest import TestCase
from TransactionsGenerator import *
from TransactionsAggregator import *
from TransactionsAggregatorDataCSV import *
import os
#from TransactionsGenerator import *
#import TransactionsGenerator
class TransactionsAggregatorTest(TestCase):
    def test_ToTransactionHistoryOutput(self):

        inputs = TransactionsGenerator.GetTransactionHistoryInput3Banks()
        service = TransactionsAggregator()
        output = service.ToTransactionHistoryOutput(inputs)
        expectedOutput = TransactionsGenerator.GetTransactionHistoryOutput3Banks()
        check = output == expectedOutput

        wrapper = TransactionsAggregatorDataWrapperCSV.GetInstance()
        wrapper.SerializeTransactionHistoryOutput("output2.csv", output)
        assert check
    def test_ToTransactionHistoryOutputCSV(self):

        location = os.getcwd()
        wrapper = TransactionsAggregatorDataWrapperCSV.GetInstance()
        inputs = wrapper.GetTransactionHistoryInputs(location)
        
        service = TransactionsAggregator()
        output = service.ToTransactionHistoryOutput(inputs)
        expectedOutput = TransactionsGenerator.GetTransactionHistoryOutput3Banks()
        check = output == expectedOutput
        wrapper.SerializeTransactionHistoryOutput("outputs\output.csv", output)
        assert check
if __name__ == "__main__":
    unittest.main(exit = False)