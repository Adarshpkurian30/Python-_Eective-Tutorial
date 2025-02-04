a=[]
a=input('enter the numbers(separete using commas):').split(',')
a=list(map(int,a))
print('elements are:',a)
print(max(a),"is the largest number")
print(min(a),"is the smallest number")
