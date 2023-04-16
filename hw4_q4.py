#####Author= Naufil Bin Imran
######Assignment/ Part: HW4-Q4
########Date Due: 2022-03-03
############I pledge that I have completed this assignment without collaborating with anyone else, in conformance with the NYU School of Engineering Policies and Procedures on Academic Misconduct.


user_input = int(input("Please input any positive integer: "))
numbers_to_print = ''
for numbers in range(1, user_input+1):
    number= numbers
    even_count = 0
    odd_count = 0
    while number > 0:
        if (number % 10) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        number = number // 10

    if even_count > odd_count:
        numbers_to_print += ' ' + str(numbers)

print(numbers_to_print)
