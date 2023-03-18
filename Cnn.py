
import numpy as np
import pandas as pd
import os


# load and read in the excel file, no need to prepare data as already in correct format
path = os.getcwd()
filename = os.path.join(path,'Subject_1.xlsx')
df = pd.read_excel(filename)

#Split data into however many time steps we want, to pass then through model
def split_sequences(dataframe, steps):
    x,y = list(),list()
    for i in range(len(dataframe)):
        end_seq = i + steps
        if end_seq > len(dataframe):
            break
        else:
            x.append(dataframe.iloc[i:end_seq,1:-1])
            y.append(dataframe.iloc[end_seq-1,-1])
    return np.array(x),np.array(y)  

x,y = split_sequences(df,4)
for i in range(len(x)):
    print(x[i],y[i])
    if i ==6:
        break