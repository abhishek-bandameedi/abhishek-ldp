str1="hello"
print(str1)

str2="""
This is a
multiline string
"""
print(str2)

#Accessing the string

word="Strings"
print(len(word))

print(word[0],word[1],word[2],word[3])

print(word[1:4])
print(word[1:])
print(word[:3])

print("negatice indexing ",word[-5:-3])

#Modifying the strings

print(word.upper())
print(word.lower())
print(word.replace("S","P"))

greetings="welcome to python"
print(greetings.split("o"))

#String formatting

name="abhi"
age=22
language="python"
txt="{} is {} years old learning {}"

print(txt.format(name,age,language))