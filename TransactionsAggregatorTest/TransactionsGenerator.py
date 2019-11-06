from Transaction import *
import pandas as pd
#from pandas import * as pd
class TransactionsGenerator:
    @staticmethod
    def GetTransactionHistoryInput3Banks():
        res = []
        #pass
        l11 = ['Oct 1 2019', 'remove', 99, 182, 198]
        l12 = ['Oct 2 2019', 'add', 2000, 198, 188]
        data1 = [l11, l12]
        dataFrame1 = pd.DataFrame(data1)
        res.append(TransactionHistoryInput("bank1.csv", dataFrame1))
        ####################
        l21 = ['03-10-2019', 'remove', 99, 182, 198]
        l22 = ['04-10-2019', 'add', 2000, 198, 188]
        data2 = [l21, l22]
        dataFrame2 = pd.DataFrame(data2)
        res.append(TransactionHistoryInput("bank2.csv", dataFrame2))
        #####################
        l31 = ['Oct 4 2019', 'remove', 99, 182, 198]
        l32 = ['Oct 5 2019', 'add', 2000, 198, 188]
        data3 = [l31, l32]
        dataFrame3 = pd.DataFrame(data3)
        res.append(TransactionHistoryInput("bank3.csv", dataFrame3))
        return res
    
    @staticmethod
    def GetTransactionHistoryOutput3Banks():
       dictionary = dict()
       inputs = TransactionsGenerator.GetTransactionHistoryInput3Banks()
       dictionary[inputs[0].bank] = inputs[0].transactions
       dictionary[inputs[1].bank] = inputs[1].transactions
       dictionary[inputs[2].bank] = inputs[2].transactions
       res = TransactionHistoryOutput(dictionary)
       return res