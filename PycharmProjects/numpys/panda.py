'''import pandas
import pandas as pd

data=pandas.read_csv('C:\\Users\\adarsh.pandey\\PycharmProjects\\numpys\\Location.csv',squeeze=True)
print(data)
print(data.head())
print(data.describe())
print(len(data))'''
x=[
  {
    "name": "Adarsh",
    "department": "Computer Science",
    "Company": {"Brillio Technologies","HCL","LG"},
    "Location": {"Bangalore","Lucknow"}
  },
  {
    "name": "Shailja",
    "department": "Computer Science",
    "Company": {"Emids","EMC","Dell"},
    "Location": {"Bangalore"}
  }
]
print(x)