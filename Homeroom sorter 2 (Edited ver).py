last_name = (input("what is the first letter in your last name"))
last_initial = last_name[0]

x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
y = ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

if last_initial in x:
    print("Homeroom 101")
elif last_initial in y:
    print("Homeroom 102")
else:
    print("Homeroom 103")