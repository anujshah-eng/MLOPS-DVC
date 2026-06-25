import pandas as pd 
import os

#create a sample data frame 

data ={ 'NAME':['Alice' ,'Bob', 'Cap'],
        'Age':[20, 25, 10],
        'City': ['HLD', 'Doon', 'Delhi'],
}

df = pd.DataFrame(data)

# Adding a new row to df for V2
new_row_loc={'NAME': 'GF1', 'Age': 30, 'City': 'MUM'}
df.loc[len(df.index)] = new_row_loc

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path =os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")