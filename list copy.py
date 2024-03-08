accounts = [["1", "2", "3"], ["5", "6", "7"], ["1", "2"]]
y = [[int(i) for i in x] for x in accounts]
a = (sum(y[0]))
b = (sum(y[1]))
c = (sum(y[2]))

print(sum(a,b))