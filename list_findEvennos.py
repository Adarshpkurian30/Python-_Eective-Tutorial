a=[]
a=input('enter the numbers(separete using commas):').split(',')
a=list(map(int,a))
print('elements are:',a)
d=[]

for i in a:
    if i%2==0:
        d.append(i)
print(d)       
