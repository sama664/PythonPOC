# Lets Play with Loop

x=0
for index in range(10):
    print ("this is value of X {0}".format(x))
    x+=10

#explore range with start and Stop
y=5
for index in range(3,8):
    print ("this is value of Y {0}".format(y))
    y+=10
#explore range with incremet by 2
y=5
for index in range(3,8,2):
    print ("this is value of Y {0} when increment by 2".format(y))
    y+=10
#Play with break
y=3
for index in range(5):
    if index == 3:
        print("this will not print anymore while break")
        break
    print ("this is value of Y {0} ".format(y))
    y+=10

#Play with break
y=4
for index in range(5):
    if index == 2:
        print("this will  print apart form these", index)
        y=1
        continue
    print ("this is value of Y {0} ".format(y))
    y+=2