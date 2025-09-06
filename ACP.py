import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 80000, 52000]
}

df = pd.DataFrame(data)

df['Bonus'] = df['Salary'] * 0.1

df_filtered = df[df['Department'] == 'IT']

df_sorted = df.sort_values(by='Salary', ascending=False)

df_grouped = df.groupby('Department').agg({'Salary': 'mean', 'Bonus': 'sum'})

df_updated = df.copy()
df_updated.loc[df_updated['Age'] > 30, 'Salary'] *= 1.05

df_dropped = df.drop(columns='Bonus')

new_row = pd.DataFrame([{'Name': 'Frank', 'Age': 32, 'Department': 'Marketing', 'Salary': 58000, 'Bonus': 5800}])
df_appended = pd.concat([df, new_row], ignore_index=True)

df_reset = df_sorted.reset_index(drop=True)

print(df)
print(df_filtered)
print(df_sorted)
print(df_grouped)
print(df_updated)
print(df_dropped)
print(df_appended)
print(df_reset)
