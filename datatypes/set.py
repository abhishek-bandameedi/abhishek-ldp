# A set is a collection which is unordered, unindexed and unique items.

# Once a set is created, you cannot change its items, but you can remove items and add new items.

sample={"a","b","c"}
print(sample)
sample2={"a","b","c","a"}
print(sample2)

print(len(sample))

new=set(("hello","world"))
print(new)


#set methods

s={1,2,3}

s.add(4)
print(s)

s.remove(4)
print(s)

# s.remove(4)
s.discard(4) #Removes the specified element from the set if it is present. Does not raise an error if the element is not found.
print(s)

s.clear() 
print(s)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))