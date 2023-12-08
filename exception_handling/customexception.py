# custom exception

#custom exception class
class NegativeValueError(Exception):
    def __init__(self,val):
        self.val = val
        message=f"Negative values are not allowed but received: {val}"
        super().__init__(message)


def validate(val):
    if val<0:
        raise NegativeValueError(val)
    return f"value {val} is valid"

try:
    num=int(input("Enter a non negative value: "))
    res=validate(num)
    print(res)
except NegativeValueError as e:
    print(f"Caught a custom exception: {e}")