#Task1
def calculator(a,b):
    print(f"Addition of two numbers is:{a+b}\nSubraction of two numbers is:{a-b}\nDivision of two numbers is:{a//b}\nMultiplication of two numbers is:{a*b}")
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
calculator(a,b)

#Task2
def covid(name,body_temperature=98):
    print(f"Name:"+name,"\nBody Temperature:"+str(body_temperature))
covid("arjun")
covid("sreeram",98.6)