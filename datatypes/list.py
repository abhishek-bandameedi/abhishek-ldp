# list is an ordered collection of items and it is mutable and allows duplicate values

lst=["table","chair","laptop"]
print(lst)

print(len(lst))

new=list(("hello","world"))
print(new)

# List methods

nums=[1,2,3]

nums.append(4)
print("after appending",nums)

nums2=[5,6]
nums.extend(nums2)
print("after extending",nums)

print(nums[1:])
print(nums[:3])
print(nums[3:6])

nums.insert(1,"hello")
print("inserting value at index 1",nums)

nums.remove("hello")
print("removing first occurance of value",nums)

nums.pop(0)
print("removing item at specified index",nums)

nums.reverse()
print("reverse a list",nums)

nums.sort()
print("sort the list",nums)

squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)

result = [x**2 if x % 2 == 0 else x**3 for x in range(10)]
print(result)

nums.clear()
print("remove all items",nums)

