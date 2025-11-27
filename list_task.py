import math



list = input()
list = list.split()
intls = []
#print(list)
intls = [int(item) for item in list] # idk how do it without stackoverflow
print(intls)
result = math.prod(intls)
print(result) 