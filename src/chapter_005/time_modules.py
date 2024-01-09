# time modules

import time

# time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch)
print(time.time())
# time.sleep() stops the program for the given amount of seconds
time.sleep(5)
print('Hello')
# time.ctime() returns the current system time in a readable format
print(time.ctime())
# time.localtime() returns the current system time in a tuple format
print(time.localtime())
# time.strftime() returns the current system time in a readable format
print(time.strftime('%Y-%m-%d %H:%M:%S'))
# time.strptime() returns the current system time in a tuple format
print(time.strptime('2020-09-02 11:22:33', '%Y-%m-%d %H:%M:%S'))
# time.gmtime() returns the current system time in a tuple format
print(time.gmtime())

# program to calculate the time taken to execute the code
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print('Time taken to execute the code is: ', end-start)