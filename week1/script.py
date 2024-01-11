#1
x = int(input("Enter Length"))
y = int(input("Enter Breadth"))
print("Area: ",(x*y))
#2
x = int(input("Enter Val1"))
y = int(input("Enter Val2"))
x,y=y,x
print("(1,2): ",x,",",y)
#3
x = int(input("Enter Number"))
if x%2==0:
    print("Even")
else:
    print("odd")
#4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)

#5
list = ['physics', 'chemistry', 1997, 2000]
list.append('maths')
print(list)
del list[2]
print(list)
'physics' in list
'english' in list
len(list)
list.count('physics')
print(list)
list.pop()
print(list)
list.insert (2, 'maths')
print(list)
list.remove('chemistry')
print(list)
list.reverse()
print(list)
#6
x=(1,3,5,7,9,2,4,6,8,10)
y=len(x)/2
for i in x:
    print(i,end=',')
    if y==0:
        print()
    y=y-1
#7
x=(1,3,5,7,9,2,4,6,8,10)
y=len(x)/2
z=[]
for i in x:
    if i%2==0:
        z.append(i)
print(tuple(z))
#8
x=[11, -21, 0, 45,66, -93]
for i in x:
    if i<0:
        print(i)
#9
x=[11, -21, 0, 45,66, -93]
pos=neg=0
for i in x:
    if i<0:
        neg=neg+1
    elif i>0:
        pos=pos+1
print("Positive: ",pos,", Negative: ",neg)
#10
x=[11, -21, 0, 45,66, -93]
print(x)
for i in x:
    if i<0:
        x.remove(i)
print(x)