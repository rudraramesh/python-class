def square(num):
    return num**2

x=square(3)
print(x)



sqr=lambda num : num**2
y=sqr(5)
print(y)


my_nums=[0,1,2,3,4,5,6,7,8,9,10]

filter_data=list(filter(lambda num:num%2==0,my_nums))

print(filter_data)