
n=int(input())
k={}
for i in range(n):
    a=input().split(' ')
    k[a[0]]=a[1]

while True:
    try:
        a=input()
        if(a in k.keys()):
            print('{0}={1}'.format(a,k[a]))
        else:
            print('Not found')
    except:
            break
