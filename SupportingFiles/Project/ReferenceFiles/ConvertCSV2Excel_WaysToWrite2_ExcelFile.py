# Convert Excel to CSV using Python
import pandas as pd
data_xls = pd.read_excel('excelfile.xlsx', 'Sheet2', dtype=str, index_col=None)
data_xls.to_csv('csvfile.csv', encoding='utf-8', index=False)
# -------------------------------------------------------------------------------------------------------------
# how to convert csv to excel in python
import pandas as pd
data = pd.read_csv("k.csv")
data.to_excel("new_file.xlsx", index=None, header=True)
# -------------------------------------------------------------------------------------------------------------

import pandas as pd
# Save Dataframe df to output.xlsx in current directory with sheet_name_1
df.to_excel("output.xlsx", sheet_name='Sheet_name_1')

# -------------------------------------------------------------------------------------------------------------
# python csv to excel
with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
       writer.writerow([key, value])