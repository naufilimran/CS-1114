
#####Author= Naufil Bin Imran
######Assignment/ Part: HW4-Q2
########Date Due: 2022-03-03
############I pledge that I have completed this assignment without collaborating with anyone else, in conformance with the NYU School of Engineering Policies and Procedures on Academic Misconduct.

user_input = int(input(" Please enter a positive integer: "))
asterisks = ((2*user_input)-1)

#astericks are odd so this equation is used

max_asterisks = asterisks
bottom_max_asterisks = 3

#appointed a value of 3 because after asterick is 1 it will always increase to 3

while max_asterisks >= 1 or bottom_max_asterisks <= asterisks:
    if max_asterisks > 1:
        print(' ' * ((asterisks - max_asterisks)//2), '*' * max_asterisks)
        max_asterisks -= 2
    elif max_asterisks == 1:
        print(' ' * ((asterisks - max_asterisks)//2), '*' * max_asterisks)
        max_asterisks -= 2
    if max_asterisks < 1 and bottom_max_asterisks <= asterisks:
        print(' ' * ((asterisks-bottom_max_asterisks)//2), '*' * bottom_max_asterisks)
        bottom_max_asterisks += 2
