n = int(input("How many items do you want to add: "))
lst = []
for i in range(n):
    lst.append(input("Enter object: "))
b = int(input('''
Which comprehension you want to do?
Press 1 for list
Press 2 for dict
Press 3 for set
'''))
if b==1:
    clst = [i for i in lst]
    print(f"LIST: {clst}")
elif b==2:
    cdict = {i:f"Item {i}" for i in lst}
    print(f"DICT: {cdict}")
elif b==3:
    cset = {i for i in list}
    print(f"SET: {cset}")
else:
    print("Invalid input")