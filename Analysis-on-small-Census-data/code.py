# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
# delimiter is set to ',' because we are reading csv(comma separated file)
data = np.genfromtxt(path, delimiter = ',', skip_header = 1)
print(data.shape)
census = np.concatenate((data, new_record), axis = 0)
print(census.shape)


# --------------
#Code starts here
import numpy as np
age = census[:,0]
max_age = np.max(age)
print('max_age: ', max_age)
min_age = np.min(age)
print('min_age: ', min_age)
age_mean = np.mean(age)
print('age_mean: ', age_mean)
age_std = np.std(age)
print('age_std: ', age_std)


# --------------
# #Code starts here
# race= census[:, 2]

# race_0 = census[census[:, 2] == 0]

# race_1 = race[race == 1.0]
# race_2 = race[race == 2.0]
# race_3 = race[race == 3.0]
# race_4 = race[race == 4.0]
# # print(race_0)
# for i in race_0:
#     print(i)
# len_0 = len(race_0)
# len_1 = len(race_1)
# len_2 = len(race_2)
# len_3 = len(race_3)
# len_4 = len(race_4)

# # print('Number of citizen of race 0: ', len_0)
# # print('Number of citizen of race 1: ', len_1)
# # print('Number of citizen of race 2: ', len_2)
# # print('Number of citizen of race 3: ', len_3)
# # print('Number of citizen of race 4: ', len_4)

# tuple_of_race_no = (len_0,len_1, len_2,len_3, len_4)
# print(tuple_of_race_no)

# if (len_0 < len_1 and len_0 < len_2 and len_0 < len_3 and len_0 < len_4):
#     minority_race = 0
# elif ( len_1 < len_2 and len_1 < len_3 and len_1 < len_4):
#     minority_race = 1
# elif (len_2 < len_3 and len_2 < len_4):
#     minority_race = 2
# elif (len_3 < len_4):
#     minority_race = 3
# else:
#     minority_race = 4

# print('minority race:', minority_race)



race_0 = census[census[:, 2] == 0]
race_1 = census[census[:, 2] == 1]
race_2 = census[census[:, 2] == 2]
race_3 = census[census[:, 2] == 3]
race_4 = census[census[:, 2] == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print('Number of citizen of race 0: ', len_0)
print('Number of citizen of race 1: ', len_1)
print('Number of citizen of race 2: ', len_2)
print('Number of citizen of race 3: ', len_3)
print('Number of citizen of race 4: ', len_4)

tuple_of_race_no = (len_0,len_1, len_2,len_3, len_4)
print(tuple_of_race_no)

if (len_0 < len_1 and len_0 < len_2 and len_0 < len_3 and len_0 < len_4):
    minority_race = 0
elif ( len_1 < len_2 and len_1 < len_3 and len_1 < len_4):
    minority_race = 1
elif (len_2 < len_3 and len_2 < len_4):
    minority_race = 2
elif (len_3 < len_4):
    minority_race = 3
else:
    minority_race = 4

print('minority race:', minority_race)


# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]
working_hours_sum = sum(senior_citizens[:, 6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print('average working hours of senior citizen :', avg_working_hours)


# --------------
#Code starts here
import numpy as np
high = census[census[:, 1] > 10]
low = census[census[:,1] <= 10]
print(low, high)

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high, avg_pay_low)


