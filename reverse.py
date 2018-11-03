print("reversing a string")
i=0
revstr=""
n = input("enter word")
while (i<(len(n))):
    m= (n[-1:])
    revstr=(revstr+m)
    n=n[0:(len(n)-1)]
i+=i
print("reverse:" ,revstr)
