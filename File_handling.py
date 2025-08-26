#trying to revise how to handle files in python

# Open a file
with open("C:\\Users\\NITRO V\\Downloads\\employees.csv", 'r') as f:
    #read the content of the file
    # content = f.read()
    # print(content)
    for i in range(5):
        rows = f.readline()
        print(rows)

import pandas as pd
df = pd.read_csv("C:\\Users\\NITRO V\\Downloads\\employees.csv")
print(df)
print('')

print(df.head(5))

print("")
df_filter = df[df['Department'] == 'IT']
print(df_filter)


group = df.groupby('Department').count()
print("")
print(group)

average = df['Salary'].mean()
print("")
print(f"AVERAGE SALARY IS {average}")


elder = df['Age'] > 30
print("")
print(df[elder])


highest =df['Salary'].max()
print("")
print(df[df['Salary'] == highest])


aver = df.groupby('Department')
av = aver['Salary'].mean()
print("")
print(av)


#save to new file whose salary is > 50000
new_df = df[df['Salary'] > 50000]
new_df.to_csv('high_salary_employees.csv', index=False)
print("")
print("File saved as high_salary_employees.csv")


#sorting
sorted_df = df.sort_values(by='Age')
print("")
print(sorted_df)


df['Tax'] = df['Salary'] * 10/100
print(df)