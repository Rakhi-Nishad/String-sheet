#  A="aabbcc"
#  B=98
#  Output:
#  2

A=input()
B=98
count=0
# print(B)
for i in range(len(A)):
      if ord(A[i])==B:
            count+=1
print(count)