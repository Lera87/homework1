s = "I'm learning Python"
print(s, type(s))
s2 = """
abc
def
ghj
"""
print(s2, type(s2))

"""
My comment line 1
My comment line 2
My comment line 3
"""

path = 'C:temp\new\folder'
path2 = r'C:temp\new\folder'
print(path)
print(path2)

s3 = '\u45dd'
print(s3)
s3_1 = '\u26BD'
print(s3_1)
s3_2 = u"\U0001F339"
print(s3_2)

s4 = "Hillel"
print(s4[0])
print(s4[0:3])
print(s4[:3])
print(s4[3:])
print(s4[:])

#time = "18:23:01"
#посчитать общее колво секунд, которые прошли с начала суток
       #01234567
time = "09:32:01"
hours = int(time[0:2])
print(hours)
minutes = int(time[3:5])
print(minutes)
seconds = int(time[6:])
print(seconds)
total_seconds = hours*3600 + minutes*60 + seconds
print(total_seconds)

time = "19:2:01"
lst = time.split(':')
print(lst)
print(type(lst))
#print(lst[0], lst[1], lst[2])
hours = int(lst[0])
minutes = int(lst[1])
seconds = int(lst[2])
total_seconds = hours*(60*60) + minutes*60 + seconds
print(total_seconds)

str = "abcd"
var1 = 42
print(type(var1))
var1 = "42"
print(type(var1))





