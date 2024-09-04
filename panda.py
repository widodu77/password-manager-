import pandas as pd
import numpy as np 


data = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

dict_data = {
    "list": ['one', 'two', 'three'],
    "ha": ['fout', 'five', 'sis'],
    "haha": [1, 2, 3],
    'euh': [5, 6,  8],
    "listee": ['one', 'two', 'three'],
    "haaaa": ['ftour', 'shour','ramadan'],
    "hahhaa": [44, 55,  77],
    'euhhh': [0, 66,  88],
    "lissst": ['haaaaaaa','hooooo','heeeeee'],
    "ijha": ['asdasd','asdaha','fem']
}

list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'nineth', 'tenth']

series1 = pd.Series(data, index=index)
series2 = pd.Series(dict_data)
series3 = pd.Series(list_data, index=index)


series2.index = index

data1 = [1,2,3,4,5]
df= pd.DataFrame(data1,columns=['ahhhhh'])


hashbrown = pd.DataFrame(dict_data, index = ['first','second','third'])

d = { 'one' : pd.Series([1,2,3], index=['A','b','c']),
     'two' : pd.Series([1,2,3], index=['A','b','c'])
     }