from turtle import *


fd = 10





print("?- for commands   off- to shut down")
question = input("hello, i am your drawing bot, please enter a command")
while question != 'off':
    if question == '?':
        print("here are your drawing commands:")
        print("w- forward")
        print("l- turn left on set degree")
        print("r- turn right on set degree")
        print("p- set pen size")
        print("c- draw circle in set size")
        print("d- set forward distance")
        print("h- hide turtle")
        print("pu - pen up")
        print("pd - pen down")
        print("gt- goto")
        print("sp- change speed")
    elif question == 'w':
        forward(fd)
    elif question == 'l':
        degree = int(input("what degree do you want to turn left?"))
        left(degree)
    elif question == 'r':
        degree1 = int(input("what degree do you want to turn right?"))
        right(degree1)
    elif question == 'p':
        ps = int(input("what pensize do you want to have?"))
        width(ps)
    elif question == 'c':
        cir = int(input("what circle size do you want to have?"))
        circle(cir)
    elif question == 'd':
        fdc = int(input("what length of the line do you want to have?"))
        fd = (fdc)
    elif question == 'h':
        hideturtle()
    elif question == 'pu':
        penup()
    elif question == 'pd':
        pendown()
    elif question == 'gt':
        xc = int(input("enter the x coordinate"))
        yc = int(input("enter the y coordinate"))
        goto(xc,yc)
    elif question == 'sp':
        sped = int(input("what speed do you want tot have?"))
        speed(sped)    
    else:
        print("?- for commands   off- to shut down")
    question = input("hello, i am your drawing bot, please enter a command")    


























































