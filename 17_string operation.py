# A="aeiOUz"
#  Output:
#  "###z###z"

A = "aeiOUz"
A = A + A
A = ''.join(ch for ch in A if not ch.isupper())

vowels = 'aeiou'
result = ''
for ch in A:
    if ch in vowels:
        result += '#'
    else:
        result += ch

print(result)
