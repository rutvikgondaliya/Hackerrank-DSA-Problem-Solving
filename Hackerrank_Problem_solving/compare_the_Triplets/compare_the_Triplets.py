a = list(map(int,input().split()))
b = list(map(int,input().split()))
a1 = 0
b1 = 0
for i in range(len(a)):
    if a[i] > b[i] :
        a1 +=1
    elif a[i] < b[i] :
        b1 += 1
print(a1 ,b1)
