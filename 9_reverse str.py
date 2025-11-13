# Everyone loves data science
# output--- enoyrevE sevol atad ecneics

A= input().split()     #split() → breaks a string into a list of words.
#A=A[::-1]
rev=[]
for i in A:
    rev.append(i[::-1])
A=' '.join(rev)   # .join is use to joins list of words back into a string, adding spaces between them.
print(A)
