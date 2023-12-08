# Opening a file in read mode
file_path = "file_handling/example.txt"
file = open(file_path, "r")

#Reading a file
content=file.read() # read() method reads entire contents of file
print(content)
# closing the file
file.close()

file1 = open(file_path, "r")
single_line=file1.readline() # readline() method reads a single line from the file
print(single_line) 
file1.close() 

file2 = open(file_path, "r")
lines=file2.readlines() # readlines() method reads all lines of file and returns a list
print(lines)
file2.close()



#opening a file in write mode

new_file="file_handling/newfile.txt"
file3=open(new_file,"w")

file3.close()

# Using 'with' statement

# The 'with' statement ensures that the file is properly closed after its suite finishes.
# The 'with' statement ensures proper cleanup even if an exception is raised within the block.

with open("file_handling/example.txt","r") as fl:
    content=fl.read()
    print("using with:\n"+content)


# Iterating Over Lines:

with open("file_handling/example.txt","r") as file:
    for line in file:
        print(line.strip())  # Strip newline characters

print()

# seek() method is used to change the file cursor position

file = open("file_handling/example.txt","r")
file.seek(5)  # Move to the beginning of the file
content = file.read()
print(content)
file.close()

