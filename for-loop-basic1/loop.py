for y in range (0,151):
    print(y)
# multiples of 5
for x in range (5,1001):
  if x%5 == 0:
    print(x)
#  counting the dojo way
def dojo_way():
    for i in range (1,100+1):
        if i % 5 == 0:
            print ('Coding')
        if i % 10 == 0:
            print ('Dojo')

dojo_way()

#  whoa that suckers huge
sum = 0
for d in range(500000):
    if d % 2 != 0 and d % 3 ==0:
      d += d
      sum = d
      print(sum)

# Countdown by Fours
for z in range(2018,0,-4):
  print(z)


# flexible counter

lowNum=2
highNum=9
mult=3

for v in range(lowNum,highNum+1):
  if v % mult ==0:
    print(v)