print('1st program')
a=[]
a=input('enter the numbers(separete using commas):').split(',')
a=list(map(int,a))
print('elements are:',a)
temp=int(input('enter the max limit no:'))
c=[]
i=0
b=sorted(a,reverse=False)
while(b[i]<=temp):
    c.append(b[i])
    i+=1
print(c)    
