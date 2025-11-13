T=int(input())    # abcba axax abba output[1 0 1]
for i in range(T):
    s=input()
    list=[]
    for j in s:
        list.append(j)
    rev=[]  
    if s==list:
        print("1")
    else:
        print("0")