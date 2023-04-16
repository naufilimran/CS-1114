#####Author= Naufil Bin Imran
######Assignment/ Part: HW4-Q3
########Date Due: 2022-03-03
############I pledge that I have completed this assignment without collaborating with anyone else, in conformance with the NYU School of Engineering Policies and Procedures on Academic Misconduct.


user_number= int(input("Please enter a positive integer: "))

for values in range(1, user_number+1):
    string_to_print = " " * (user_number - values)
    
    for integers in range(1, values+1):
        string_to_print += str(integers)
        
    print(string_to_print)

    
