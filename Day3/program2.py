from itertools import permutations
x=input("Enter a string : ")
perms = [''.join(p) for p in permutations(x)] 
print(perms)
