
# To Find that the number is even or an odd number

num1 = int(input("Enter 1st number: "))         
if(num1 % 2 ==0):
    print(num1, " is even number")
else:
    print(num1, " is Odd number")


# Assignement for finding percentage of marks

physics = input("Enter marks in Physics: ")
chemistry = input("Enter marks in chemistry: ")
Maths = input("Enter marks in Maths: ")
pakistan_Study = input("Enter marks in pakistan_Study: ")
Urdu = input("Enter marks in Urdu: ")
English = input("Enter marks in English: ")
Islamiat = input("Enter marks in Islamiat: ")

sumOfObtainedMarks =int(physics) + int(chemistry) + int(Maths) + int(pakistan_Study) + int(Urdu) + int(English) + int(Islamiat)
totalMarks = 700
percentageOfTotalMarks = (sumOfObtainedMarks * 100)/totalMarks
print("Percentage of Total Marks is = ",percentageOfTotalMarks)