# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 

data = pd.read_csv(path)
data['Gender'].replace('-', 'Agender' , inplace = True)
gender_count = data['Gender'].value_counts()
print(gender_count)
plt.bar(gender_count.index, gender_count.values)
plt.title('Gender count')


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.pie(alignment, autopct = '%1.1f%%', labels = alignment.index, startangle = 90, shadow = True, explode = (0,0.04,0,))


# --------------
#Code starts here

sc_df = data[['Strength', 'Combat']]

sc_covariance = sc_df.cov()['Strength'][1]
print(sc_covariance)
sc_strength = sc_df['Strength'].std()

sc_combat = sc_df['Combat'].std()

sc_pearson = sc_covariance/(sc_strength * sc_combat)
print('Correlation betwee Strength and Combat:',sc_pearson)

ic_df = data[['Intelligence','Combat']]

ic_covariance = ic_df.cov()['Intelligence'][1]

ic_intelligence = ic_df['Intelligence'].std()

ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance/(ic_intelligence * ic_combat)
print('Correlation between Intelligence and combat:', ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
super_best = data[data['Total'] >total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here

fig, (ax_1,ax_2,ax_3) = plt.subplots(1,3, figsize = (20,10))

ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')

ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed')

ax_3.boxplot(data['Power'])
ax_3.set_title('Power')


