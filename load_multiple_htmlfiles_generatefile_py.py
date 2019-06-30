#Section 1
#extract data from HTML Reference USA

import re
import pandas as pd
import codecs
import numpy as np

#load first file for testing if it works
f = codecs.open('ReferenceUSA - Search Results.html','r', 'utf-8')
df = pd.read_html(f)
dfs = df[0]
dfs.head(5)

#Section 2
#loop name setter
o = True
number = 2
while o == True:
    #change the name below for the name of the file, in this case it goes up by one until 29 files have been read
    name = 'ReferenceUSA - Search Results' + str(number) + '.html'
    html = codecs.open(name,'r', 'utf-8')
    #merge above file and new file
    df2 = pd.read_html(html)
    dfs = dfs.append(df2[0])

    number +=1
    #print(number)
    if number == 29:
        dfs = pd.DataFrame(dfs)
        break


#Section 3
#choose columns
dfnew = dfs[dfs.columns[1:7]]
dfnew = dfnew.drop_duplicates()
#choose columns
dfnew = dfnew.dropna(subset=dfnew.columns[[0]], how='any')
dfnew

#Section 4
#export to csv file with header
export_csv = dfnew.to_csv (r'export_dataframe.csv', index = None, header=True)
