list1=[1,2,3,4,7,8,9,10,11,12,13,14,15]
# for num in list1:
    # print(num)

# print only even number
for num in list1:
    if num % 2 == 0:
        print(num)

    else:
        print('odd number')


#  sum of all
sum = 0
for num in list1:
    sum=sum+num
print('the total sum is %d'%sum)


# string
for letters in 'this is a dursikshya':
  print(letters)


# tuple
mytuple=("apple","mango","banana","orange")
for frut in mytuple:
    print(frut)