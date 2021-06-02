# daemon thread = a thread that runs in the background, not important
#                 for program to run. you program will not wait for daemon threads
#                 to complete before exiting.
#                 non-daemon threads cannot normally be killed, stay alive until task is complete

#                 usually used for: background tasks, garbage collection,
#                                   waiting for input, and long running processes

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")


# x = threading.Thread(target=timer)
# This will run infinitely because it cannot be killed

# This can be killed once main thread is completed
x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# This could also be used to set a thread to daemon
# must be specified before the x.start() function

# to check if the thread is a daemon or not:
print(x.isDaemon())

answer = input("Do you wish to exit?")
