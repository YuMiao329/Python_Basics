import time

print(time.ctime(0))  # Thu Jan  1 08:00:00 1970 - the epoch time
# convert a time expressed in seconds since epoch to a readable string
# epoch =  when your computer thinks time began (reference point)

print(time.ctime(100))  # Thu Jan  1 08:01:40 1970
# returns 100 seconds after Thu Jan  1 08:00:00 1970

print(time.time())  # 1622634335.2802956 + seconds since epoch
# returns current seconds since epoch

print(time.ctime(time.time()))  # returns current date & time

# ----------------------------------------------------------------------------------------------------------------

# time.localtime() # creates time object on current local time
time_object = time.localtime()
# time.struct_time(tm_year=2021, tm_mon=6, tm_mday=2, tm_hour=19,
# tm_min=49, tm_sec=51, tm_wday=2, tm_yday=153, tm_isdst=0)
print(time_object)
# time.strftime(format, time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# %B: locale's full month name.
# %d: day of the month as a decimal number [01, 31].
# %Y: year with century as a decimal number.
# %H: hour as a decimal number [00, 23].
# %M: minute as a decimal number [00, 59].
# %S: second as a decimal number [00, 61].
print(local_time)  # June 02 2021 19:56:37

# ----------------------------------------------------------------------------------------------------------------

print(time.gmtime())  # UTC time

# ----------------------------------------------------------------------------------------------------------------

time_string = "20 April, 2020"
time_object2 = time.strptime(time_string, "%d %B, %Y")
print(time_object2)
# created a time object with detailed parameters
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=20, tm_hour=0,
# tm_min=0, tm_sec=0, tm_wday=0, tm_yday=111, tm_isdst=-1)

# ----------------------------------------------------------------------------------------------------------------

# asctime will convert tuple of time to a readable string
# tuple format: (year, month, day, hours, minutes, secs,
# #day of the week (0 as monday), #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string2 = time.asctime(time_tuple)
print(time_string2)  # Mon Apr 20 04:20:00 2020
time_seconds_since_epoch = time.mktime(time_tuple)
print(time_seconds_since_epoch)  # 1587327600.0
