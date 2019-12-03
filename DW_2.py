import pandas as pd

messy = {'Box': ['Box1','Box1','Box1','Box2','Box2','Box2'], 
         'Dimension': ['Length','Width','Height','Length','Width','Height'], 
         'Value': [6, 4, 2, 5, 3, 4]}
mTable = pd.DataFrame(messy, columns = ['Box','Dimension','Value'])

tidy = mTable.pivot_table(index = ['Box'], columns = 'Dimension', values = 'Value').reset_index()

volume0 = (tidy.iloc[0,1]) * (tidy.iloc[0,2]) * (tidy.iloc[0,3])
volume1 = (tidy.iloc[1,1]) * (tidy.iloc[1,2]) * (tidy.iloc[1,3])

newColumn = tidy['Volume'] = [volume0, volume1]
