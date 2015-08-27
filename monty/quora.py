#!/usr/bin/env python
 
import random
 
stay_win = 0
discard = 0
switch_win = 0
for i in range(0, 1000):
    car = randint(1,3)
    player = randint(1, 3)
    reveal = randint(1,3)

#    print "Car: " + str(car) + " Picked: " + str(player) + " Revealed: " + str(reveal)

    if reveal == car:
#        if reveal == player:
#            print "Monty revealed the car, and the player instantly won."
#        else:
#            print "Monty revealed the car, and the player instantly lost."
        discard += 1
    elif reveal == player:
#        print "Monty opened the player's door."
        discard += 1
    elif player == car:
#        print "Staying wins."
        stay_win += 1
    else:
#        print "Switching wins."
        switch_win += 1
    
       
print "Case 1: Random choice 1-3 to reveal"
print "  Staying won " + str(stay_win) + " cases."
print "  Switching won " + str(switch_win) + " cases."


# Variant for Monty never picks player's door

stay_win = 0
discard = 0
switch_win = 0

for i in range(0, 1000):
    car = randint(1,3)
    player = randint(1,3)
    
    if player == 1:
        # if player chose 1, make reveal range 2-3
        reveal = random.choice(tuple([2,3]))
    elif player == 2:
        # if player chose 2, make reveal 1 or 3
        reveal = random.choice(tuple([1,3]))
    else:
        # player chose 3, make reveal 1 or 2
        reveal = random.choice(tuple([1,2]))
    
    if reveal == car:
#        print "Monty revealed the car, and the player instantly lost."        
        discard += 1
    elif player == car:
#        print "Staying wins."
        stay_win += 1
    else:
#        print "Switching wins."
        switch_win += 1
        
print "Case 2: Monty flips a coin, opens a door the player didn't choose"
print "  Staying won " + str(stay_win) + " cases."
print "  Switching won " + str(switch_win) + " cases."


# Classic Variant: Monty always picks a door other than the player's, and it's
# always one with a goat

stay_win = 0
switch_win = 0

for i in range(0, 1000):
    car = randint(1,3)
    player = randint(1,3)
    
    reveal_choices = {1,2,3}
    reveal_choices.discard(car)  # Don't show the car.
    reveal_choices.discard(player)  # Don't open the player's door.
    reveal = random.choice(tuple(reveal_choices))
    
    if player == car:
#        print "Staying wins."
        stay_win += 1
    else:
#        print "Switching wins."
        switch_win += 1
        
print "Case 3 (Classic Monty Hall problem): Monty uses foreknowledge to open a door the player didn't choose and which shows a goat"
print "  Staying won " + str(stay_win) + " cases."
print "  Switching won " + str(switch_win) + " cases."
