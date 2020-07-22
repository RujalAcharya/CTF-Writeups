# Machine Fix
<h3>Description</h3>
 We ran a code on a machine a few years ago. It is still running however we forgot what it was meant for. It completed n=523693181734689806809285195318 iterations of the loop and broke down. We want the answer but cannot wait a few more years. Find the answer after n iterations to get the flag.<br>
 The flag would be of the format <code> csictf{answer_you_get_from_above} </code>.
 
 
 <strong> File Included: </strong> <a href='https://github.com/TheFakeS1imShady/CTF-Writeups/blob/master/CSICTF-2020/Machine%20Fix/code.py'>code.py</a><hr>
 
 <h3>Solution</h3>
 First of all, I had a look at the code included with the challenge which was <a href='https://github.com/TheFakeS1imShady/CTF-Writeups/blob/master/CSICTF-2020/Machine%20Fix/code.py'>code.py</a>.
	
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
 When I looked at the code, my first instinct was to try running the code.So as a gentleman, I ran the code, which took forever to give output. Later on, I realized that the problem was to optimize the code so that we could get the output quickly. I felt dumb.<br>
 
 When I scanned through the code, I realized that the main reason the code takes forever to run is the value of n in the while loop. So, i modified the code a little bit as <a href='https://github.com/TheFakeS1imShady/CTF-Writeups/blob/master/CSICTF-2020/Machine%20Fix/pattern.py'>pattern.py</a> so that I could look at the output of the program in the desired range of value of n. Then, I ran the code so that I could get the output for the range 0-100.
 
 <code>[0, 1, 2, 4, 5, 6, 8, 9, 10, 13, 14, 15, 17, 18, 19, 21, 22, 23, 26, 27, 28, 30, 31, 32, 34, 35, 36, 40, 41, 42, 44, 45, 46, 48, 49, 50, 53, 54, 55, 57, 58, 59, 61, 62, 63, 66, 67, 68, 70, 71, 72, 74, 75, 76, 80, 81, 82, 84, 85, 86, 88, 89, 90, 93, 94, 95, 97, 98, 99, 101, 102, 103, 106, 107, 108, 110, 111, 112, 114, 115, 116, 121, 122, 123, 125, 126, 127, 129, 130, 131, 134, 135, 136, 138, 139, 140, 142, 143, 144, 147]</code>
 
 
