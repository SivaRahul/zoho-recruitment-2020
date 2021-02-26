s=input("Enter a String: ")
t=''
n=len(s)
mid=n//2
p=n
t=s[mid:n]+s[0:mid]
for i in range(0,n):
    print((n-i-1)*' '+t[0:i+1])
