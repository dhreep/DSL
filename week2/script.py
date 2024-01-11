import pandas as pd
#1
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6\n")
  
#2
i = 0
dat = [1,-2,3,-4,5,-6,7,-8,9,-10]
while i<len(dat):
    if dat[i]<0:
        print(dat[i])
    i=i+1
      
#3
students_data = {
   'Name': ['Student1', 'Student2', 'Student3', 'Student4', 'Student5'],
   'Height': [170, 175, 180, 185, 190],
   'Qualification': ['BSc', 'MSc', 'PhD', 'BSc', 'MSc']
}
print("\nThe dictionary is: ",students_data)
df = pd.DataFrame(students_data)
print("\nThe data frame is:\n",df,"\n")
addresses = ['Manipal', 'Mumbai', 'Jamshedpur', 'Pune', 'Kolkata']
df['Address'] = addresses
print("\nThe new data frame is:\n",df,"\n")

#4
print("\nThe dictionary is: ",students_data)
df = pd.DataFrame(students_data)
print("\nThe data frame is:\n",df,"\n")
addresses = ['Manipal', 'Mumbai', 'Jamshedpur', 'Pune', 'Kolkata']
addresses = ['Address1', 'Address2', 'Address3', 'Address4', 'Address5']
df.insert(3, 'Address', addresses)
print("\nThe new data frame is:\n",df,"\n")

#5
df1 = pd.DataFrame({'Name': ['Ram','Diya','Chandan','James','Alex']})
df2 = pd.DataFrame({
   'Maths': [80.0,90.0,77.5,87.5,86.5],
   'Physics': [81.0,94.0,74.5,83.0,82.5],
   'Chemistry': [91.5,86.5,85.5,90.0,91.0],
   'Biology': [82.5,83.5,84.5,85.0,93.0]
})
df_new = pd.concat([df1, df2], axis=1, ignore_index=True)
df_new.columns = ['Name', 'Maths', 'Physics', 'Chemistry', 'Biology']
print("\nThe new data frame is:\n",df_new,"\n")
df_new['Total'] = df_new[['Maths', 'Physics', 'Chemistry', 'Biology']].sum(axis=1)
print("\nThe new data frame is:\n",df_new,"\n")

#6
df1 = pd.DataFrame({'Name': ['Annie','Diya','Charles','James','Emily']})
df2 = pd.DataFrame({
   'Quiz_1/10': [8.0,9.0,7.5,8.5,6.5],
   'Insem_1/15': [11.0,14.0,14.5,13.0,12.5],
   'Quiz_2/10': [9.5,6.5,8.5,9.0,9.0],
   'Insem_2/15': [12.5,13.5,14.5,15.0,13.0]
})
df_new = pd.concat([df1, df2], axis=1, ignore_index=True)
df_new.columns = ['Name', 'Quiz_1/10', 'Insem_1/15', 'Quiz_2/10', 'Insem_2/15']
df_new['Total'] = df_new[['Quiz_1/10', 'Insem_1/15', 'Quiz_2/10', 'Insem_2/15']].sum(axis=1)
df_new.loc['Mean'] = df_new[['Quiz_1/10', 'Insem_1/15', 'Quiz_2/10', 'Insem_2/15','Total']].mean()
print(df_new)
