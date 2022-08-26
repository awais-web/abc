# Project task
# create a list of 1000 integers and create new list of numbers divisible by 77 and than find its quantity


list1 = list(range(1,1001))

newlist = [x for x in list1 if x % 77 == 0]
print(newlist)