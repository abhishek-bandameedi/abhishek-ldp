import re

'''
Metacharacters:

.: Matches any character except a newline.
^: Anchors the match at the start of the string.
$: Anchors the match at the end of the string.
*: Matches 0 or more occurrences of the preceding character.
+: Matches 1 or more occurrences of the preceding character.
?: Matches 0 or 1 occurrence of the preceding character.
[]: Specifies a character class.
|: Acts like a logical OR.

'''

# search(pattern,string): Searches for the first occurrence of the pattern in the string.

pattern="^The.*Spain$"
text="The rain in Spain"
x=re.search(pattern,text)
print(x)
print(x.start())

# findall() returns list containing all matches

x= re.findall("ai",text)
print(x)

# split() returns a list where the string has been split at each match

x = re.split("\s", text)
print(x)

# sub() replaces the matches with the text of your choice

x = re.sub("\s", "9", text)
print(x)

y = re.sub("\s", "9", text, 2) # controll no of replacements by specifying count
print(y)

