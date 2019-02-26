# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)




# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID', axis = 1)
print(banks.isnull().sum())

bank_mode = banks.mode()
col = list(bank_mode.columns)
mode  = list(bank_mode.iloc[0])
dic =dict(zip(col, mode))
banks = banks.fillna(dic)

print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here

avg_loan_amount = banks.pivot_table(index = ['Gender','Married','Self_Employed'], values = 'LoanAmount')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here

loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_se)

loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_nse)

percentage_se = (loan_approved_se/614)*100
print(percentage_se)

percentage_nse = (loan_approved_nse/614) * 100
print(percentage_nse)

# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
big_loan_term = len(loan_term[loan_term >= 25])



# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()
print(mean_values)


# code ends here


