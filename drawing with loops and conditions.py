#Making use of all that we have learnt like operators, loops, turtle function,

import turtle #importing turtle library
t=turtle.Pen()#using one of the function inside turtle library and assigning value to t

t.color('blue','green') #using another function inside the library turtle
t.begin_fill()#using another function inside the turtle library

count=0 #making the initial value with assignment operator

#draw a star

for x in range(1,9): #starting of a loop
    t.forward(300)
    t.left(225)#asking the pointer to move 225 degree left
    count=count+1#asking to add 1 to the count
    print("Count is:" + str(count)) #converting integer to string as we cannot print string with integer

    #stop drawing after 8 loops
    #if count>7 and count<9:
    if count>7:
        print("the star pattern is complete")
        #break

t.end_fill()#using another function inside turtle to end the fill
print("A star is born")

#End of the program
