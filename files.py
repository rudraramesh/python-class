my_files=open('test.txt')
print(my_files)
print(my_files.read())
print(my_files.read())
my_files.seek(0)
print(my_files.read())


# readlines return a list of the lines in the file
my_files.seek(0)
print(my_files.readlines())

# #n -> next line
my_files.close()

# writing to a file
# open() -> opening the files
# passing w+ let us read and write to the file
# open('text.txt','w+') -> this will truncates the orginal, meaning the anything that was before in original file in deleted

my_files=open('test.txt','w+')
print(my_files)


my_files.write('this is a new text')
my_files.seek(0)
print(my_files.read())
my_files.write('\n this is a new line text')
my_files.seek(0)
print(my_files.read())
my_files.close()



# appending to the file 
newfile=open('hello.txt','a+')
print(newfile)
newfile.write('this is rudra ramesh file important')
newfile.write('\n this is new line for only redra')
newfile.seek(0)
print(newfile.read())