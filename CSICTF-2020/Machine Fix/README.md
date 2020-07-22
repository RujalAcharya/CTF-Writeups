# Machine Fix
<h3>Description</h3>
 We ran a code on a machine a few years ago. It is still running however we forgot what it was meant for. It completed n=523693181734689806809285195318 iterations of the loop and broke down. We want the answer but cannot wait a few more years. Find the answer after n iterations to get the flag.<br>
 The flag would be of the format csictf{answer_you_get_from_above}.
 
 
 <strong> File Included: </strong> <a href='https://github.com/TheFakeS1imShady/CTF-Writeups/blob/master/CSICTF-2020/Machine%20Fix/code.py'>code.py</a><hr>
 
 <h3>Solution</h3>
 First of all, I had a look at the code included with the challenge which was <a href='https://github.com/TheFakeS1imShady/CTF-Writeups/blob/master/CSICTF-2020/Machine%20Fix/code.py'>code.py</a>.<br>
 <code>
	
```python
 def convert (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

count=0
n=1
while(n<=523693181734689806809285195318):
	str1=convert(n)
	str2=convert(n-1)
	str2='0'*(len(str1)-len(str2))+str2
	for i in range(len(str1)):
		if(str1[i]!=str2[i]):
			count+=1
	n+=1

print(count)
```
 </code><br>
 
 
