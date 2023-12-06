# Dictionaries are used to store data values in key:value pairs.

sample={
    "name":"abhi",
    "age":22,
    "lang":"python"
}

print(sample)

print(sample["name"])

print(len(sample))

new=dict(name="python",type="dynamic")
print(new)

#dict methods

print(sample.keys())
print(sample.values())
print(sample.items())

print(sample.get("age"))
print(sample.get("age1",0)) # gives value for key if it exists else returns default value

sample.pop("age")
print(sample)

sample["age"]=22 #add a key value
print(sample)

squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(squares_dict) 

result_dict = {x: x**2 if x % 2 == 0 else x**3 for x in range(10)}
print(result_dict)