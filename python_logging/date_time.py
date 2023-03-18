import datetime
import pytz

"""

############################ working with 'date' using 'datetime' module ####################
when we work with 'date' in datetime module then we are only working with year,month and date
We can not use hour, minutes and seconds while working with 'date'
"""

d = datetime.date(2023,3,12)
print(d)
"""
Output : -->>
2023-03-12
"""
today_date = datetime.date.today()
print(today_date)
"""
Output :-->
2023-03-12
"""
print(today_date.weekday())
"""
Output :-->
6
Monday = 0 , Sunday = 6
"""
print(today_date.isoweekday())
"""
Monday = 1 , Sunday = 7
Output :-->
7
"""

################## timedelta ###############
##################           ###############
tdelta = datetime.timedelta(days = 7)
print(today_date + tdelta)
"""
Output :-->>
2023-03-19

Explanation : 
date2 = date1 + timedelta
timedelta = date2 -/+ date1
"""
"""
*************************************************************************************************
###################################### Working with 'time' using 'datetime' module ##############
Here we are working with hour, minutes and seconds
we can not use year months or date while working with 'time'
"""

t = datetime.time(9,30,45,10000)
print(t)
"""
Output :-->
09:30:45.010000
"""

"""
*************************************** Working with 'datetime' ***********************************
With 'datetime' we can work with date along with time 
"""
dttm = datetime.datetime(2023,3,12,9,30,45,1000)
print(dttm)
"""
Output
2023-03-12 09:30:45.001000
"""
print(dttm.time())
"""
Output :-->>
09:30:45.001000
"""
print(dttm.year)
"""
Output :-->
2023
"""
tmdelta = datetime.timedelta(hours = 7)
print(dttm + tmdelta)
"""
Output :-->>
2023-03-12 16:30:45.001000
"""
dttm_today = datetime.datetime.today()
dttm_now = datetime.datetime.now()
dttm_utcnow = datetime.datetime.utcnow()

print("dttm_today : ",dttm_today)
print("dttm_now :",dttm_now)
print("dttm_utcnow :",dttm_utcnow)

"""
Output :-->>
dttm_today :  2023-03-12 19:55:45.572010
dttm_now : 2023-03-12 19:55:45.572009
dttm_utcnow : 2023-03-12 14:25:45.572009

*********** Difference between 'datetime.datetime.today()' and 'datetime.datetime.now()' **************
 datetime.datetime.today() will give today date and time  local 
 but, in datetime.datetime.now() we can pass timezone and it will return that date and time zone

"""
"""
**************************************** Working with 'pytz' *********************************
****************************************                     *********************************
"""
dt_pytz = datetime.datetime(2013,3,12,12,30,45,10000,tzinfo=pytz.UTC)
print("dt_pytz : ",dt_pytz)
"""
Output :-->>
dt_pytz :  2013-03-12 12:30:45.010000+00:00
"""
dt_pytz_now = datetime.datetime.now(tz = pytz.UTC)
print("dt_pytz_now : ",dt_pytz_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
print("dt_utcnow : ",dt_utcnow)
"""
Output :-->>
dt_pytz_now :  2023-03-12 14:43:18.170890+00:00
dt_utcnow   :  2023-03-12 14:43:18.170890+00:00
*********************
In output we can see that both method line 123 and 124 return same date time, means 
we can use any one of these two to get UTC now time , but we prefer first method 
bcz second method is complex in writing 
"""
"""
********************** Converting UTC time zone in another required time zone *************** 
"""
dt_pytz_now = datetime.datetime.now(tz = pytz.UTC)

dt_US_mount_timezone = dt_pytz_now.astimezone(pytz.timezone('US/Mountain'))
print("dt_pytz_now : ",dt_pytz_now)
print("dt_US_mount_timezone :",dt_US_mount_timezone)
"""
Output :-->
dt_pytz_now :  2023-03-12 14:53:27.893775+00:00
dt_US_mount_timezone : 2023-03-12 08:53:27.893775-06:00
"""
"""
*********************************************** Important Note :-->> **************************
We can not convert 'naive' time to required time zone 
We can only convert time zone aware date time to our required time zone 
we will understand it with below example 
"""
local_time = datetime.datetime.now()
print("local_time :",local_time)
print("type of date time :",local_time.tzinfo)
"""
Output :-->>
local_time : 2023-03-12 20:36:11.343319
type of date time : None
"""
# here 'local_time' is not time zone aware, 
# now we will try to convert it in another time zone and we will get error
dt_east = local_time.astimezone(pytz.timezone('US/Mountain'))
print("dt_east :",dt_east)
print("type of time zone :",dt_east.tzinfo)
"""
Output :->>
dt_east : 2023-03-12 09:23:53.670682-06:00
type of time zone : US/Mountain

Confusion :-->>> Here naive date time has been converted to another time zone while it was supposed 
not to be converted, will check this later
"""

"""
*********************************** Use of 'strftime' *************************************
***********************************                   *************************************
this function is used to convert any date time to a required format(string format)
"""
local_date_time_zone_aware = datetime.datetime.now(tz = pytz.timezone('Asia/Calcutta'))
print("local_date_time_zone_aware :",local_date_time_zone_aware)
print("type of zone :",local_date_time_zone_aware.tzinfo)
"""
Output :-->
local_date_time_zone_aware : 2023-03-12 21:47:16.732145+05:30
type of zone : Asia/Calcutta
"""
# now we will convert this date time in a required format using 'strftime' function
strftime_fmt = local_date_time_zone_aware.strftime('%B %d, %Y')
print("required format :",strftime_fmt)
"""
Output :-->>
required format : March 12, 2023

Note :--> There are other multiple formats ,can be found in python documentation
"""

"""
************************************* Use of 'strptime' ******************************
*************************************                   ******************************
This function is used to convert a date time string into 'datetime' format
"""
string_date_time = 'March 12, 2023'
datetime_fmt = datetime.datetime.strptime(string_date_time,'%B %d, %Y')
print("datetime_fmt :",datetime_fmt)
"""
Output :-->
datetime_fmt : 2023-03-12 00:00:00
"""