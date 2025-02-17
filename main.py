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
    if not mylist:
        return Result (0, 0, 0, False)
    if len(mylist) == 1:
        count = 1 if mylist[0] == key else 0
        return Result(count, count, count, count == 1)
    mid = len(mylist) // 2
    result_left = longest_run_recursive(mylist[:mid], key)
    result_right = longest_run_recursive(mylist[mid:], key)


    left_size = result_left.left_size
    if result_left.is_entire_range:
        left_size += result_right.left_size
    
    right_size = result_right.right_size
    if result_right.is_entire_range:
        right_size += result_left.right_size

    combined = left_result.right_size + result_right.left_size if mylist[mid-1] == key and mylist[mid] == key else 0
    longest_run = max(result_left.longest_size, result_right.longest_size, combined)

    is_entire_range = result_left.is_entire_range and right_result.is_entire_range
    return Result(left_size, right_size, longest_run, is_entire_range)
    


