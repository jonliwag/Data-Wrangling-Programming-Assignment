import pandas as pd

data1 = {'Student': ['Ice Bear','Panda','Grizzly'], 'Math': [80, 95, 79]}
data2 = {'Student': ['Ice Bear','Panda','Grizzly'], 'Electronics': [85, 81, 83]}
data3 = {'Student': ['Ice Bear','Panda','Grizzly'], 'GEAS': [90, 79, 93]}
data4 = {'Student': ['Ice Bear','Panda','Grizzly'], 'ESAT': [93, 89, 88]}

table1 = pd.DataFrame (data1, columns = ['Student','Math'])
table2 = pd.DataFrame (data2, columns = ['Student','Electronics'])
table3 = pd.DataFrame (data3, columns = ['Student','GEAS'])
table4 = pd.DataFrame (data4, columns = ['Student','ESAT'])

mergeA = pd.merge(table1, table2, on = "Student")
mergeB = pd.merge(mergeA, table3, on = "Student")
mergeC = pd.merge(mergeB, table4, on = "Student")

conv = pd.melt(mergeC, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
longFormat = conv.rename(columns = {'variable':'Subject','value':'Grades'})