#####Author= Naufil Bin Imran
######Assignment/ Part: HW4-Q5
########Date Due: 2022-03-03
############I pledge that I have completed this assignment without collaborating with anyone else, in conformance with the NYU School of Engineering Policies and Procedures on Academic Misconduct.

import turtle

polygon_shape = int(input("Please enter the shape of polygon you would like to use for your design: "))
for Zelijj in range(0, 21):
    for side in range(0, polygon_shape):
        turtle.forward(50)
        turtle.left(360/polygon_shape)
    turtle.left(360/20)
