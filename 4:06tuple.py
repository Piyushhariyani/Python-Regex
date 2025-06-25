#tuple
x=(10,20,"abc")
print(type(x))
#tuples are immutable
#we can't fo insert, update and delete
x=(10,20,"abc",10,10,40,90)
print(x.count(10))
print(x.index(40))
#list vs tuple
#[] , ()
#slower    

#Dictionary : datatype, use to store data but
'''
without indext position
data is store =>key,values
key is unique
value can be unique/duplicate
Dictionary are mutable
- no index position
key => data(unique)
--bill no:101
--101=> product?,kitna, kab(value)
key:value
Dictionary => why we create it 
'''
mydictionary={101:"tushar","salary":200000,"email":"tushar@gmail.com"}
print(mydictionary)
print(mydictionary["email"])

mydictionary["add"]= "jaipur"   #insert

print(mydictionary)

mydictionary.keys()

print()
mydictionary.values()

x=mydictionary.pop(101)
print(mydictionary,x)


mydict={10:"a","amount":6000}
for i in mydict:
    print(i,mydict[i])

for i in mydict.values():
    print(i)

mydict["amount"]=mydict["amount"]+5
print(mydict)



for i in range(1,6):
    for j in range(1,i):
        print(" ",end='')
    for k in range(1,6-i+1):
        print("*",end='')
    print()
for i in range(2,6):
    for j in range(1,6-i):
        print(" ",end='')
    for k in range(1,i+1):
        print("*",end='')
    print()

print()

num=int(input("Enter a range"))
a=0
b=1
print(a,b,end='  ')
for i in range(2,num):
    c=a+b
    print(c,end=' ')
    a,b=b,a
    b,c=c,a