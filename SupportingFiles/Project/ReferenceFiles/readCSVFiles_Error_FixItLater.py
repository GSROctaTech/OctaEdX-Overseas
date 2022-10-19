# https://samanemami.medium.com/how-to-make-data-frames-from-different-csv-files-in-python-4fe40a7c3cc1

import os
import fnmatch

for file in os.listdir('..'):
    print(file)

    '''This will print all the stored files once for you.But what if we are looking for specific files 
    among all the outputs? I have the answer here, the fnmatch library of Python.'''

    for file in os.listdir('..'):
        if fnmatch.fnmatch(file, '*_yourFileName.csv'):
            print(file)
            df = pd.read_csv(file)

    ''' In the above code, the `yourFileName` is a string including the lookup value.And it will print the file name 
    you’re looking for it.It is time to save the file as a data frame.For this purpose, we use the pandas 
    library and its to_csv() method.'''

index_ = {'name': [], 'shape': []}
for file in os.listdir('..'):
    if fnmatch.fnmatch(file, '*_yourFileName.csv'):
        index_['shape'].append((pd.read_csv(file).shape[1]))
        index_['name'].append(file)
max_cl = max(index_['shape'])
file = index_['name'][index_['shape'].index(max_cl)]
dic = {'key': pd.read_csv(file).columns}
dic = list(pd.read_csv(file).columns)
row_names = [index_['name'][i][2:-9] for i in range(len(index_['name']))]
df = pd.DataFrame(np.zeros((len(index_['name']), max_cl)), columns=dic, index=row_names)

for _, file in enumerate(index_['name']):
    ave = (pd.read_csv(file)).mean()
    for i, j in enumerate(ave.index):
        df.iloc[_, dic.index(j)] = ave.iloc[i]
