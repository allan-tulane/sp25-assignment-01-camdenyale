"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    max_length = 0
    cur_length = 0
    for num in array:
        if num == key:
            cur_length += 1
            max_length = max(max_length, cur_length)
        else:
            cur_length = 0
    return max_length

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    return _longest_run_recursive(mylist, key).longest_size

def _longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    mid = len(mylist) // 2
    result_left = _longest_run_recursive(mylist[:mid], key)
    result_right = _longest_run_recursive(mylist[mid:], key)
    return combine_results(result_left, result_right)

def combine_results(result1, result2):
    if result1.is_entire_range and result2.is_entire_range:
        total = result1.longeset_size + result2.longeset_size
        return Result(total, total, total, True)

    left_size = result1.left_size
    if result1.is_entire_range:
        left_size += result2.left_size
    
    right_size = result1.right_size
    if result2.is_entire_range:
        right_size += result2.right_size

    overlap = result1.right_size + result2.left_size
    longest_run = max(overlap, result1.longest_size, result2.longest_size)
    return Result(left_size, right_size, longest_run, False)
    


