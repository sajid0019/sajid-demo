import random
import time
val = random.randint(1,50)
time_start = time.time()
time_period = 30
while True:
    inp = int(input("Guess the value :"))
    elapsed_time  = time.time() - time_start
    if  elapsed_time > time_period:
        print("Time is up !!!...😓")
        break
    if  inp > val:
        print("you choosed higher number")
    elif    inp < val:
        print("you choosed lower number")
    elif    val == inp :
        print(f"Guess is correct Bingo!!😎😎 number is {val}")
        break
    
    
        
