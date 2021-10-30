import datetime

today = datetime.datetime.now() # package.module.function()
print(today)
print(type(today)) # <class 'datetime.datetime'>

day = today.weekday()
print(day) # 0~6(1)

if day >= 5 :
    print('주말')
else :
    print('평일')
