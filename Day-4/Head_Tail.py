# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

import random

random_toss=random.randint(0,1)

if random_toss==1:
    print("Heads")
else:
    print("Tails")