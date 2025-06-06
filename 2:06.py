#call by refrence
age=10
print("Memory address of age=>",id(age))
x=age
print("Memory address of x=>",id(x))
x=20
print("new memory of x",id(x),id(age))
#append
mylist=[10,20,"abc"]
mylist.append(199)
print(mylist)
#update element
print(mylist)
mylist[0]=9
print(mylist)

print()

#pop
print(mylist)
x=mylist.pop()
print(mylist,x)

print()

#Questions
list1=[10,20,30,40,3,2,70]
for i in list1: #execute loop directly => iterable
    print(i)

print()

for index in range(len(list1)):
    if(list1[index]>20):
        print(list1[index])

print()

list2=[]
for i in range(len(list1)):
    if(list1[i]%2==1):
        list2.append(list1[i])
print(list2)

print()

min=list1[0]
for i in range(len(list1)):
    if(list1[i]<min):
        min=list1[i]
print(min)

print()

max=list1[0]
count=0
for i in range(len(list1)):
    if(list1[i]>max):
        max=list1[i]
print(max)

print()

mylist=[10,20,30,40,50,70]
for i in range(len(mylist)):
    if(type(mylist[i]) == int):
        print(mylist[i])

print()

max=mylist[0]
smax=0
for i in range(len(mylist)):
    if(mylist[i] > max):
        smax=max
        max=mylist[i]
    elif(mylist[i]>smax):
        smax=mylist[i]
print(max,smax)

print()

total=0
for i in range(len(mylist)):
    total+=mylist[i]
    print(total)

