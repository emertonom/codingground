#!/usr/bin/env python
 
from random import randint
 
win = 0
for i in range(0, 1000):
    car = randint(1, 3)
    player = randint (1, 3)
    
    while True:
        reveal = randint(1, 3)
        if (reveal == player):
           continue
        if (reveal == car):
           continue
        break
           
    print "Car not behind door " + str(reveal) + "!"

    if player == car:
        print "Staying wins!"
        win += 1
    else:
        print "Switching wins!"
    
print "You won " + str(win) + " out of 1000 cases!"
print "This is " + str(win / 10.0) + " percent!"
