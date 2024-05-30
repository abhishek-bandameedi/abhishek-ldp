# Some objects, like file handles, sockets, or database connections, cannot be pickled. 
# You can handle such cases using the pickle.PicklingError exception.

import pickle

class UnpicklableObject:
    def __reduce__(self):
        raise pickle.PicklingError("Cannot pickle UnpicklableObject")

obj = UnpicklableObject()

with open('pickle/unpicklable_object.pickle', 'wb') as file:
    try:
        pickle.dump(obj, file)
    except pickle.PicklingError as e:
        print(f"PicklingError: {e}")
