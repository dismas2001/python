#a program to calculate the net bonus amount
time = int(input("Enter your years of service"))
amount = int(input("Enter your salary"))
if (time>10):
    print("your bonus is 10%") 
elif(time>=6 and time<=10):
    print("your bonus is 8%")
elif(time<6):
    print("your bonus is 5%")
