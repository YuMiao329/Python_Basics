# thread = a flow of execution. Like a separate order of instructions.
#          However each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock).
#          allows only one thread to hole the control of the Python interpreter

# cpu bound = program/task spends most of it's time waiting for internal events
#             (CPU interpreter: use multiprocessing)

# io bound = program/task spends most of it's time waiting for external events
#            (user input/web scraping: use multithreading)

import threading
import time


# create a program two threads run concurrently (one is running while the other is idle)
def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finished study")


# eat_breakfast()  # takes 3 seconds before printing "You ate breakfast"
# drink_coffee()  # takes additional 4 seconds before printing "You drank coffee"
# study()  # takes additional 5 seconds before printing "You finished study"


# This will finish in sequence.
# The next task needs to wait for the previous one to finish

print(threading.active_count())  # 1
print(threading.enumerate())  # [<_MainThread(MainThread, started 12408)>]

# --------------------------------------------------------------------------

# To do tasks concurrently, we need to add threads in each method
def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finished study")


# remember target=function with no ()
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# add join() functions to let main thread to wait for other 3 threads to complete
# the perf_counter() will be the total time
# main thread wait for x, y, and z threads to join and wait them to finish
x.join()
y.join()
z.join()

print(threading.active_count())  # 4
# the job of main thread is to create 3 additional threads and print statements
# other three threads are used for 3 variable x, y, z functions
print(threading.enumerate())  # [<_MainThread(MainThread, started 10496)>, <Thread(Thread-1, started 6308)>, <Thread(
# Thread-2, started 14648)>, <Thread(Thread-3, started 2968)>]
print(time.perf_counter())  # main threads finish its task in 0.0580815 s
