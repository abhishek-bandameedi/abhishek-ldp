# The write() method is used to write content to a file. It overwrites existing content.

file=open( "file_handling/newfile.txt","w")
file.write("this is a new file")
file.close()

# The append() method is used to add content to the end of an existing file.

file2=open( "file_handling/newfile.txt","a")
file2.write("\nThis content is appended")
file2.close()

# using 'with' statement

with open( "file_handling/newfile.txt","a") as file:
    file.write("\nhello using with keyword")

# writelines() writes a list of strings to file

with open('file_handling/sample.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.writelines(['Line 1\n', 'Line 2\n'])
