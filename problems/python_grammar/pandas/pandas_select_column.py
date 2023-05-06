import pandas as pd
import numpy as np

# 데이터프레임 1
df1 = pd.DataFrame(data=np.array([['lee', 'L.A.', 20], ['park', 'Seattle', 20], ['kim', 'Washington DC', 20]]), columns=['name', 'city', 'age'])

# 데이터프레임 2
df2= pd.DataFrame(data=np.array([['Jung', 'Korea', 21]]), columns=['name', 'city', 'age'])

# 데이터프레임 1과 2를 더해서 새로운 데이터프레임을 리턴
df = pd.concat([df1, df2], ignore_index=True)

print(df)

# attribute가 name인 column가져오기
print(df['name'])

# index가 2인 row 가져오기
print(df.iloc[2])


np.random.seed(0)
df = pd.DataFrame(np.random.randint(1,20,size=(20, 4)), columns=list('ABCD'))
print(df.loc[df['B'] == 4])