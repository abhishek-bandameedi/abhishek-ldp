
from packages import module1

# from packages import *
from packages import module2 as m2


msg=module1.greet("abhi")
print(msg)

res=module1.name+" is "+module1.type
print(res)

# print(dir(module1))

print(m2.welcome())
# print(module2.welcome())