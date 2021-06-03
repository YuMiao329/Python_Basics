# multiprocessing = running tasks in parallel on different cpu cores,
#                   bypasses GIL used for thread.

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print("You have: ", cpu_count(), " cores")
    # If assign more cores than have:
    # it takes longer time

    a = Process(target=counter, args=(250000000,))
    # if only one core processes 1000000000 works:
    # finished in:  53.6432715 seconds
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()
    # if four cores run in parallel it only takes :
    # finished in:  13.8267121 seconds

    print("finished in: ", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()
# for Windows system add this
# to make sure its not running child process which will cause problem
