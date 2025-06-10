#program to sort a list using only one loop
'''
ls=[10,2,30,40]
i=0
j=i+1
while(i<len(ls)):
    print("Values=>>",i,j)
    if(ls[i]>ls[j]):
        ls[i],ls[j]=ls[j],ls[i]
        print("after swap=>>",ls[i],ls[j])
    if(j!=len(ls)-1):
        j+=1
    else:
        i+=1
print(ls)
'''
'''
#Enamurate Function
ls1=[10,20,30]
for i in enumerate(ls1):
    print(i)
'''

questionbank=[{"Q":"What is the national animal of india?",
              "option":["A. Peacock","B. Lion","C. Tiger","D. Dog"],
              "Ans1":"C"},
              {"Q":"Who is the father of nation?",
              "option":["A. Rabindra nath tagore","B. Mahatma gandhi","C. Sharukh khan","D. Salman khan"],
              "Ans1":"B"}]

print("Welcome to kaun banega crorepati")
total_winning=0
prizemoney=[10000,25000]
for i,q in enumerate(questionbank):
    print(f"The {i+1} question for money{prizemoney[i]}is in front of you \n")
    print(q["Q"])
    for option in q["option"]:
        print(option)
    
    user_input=input("Choose any 1 option A, B, C, D or Press Q for quit ").upper()
    if(user_input=="Q"):
        print(f"Thank you for game and your total winning amount is {total_winning} ")
        break
    if(user_input==q["Ans1"]):
        total_winning+=prizemoney[i]
        print("Answer is correct GAME OVER")
    else:
        print("Answer is incorrect")
        break

print(total_winning)