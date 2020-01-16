# __str__ Method

#inside class Time:
  
  def __str__(self):
      return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    
 
time = Time(9, 45)
print(time)
09:45:00
    
#operator overloading
    
def __add__(self, other)
    seconds = self.time_to_init() + other.time_to_int()
    return int_to_time(seconds)
  
start = Time(9,45)
duration = Time(1, 35)
print(start + duration)
11:20:00
