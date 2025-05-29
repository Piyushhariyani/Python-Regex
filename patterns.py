for i in range(1,4):
    for j in range(1,5):
        print(i,end=' ')
    print()

for i in range(1,5):
    for j in range(1,5):
        print(j,end=' ')
    print()

for i in range(1,4):
    for j in range(4,0,-1):
        print(j,end=' ')
    print()

for i in range(4,1,-1):
    for j in range(1,4):
        print(i,end=' ')
    print()

k=1
for i in range(1,4):
    for j in range(1,4):
        print(k,end=' ')
        k+=1
    print()

for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()


for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=' ')
    print()

for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

for i in range(1,4):
    k=4
    for j in range(1,i+1):
        print(k,end=' ')
        k+=1
    print()

x=4
for i in range(1,5):
    for j in range(1,i+1):
        print(x,end=' ')
    x-=1
    print()

k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=' ')
        k+=1
    print()

for i in range(1,4):
    char=65
    for j in range(1,i+1):
        print(chr(char),end=" ")
        char+=1
    print()

char=65
for i in range(1,4):
    for j in range(1,i+1):
        print(chr(char),end=' ')
        char+=1
    print()

char=90
for i in range(1,4):
    for j in range(1,i+1):
        print(chr(char),end=" ")
        char-=1
    print()
           
for i in range (1,5):
    for j in range(5,i,-1):
        print("*",end='')
    print()

for i in range (1,5):
    x=4
    for j in range(5,i,-1):
        print(x,end='')
        x-=1
    print()

x=10
for i in range(1,4):
    for j in range(1,i+1):
        print(x,end='')
        x+=1
    print()

for i in range(1,5):
    ch=68
    for j in range(1,i+1):
        print(chr(ch),end='')
        ch-=1
    print()

for i in range(1,5):
    x=10
    for j in range(1,i+1):
        print(x,end='')
        x+=1
    print()

for i in range(1,5):
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end='')
        ch+=1
    print()

for i in range(1,5):
    ch=68
    for j in range(5,i,-1):
        print(chr(ch),end='')
        ch-=1
    print()

for i in range(1,6):
    for j in range(1,i+1):
        if(j%2==0):
            print("2",end='')
        else:
            print("1",end='')
    print()

ch=70
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(ch),end='')
        ch+=2
    print()

print()

for i in range(1,6):
    ch=65
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i,5):
        print(chr(ch),end='')
        ch+=1
    print()

print()

for i in range(1,6):
    ch=65
    for j in range(5,i,-1):
        print(i,end='')
    for k in range(1,i+1):
        print(chr(ch),end='')
        ch+=1
    print()

for i in range(1,5):
    for j in range(i,5):
        print("-",end='')

    for k in range (1,i+1):
        print("*",end = " ")

    print()

for i in range(5,1,-1):
    for j in range(1,i):
        print("-",end='')
    for k in range(1,i+1):
        print("*",end='')
    print()

print()

for i in range(1,6):
    for j in range(1,i+1):
        if(j==1 or i==5 or i==j):
            print("*",end='')
        else:
            print(" ",end='')
    print()

print()

for i in range(1,6):
    for j in range(1,6-i+1):
        if(j==1 or i==1 or j==5-i+1):
            print("*",end='')
        else:
            print(" ",end='')
    print()

print()

for i in range(1,6):
    for j in range(1,6):
        if(i==j or j==5 or i==1):
            print("*",end='')
        else:
            print("-",end='')
    print()

print()

