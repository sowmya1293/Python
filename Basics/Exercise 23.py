#Write a code to create a simple countdown timer of 5 seconds using a while loop.
#Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.

import time

def countdownTimer():
    i=5

    while(i>=0):
        if(i==0):
            print("Time's up")
            break
        else:
            print("Time remaining ",i," seconds")
            time.sleep(1)
            i-=1

countdownTimer()