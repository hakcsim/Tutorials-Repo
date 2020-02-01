import datetime

# native date time: no time zone, daylight saving time
# aware date time

d = datetime.date(2017, 2, 24)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.weekday())     # Monday 0 Sunday 6
print(tday.isoweekday())  # Monday 1 Sunday 7

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(2020, 8, 30)

till_bday = bday - tday
print(till_bday)
print(till_bday.total_seconds())

t = datetime.time(9, 20, 45, 100000)
print(t)
print(t.hour)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)
print(dt.year)
print(dt.date())
print(dt.time())
print(dt + tdelta)

tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

# all these are not aware date time
dt_today = datetime.datetime.today()    # no time zone
dt_now = datetime.datetime.now()        # time zone option 
dt_utcnow = datetime.datetime.utcnow()  # not time zone aware, tztinfo is still none.

print(dt_today)
print(dt_now)
print(dt_utcnow)

# aware date time from hereon
import pytz

dt = datetime.datetime(2016,7,27,12,30,45, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) 
print(dt_utcnow)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_et = dt_utcnow.astimezone(pytz.timezone('US/Eastern')) 
print(dt_et)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain')) 
print(dt_mtn)

for tz in pytz.all_timezones:
    print(tz)

# convert native date time to time zone aware date time

dt = datetime.datetime.now()        # native date time
et_tz = pytz.timezone('US/Eastern')
dt = et_tz.localize(dt)             # time zone aware
print(dt)

dt_mtn = dt.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 26, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

print("="*20)

import calendar

balance = 5000
annual_interest_rate = 0.13
monthly_payment = 500
monthly_interest_rate = annual_interest_rate / 12

today = datetime.date.today()

(first_day_in_month, days_in_current_month) = calendar.monthrange(today.year, today.month)
days_till_end_month = days_in_current_month - today.day
print(days_till_end_month)

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
print(start_date)
end_date = start_date

while balance > 0:
    interest_charge = monthly_interest_rate * balance
    balance += interest_charge
    balance -= monthly_payment

    balance = 0 if balance < 0 else round(balance, 2)

    print(end_date, balance)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date += datetime.timedelta(days=days_in_current_month)

print("="*20)

current_weight = 220
goal_weight = 180
average_lbs_week = 1.5

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= average_lbs_week

print(end_date)
print(f'Reach goal in {(end_date - start_date).days // 7}')

print("="*20)

import math

goal_subs = 100000
current_subs = 85000
subs_to_go = goal_subs - current_subs 

avg_subs_day = 200
days_to_go = math.ceil(subs_to_go / avg_subs_day)

today = datetime.date.today()
print(days_to_go)
print(today + datetime.timedelta(days=days_to_go))

















