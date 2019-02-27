# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind = 'bar',)
plt.xlabel('Status of loan')
plt.ylabel('Number of loan approved')
plt.show()


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status'])['Loan_Status'].count().unstack()
print(property_and_loan)
property_and_loan.plot(kind = 'bar')
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)
plt.show()


# --------------
#Code starts here
education_and_loan = data.groupby(['Education', 'Loan_Status'])['Loan_Status'].count().unstack()
education_and_loan.plot(kind = 'bar', stacked = True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)
plt.show()


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind = 'density', label = 'Graduate')
not_graduate['LoanAmount'].plot(kind = 'density', label = 'Not Graduate')

print(data['LoanAmount'])







#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax1,ax2, ax3) = plt.subplots(nrows = 3, ncols = 1, figsize = (20,10))
ax1.scatter(data['ApplicantIncome'], data['LoanAmount'])
ax1.set_title('Applicant Income')
ax2.scatter(data['CoapplicantIncome'], data['LoanAmount'])
ax2.set(title = 'Coapplicatn Income')
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax3.scatter(data['TotalIncome'], data['LoanAmount'])
ax3.set_title('Total Income')


