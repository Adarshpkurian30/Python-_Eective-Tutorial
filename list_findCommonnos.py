e = list(map(int,input("Enter numbers in list 1 :").split()))
f = list(map(int,input("Enter numbers in list 2 :").split()))
print("List 1 : ",e)
print("List 2 : ",f)
g = [num for num in e if num in f]
print("Common numbers : ",g)
