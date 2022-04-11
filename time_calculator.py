def add_time(start, duration, day_of_week=None):
  day_index={"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}
  day_array=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  
  duration_period=duration.partition(":")
  print(duration_period)
  duration_period_hour=int(duration_period[0])
  duration_period_min=int(duration_period[2])
  
  start_duration=start.partition(":")
  start_period_start_min=start_duration[2].partition(" ")
  start_period_hour=int(start_duration[0])
  start_period_min=int(start_period_start_min[0])
  am_or_pm=start_period_start_min[2]
  am_or_pm_flip={"AM":"PM","PM":"AM"}

  day=int(duration_period_hour/24)
  
  end_minutes=start_period_min+duration_period_min

  if (end_minutes >= 60):
    start_period_hour += 1
    end_minutes = end_minutes % 60
  amount_of_am_or_pm=int((start_period_hour + duration_period_hour)/12)
  end_hours=(start_period_hour+duration_period_hour)%12

  end_minutes=end_minutes if end_minutes > 9 else "0" +str(end_minutes)
  end_hours=end_hours=12 if end_hours == 0 else end_hours

  if (am_or_pm == "PM" and start_period_hour + (duration_period_hour % 12) >= 12):
    day+=1
  am_or_pm = am_or_pm_flip[am_or_pm] if amount_of_am_or_pm % 2 == 1 else am_or_pm
  returnTime=str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm

  if (day_of_week):
    day_of_week = day_of_week.lower()
    index = int((day_index[day_of_week]) + day)%7
    new_day = day_array[index]
    returnTime += ", " + new_day
  if (day == 1):
    return returnTime + " " + "(next day)"
  elif (day > 1):
    return returnTime + " (" + str(day) + " days later)"
    



  return returnTime