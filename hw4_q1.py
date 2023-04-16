#####Author= Naufil Bin Imran
######Assignment/ Part: HW4-Q1
########Date Due: 2022-03-03
############I pledge that I have completed this assignment without collaborating with anyone else, in conformance with the NYU School of Engineering Policies and Procedures on Academic Misconduct.


positive_integer=int(input("Please enter a positive integer: "))
first_even_number= positive_integer* 2
##this step is done to calculate range. If user inputs the any integer, multiplying it with 2 will make it the range, which we will use to print the first even n even numbers
number=1
print("Executing while loop....")
while number <= first_even_number:
    if number % 2== 0:
        print(number)
    number = number+1

print("Executing for loop....")
for number in range(1,first_even_number + 1):
    if number % 2 ==0:
        print(number)
