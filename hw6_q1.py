#####Author= Naufil Bin Imran
######Assignment/ Part: HW6-Q1
########Date Due: 2022-03-31
############I pledge that I have completed this assignment without collaborating with anyone else, in conformance with the NYU School of Engineering Policies and Procedures on Academic Misconduct.


def print_shifted_triangle(height,margin,symbol):
    no_of_spaces= height + margin
    for no_of_rows in range(1, height+1):   
        spaces_to_be_printed=no_of_spaces-no_of_rows
        print(" "*(spaces_to_be_printed)+(symbol)*((2*no_of_rows)-1))
    

def print_pine_tree(levels,symbols):
    for pine_design in range(1,levels+1):
        height_shifted_triangle=pine_design +1
        margin_shifted_triangle=levels-pine_design
        print_shifted_triangle(height_shifted_triangle,margin_shifted_triangle, symbols)


def main():
    character=True
    positive_integer=0
    while positive_integer <= 0 or character == True:
        positive_integer=int(input("Enter a positive, non-zero, integer: "))
        input_character=input("Enter a non-whitespace, non-alphanumeric character: ")
        character=input_character.isalnum() or input_character.isspace()
        
    print_pine_tree(positive_integer, input_character)

main()  

