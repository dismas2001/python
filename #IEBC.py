#checking if you belong to east african countries
age = int(input("Enter yuor age:"))
countries = ['kenya', 'Uganda' , 'Tanzania']
country = (input ("Enter country: "))
if country in countries and age >=18:
    print("Eligible to vote")
else:
   print("Not eligible to vote") 