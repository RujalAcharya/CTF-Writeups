req =  523693181734689806809285195318


sol = 0
i = 0
j = 0

for n in range(req):
    sol +=1
    i += 1
    if i == 3:
        i = 0
        j +=1
        sol +=1
        if j == 3:
            j = 0
            sol += 1

print(sol)
