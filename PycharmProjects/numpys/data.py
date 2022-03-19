'''import pandas as pd
import numpy as np

data=pd.read_csv('C:\\Users\\adarsh.pandey\\PycharmProjects\\numpys\\Lending-company.csv',index_col='LoanID')
lending_company_data=data.copy()
print(lending_company_data)
print(type(lending_company_data))
print(lending_company_data.index)
print(lending_company_data.columns)
print(lending_company_data.dtypes)
print(lending_company_data.to_numpy())
print(type(lending_company_data))
print(lending_company_data.shape)
print(lending_company_data[['Product','Location']].head())
