import pandas as pd
import os 


data_set = {
    'name':['adarsh','adesh','sani'],
    'age': [23,44,22],
    'batch':[2025,2024,2023]
}

df = pd.DataFrame(data_set)


# # for version 2 data add
# new_row_loc = {'name': 'GF1', 'age': 20, 'batch': 2034}
# df.loc[len(df.index)] = new_row_loc

# # for version 3 data add
# new_row_loc = {'name': 'GF2', 'age': 30, 'batch': 2014}
# df.loc[len(df.index)] = new_row_loc


folder_name = 'data'

os.makedirs(folder_name,exist_ok=True)

file_name = 'sample.csv'
file_path = os.path.join(folder_name,file_name)

df.to_csv(file_path)