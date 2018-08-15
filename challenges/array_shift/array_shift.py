def insert_shift_array(arr, val):
    """This is my first docstring.
     This function is taking in an array and adding another argument to the middle of that array"""
    ind = len(arr) // 2 + len(arr) % 2
    return arr[:ind] + [val] + arr[ind:]
