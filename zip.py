mylist1=[1,2,3,4,5]
mylist2=['a','b','c','d','e',]

x=list(zip(mylist1,mylist2))
print(x)

for item1,item2 in zip(mylist1,mylist2):
    print('for this tuple, first item is {} and second item is {}'.format(item1,item2))