def convert (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

nu = []
for j in range(int(input())):
    count = 0
    n=1
    while(n<=j):
	    str1=convert(n)
	    str2=convert(n-1)
	    str2='0'*(len(str1)-len(str2))+str2
	    for i in range(len(str1)):
		    if(str1[i]!=str2[i]):
			    count+=1
	    n+=1

    nu.append(count)

print(nu)