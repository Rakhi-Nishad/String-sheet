A=input()
B="bob"   ##"aabababaa"
occur=A.find(B)
print(occur)

# ------- ans == 1(abobc)


# --------------------------------------
C=input()
D="bob"   ##"aabobobaa"
count=0
for i in range(len(C)-2):
    if A[i:i+3]=="bob":
        count+=1
print(count)  ### answer is 2 (bobob)