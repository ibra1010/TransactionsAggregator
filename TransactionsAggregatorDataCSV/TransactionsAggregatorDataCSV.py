from Transaction import *
from TransactionsAggregatorData import *
import pandas as pd
import os
#import threading
import concurrent.futures
from Common import *

class TransactionsAggregatorDataWrapperCSV(TransactionsAggregatorDataWrapper):
    instance = None
    @staticmethod
    def GetInstance():
        if TransactionsAggregatorDataWrapperCSV.instance == None:
            TransactionsAggregatorDataWrapperCSV()
        return TransactionsAggregatorDataWrapperCSV.instance
    def __init__(self):
        if TransactionsAggregatorDataWrapperCSV.instance != None:
            raise Exception("TransactionsAggregatorDataWrapperCSV class already instanciated")
        else:
            TransactionsAggregatorDataWrapperCSV.instance = self
    def GetTransactionHistoryInput(self, location):
        """parse single data source"""
        data = None
        try:
            data = pd.read_csv(location)
        except BaseException as err:
            logging.exception("Error occured")
        
        res = TransactionHistoryInput(location, data)    
        return res
    def GetTransactionHistoryInputs(self, location):
        """parse all the data sources"""
        res = None
        try:
            listOfFiles = None
            listOfFiles = [file for file in os.listdir(location) if file.lower().endswith(".csv") and file.lower().startswith("bank")]
            #perf optim via multithreading as the operation is I/O bound
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                res = executor.map(self.GetTransactionHistoryInput, listOfFiles)
                print("")
            #data = pd.read_csv(location, skiprows = 1)
        except BaseException as err:
            logging.exception("Error occured")
        return res
    ########
    def SerializeTransactionHistoryOutput(self, location, transactionHistoryOutput):
        """parse all the data sources"""
        try:
            #y.values.tolist())
            convertedToListDictionary = {x: transactionHistoryOutput.dictionaryBankTransactions[x].values.tolist() 
                                         for x in transactionHistoryOutput.dictionaryBankTransactions}
            dataFrame = pd.DataFrame(convertedToListDictionary) 
            dataFrame.to_csv(location)
        except BaseException as err:
            logging.exception("Error occured")
################
#location = "bank1.csv"
#location = os.getcwd()
#wrapper = TransactionsAggregatorDataWrapperCSV.GetInstance()
#data = wrapper.GetTransactionHistoryInputs(location)
#for input in data:
#    print(input)
#print(data)
#wrapper.SerializeTransactionHistoryOutput("output.csv", data)
#print("tt")

