mylist=[10,20,30,40,50,60]
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
    print(total)  # Running sum

print()
 

for i in range(len(mylist)):
    for j in range(len(mylist)):
        if(mylist[i]+mylist[j]==50):
            print(mylist[i],mylist[j])

print()
#11
num=[1,2,3,4,5]
num1=[2,8,9,5,8]
num2=[]
for i in range(len(num)):
    for j in range(len(num1)):
        if(num[i]==num1[j]):
            num2.append(num[i])
print(num2)
#3
num = [1,2,3,4,5]
temp=0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]<num[j]):
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print(num)
#4
num = [5,76,8,23,4,90,1]
temp=0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]>num[j]):
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print(num)
#6
pairs=[]
target=int(input("Enter a target number"))
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]+num[j]==target):
            pairs.append((num[i],num[j]))
print(target,":",pairs)
#7
ls=[1,[2,3],[4,[5,6],7],8]
a=[]
for i in ls:
    if type(i)==list:
        for j in i:
            if type(j)==list:
                for k in j:
                    a.append(k)
            else:
                a.append(j)
    else:
        a.append(i)
print("Flattened list",a)
#8
num=[1,2,3,4,5]
small=num[0]
large=num[0]
for i in range(len(num)):
    if num[i] < small:
        small=num[i]
    
    if num[i] > large:
        large=num[i]
print(small)
print(large)
sum=0
for i in range(len(num)):
    if(num[i]!=small and num[i]!=large):
        sum+=num[i]
print(sum)
#9
ls=[1,2,3,2,1]
start=0
end=len(ls)-1
palindrome=True
while(start<end):
    if(ls[start]!=ls[end]):
        palindrome=False
        break

    start+=1
    end-=1

print(palindrome)

    

            


    
    
    

     

