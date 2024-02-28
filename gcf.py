
ans = 1

def gcf():
    global ans
    n = int(input("choose any number"))
    n2 = int(input("choose another number"))
    if n > n2:
        num = n
        smolnum = n2
    else:
        num = n2
        smolnum = n
    for i in range (1, smolnum):
        if (num%i == 0) and (smolnum%i == 0):
            ans = i
            i = 0

gcf()

print(ans)





