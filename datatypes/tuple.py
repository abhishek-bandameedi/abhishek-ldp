# tuples are similar to list but immutable

tpl=("a","b","c")
print(tpl)

print(len(tpl))

single=("unique",)
print(single)

new=tuple(("hello","world"))
print(new)

#tuple methods 

sample=(1,2,3,2)

print(sample.count(2))
print(sample.index(2))

# to work with tuples we need to convert them to lists

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)