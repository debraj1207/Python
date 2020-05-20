# python program to illustrate If else statemen:

a=5
if(a==5):
    print("correct")
else:
    print("wrong")




# python program to illustrate nested If statement


#can i buy a chocolate?

money=100                #money you have
item=80                  #amount of money used for items
chocolate=30             #price of chocolate
toffy=10                 #price of toffy
if(money-item>chocolate):
    print("yes, you can buy a chocolate")
elif(money-item>toffy):
    print("no, but you can buy a toffy")
else:
    print("no, you cant buy anything")