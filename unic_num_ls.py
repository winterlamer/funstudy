
list = input()
list = list.split()
intls = []
intls = [int(item) for item in list]
print(intls)
unic_c = 0
for i in set(intls):
    print(intls.count(i))
    if intls.count(i) == 1:
        unic_c += 1

print(f"Количиство уникальных чисел {unic_c}")
