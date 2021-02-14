# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
for i in range(a):
    k=input()
    m=k[::2]
    s=k[1::2]
    print("{0} {1}".format(m,s))

