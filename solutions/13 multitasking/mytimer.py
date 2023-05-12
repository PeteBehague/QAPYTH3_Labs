#! /usr/bin/python
"""
This user written module contains a simple mechanism for
timing operations from Python.  It contains two functions,
start_timer(), which must be called first to initialise the
present time, and end_timer() which calculates the elapsed
CPU time and displays it.

>>> start_timer()
>>> end_timer() # doctest: +ELLIPSIS
End time    : 0.000 seconds
Alt End time:... seconds
"""
import datetime
import timeit
import time
import os
ostime_start_time = 0
processtime_start_time = 0
alt_start_time = 0
timeit_start_time = 0


########################################################
# TIMER FUNCTIONS
def start_timer():
    """
    The start_timer() function marks the start of 
    a timed interval, to be completed by end_timer().
    This function requires no parameters.
    """
    global ostime_start_time
    global processtime_start_time
    global alt_start_time
    global timeit_start_time

    (utime, stime) = os.times()[0:2]
    ostime_start_time = utime + stime  # CPU exection Time
    processtime_start_time = time.process_time()  # CPU exection Time
    alt_start_time = datetime.datetime.now()  # Wall Clock time
    timeit_start_time = timeit.default_timer()  # Wall Clock time

    return

def end_timer(txt='End time'):
    """
    The end_timer() function completes a timed interval
    started by start_timer.  It prints an optional text
    message (default 'End time') followed by the CPU time
    used in seconds.
    This function has one optional parameter, the text to 
    be displayed.
    """
    global ostime_start_time
    global alt_start_time
    global timeit_start_time
    global processtime_start_time

    if ostime_start_time == 0:
        raise SystemError('end_timer() called without a start_timer()')
    (utime, stime) = os.times()[0:2]
    end_time = utime + stime
    alt_end_time = datetime.datetime.now()
    timeit_end_time = timeit.default_timer()
    processtime_end_time = time.process_time()
    time_diff = alt_end_time - alt_start_time
    timeit_total_time = timeit_end_time - timeit_start_time
    processtime_total_time = processtime_end_time - processtime_start_time

    print("{0:<12}: {1:01.3f} seconds".format(txt, end_time - ostime_start_time))  # CPU exection Time
    print("{0:<12}: {1} seconds".format("ProcessTime " + txt, processtime_total_time))  # CPU exection Time
    print("{0:<12}: {1} seconds".format("Alt " + txt, time_diff.total_seconds()))  # Wall Clock time
    print("{0:<12}: {1} seconds".format("Timeit " + txt, timeit_total_time))  # Wall Clock time


    ostime_start_time = 0
    return

        
if __name__ == '__main__':
    import doctest
    doctest.testmod()


