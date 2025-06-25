#Functions 
#block of code => repetative usage
#code redable, code reusability
# user defined, in_built functions 
'''
#with using input 
def greet():
    name=input("Enter your name ")
    print(f"Hello {name} i welcome you onboard")
greet()
'''
#passing a value to function 
def greet1(z): #parameter / formal parameter 
    print("Hello",z,"i welcome you onboard")

greet1("piyush")

#Factor function
def factors(num):
    for i in range(1,num+1):
        if(num%i==0):
            print("Factor of",num,"is",i)

factors(64)

#armstrong
'''
def arm(num):
    num1=num
    count=0
    sum=0
    temp=0
    while(temp>0):
        count+=1
        temp//=10
    temp=num
    while(temp>0):
        digit=temp%10
        sum+=digit**count
        temp//=10
    if(sum==num1):
        print(f"{num} is a armstrong number ")
    else:
        print("Not a armstrong number")
'''
#type of argument passing 
def func(id,name,salary=978):
    print(f"Id is {id} name is {name} and salary is {salary}")

func(1,"yash",900) #Required argument => parameter == value /argument 
func("yash",1,900) #Positional argument matters here
func(id=1,salary=900,name="yash") #Keyword argument 
func(1,"Piyush") #Default argumnet 
#we can set a default value for any argument in fun afterwards if we wan to change that value we also can

#Combination of keyword and positional argument 
#if we start with keyword argument then all arguments after that will follow keyword argument 
func(10,name="Abhishek",salary=8999)

def lcm(a,b,c):
    if(a>b):
        grt=a
    else:
        grt=b
    while True:
        if(grt%a==0 and grt%b==0):
            lcm=grt
            break
        grt+=1
    if(lcm>c):
        grt1=lcm
    else:
        grt1=c 
    while True:
        if(grt1%lcm==0 and grt1%c==0):
            lcm1=grt1
            break
        grt1+=1
    print(lcm1)  

lcm(2,4,36)

#First class function and its property 