def solu(start_date, end_date, login_dates):

  start_day = start_date[6:9]

  if start_day == 'MON':
    start_day = 1
  elif start_day == 'TUE':
    start_day = 2
  elif start_day == 'WED':
    start_day = 3
  elif start_day == 'TUR':
    start_day = 4
  elif start_day == 'FRI':
    start_day = 5
  elif start_day == 'SAT':
    start_day = 6
  elif start_day == 'SUN':
    start_day = 7

  start_date = [int(start_date[:2]),int(start_date[3:5])]
  end_date = [int(end_date[:2]),int(end_date[3:])]

  DDs = []
  count = 1
  max_days = 0

  for i in login_dates:
    M = int(i[:2])
    D = int(i[3:])
    DD = (D-start_date[1]) + 31 * (M-start_date[0])
    DD = (DD)%7 + 1
    if DD < 6:
      DDs.append(DD)

  
  for i in range(len(DDs)-1):
    now = DDs[i]
    next = DDs[i+1]
    
    if now + 1 == next:
      count += 1
    elif now == 5 and next == 1:
      count += 1
    else : 
      max_days = max(max_days, count)
      count = 1
  max_days = max(max_days, count)
    
  
  return max_days

a = solu("05/04","05/30",["05/06","05/07","05/08","05/21","05/22","05/23","05/25","05/26","05/27"])
print(a)
