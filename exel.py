import pandas as pd
from random import randint
from time import sleep

df = pd.read_excel (r'comments.xlsx')
df = pd.DataFrame(df, columns= ['Com1'])
df = df.to_numpy()
commentArray = []
for x in df:
    commentArray.append(x[0])
    print(x[0])
    # sleep(randint(2,5))


print(commentArray)