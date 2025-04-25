# %%

import pandas as pd
import glob
import os


try:
    folder_data = "data"

    paths_data = glob.glob(os.path.join(folder_data, '*.csv'))

    df_list = []

    for path in paths_data:
        df = pd.read_csv(path)
        company = os.path.basename(path).split('.')[0]
        df.insert(0, 'Company', company)
        df_list.append(df)

    stock_data = pd.concat(df_list, ignore_index=True)

    stock_data.to_csv('stock_data.csv', index=False)
except Exception as e:
    print(e)