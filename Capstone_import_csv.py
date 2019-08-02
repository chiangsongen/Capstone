# Importing libraries
import time
import os
import numpy as np
import pandas as pd
import dask.dataframe as dd

start_time = time.time()

# Importing csv and put into pandas df
os.chdir(r'E:\GA_DSI\Projects\Capstone\lending-club-loan-data')

loan_csv = 'loan.csv'

with open(loan_csv, mode="r", encoding="utf8") as loan_raw:
    loan_raw = pd.read_csv(loan_raw)

print(loan_raw["acc_now_delinq"].value_counts(dropna=False, normalize=True))
print(loan_raw.shape)


#   Uncomment when needed
#   Creating samples out of full dataset
# df_loan_sp_1 = loan_raw.sample(frac=0.1, random_state=1)
# df_loan_sp_1.to_csv('loan_sample_1.csv', index=None, header=True)

# df_loan_sp_2 = loan_raw.sample(frac=0.1, random_state=2)
# df_loan_sp_2.to_csv('loan_sample_2.csv', index=None, header=True)

# df_loan_sp_3 = loan_raw.sample(frac=0.1, random_state=3)
# df_loan_sp_3.to_csv('loan_sample_3.csv', index=None, header=True)

# df_loan_sp_4 = loan_raw.sample(frac=0.25, random_state=659)
# df_loan_sp_4.to_csv('loan_sample_4.csv', index=None, header=True)


print("--- %s seconds ---" % (time.time() - start_time))