# Reading a CSV file & XLS file format
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('xyz.csv',header=None)
print(df.head()) #This will display 1 st 5 records
print(df.tail()) #This will display last 5 records
#The above dataset doesn’t have header, we shall attach our own header.
df.columns=['preg','glu','bp','sft','ins','bmi','dpf','age','class']
#Let us visualize the scatter plot of two continuous variable.
plt.scatter(df['bmi'],df['glu'])
plt.xlabel('bmi')
plt.ylabel('Glucose')
plt.show()
#Let us visualize the histogram of another continuous variable 'Age’
df['age'].hist()
plt.hist(df['age'])
plt.show()
plt.boxplot(df['age'])
plt.show()
#Let us visualize the distribution 'Age’ with respect to Categories: Label-O(Healthy), Label-1 (Diabetes)#We can observe the median age of diabetes is slightly greater than median age of healthy

W = pd.read_csv('xyz.csv',header=None)
print(W.head()) #XLS file format also, we can read using pd.read_csv
D= np.loadtxt('xyz.txt',delimiter=",")
print(D[:5,:]) # this file is loaded in Numpy 2D array format
# Reading a XLSX file format
# G=pd.read_excel('xyz.xlsx',sheet_name='Sheet1')
# G.head()
#Here additionally we need to pass the sheet_name. If not specified, it will read the first page by default.

B = pd.read_html('Test.html')
for df in B:
    print(df.head())
# Reading a TXT file format
H = pd.read_table('HR.txt')
print(H.dtypes)
f=H['Department'].value_counts()
#We can visualize the distribution of categorical values using bar plot and pie chart
# Count the occurrences of each department
import pandas as pd
import matplotlib.pyplot as plt

# Count the occurrences of each department
department_counts = H['Department'].value_counts()

# Get the unique departments
unique_departments = H['Department'].unique()

# Create the bar chart
plt.bar(unique_departments, department_counts.values)

# Add labels and title
plt.xlabel('Department')
plt.ylabel('Count')
plt.title('Distribution of Departments')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=90)

# Display the plot
plt.show()

