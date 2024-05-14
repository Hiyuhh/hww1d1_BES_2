import sys
import time
import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)

#------------------------------------------------------------#

line_break()
print("Advanced Operations on Python Lists")
line_break()

# Task 1

def squares_list(n):
    return [i ** 2 for i in range(1, n + 1)]

size = sys.getsizeof(squares_list(2))

print("Memory taken:", size)
print(squares_list(2))

# Task 2

def reverse_sublist(lst, i, j):
    lst[i:j+1] = reversed(lst[i:j+1])
    return lst

end_time = time.time()

print("Time taken:", end_time)
print(reverse_sublist([1, 2, 3, 4, 5], 1, 5))

# Task 3

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

print(merge_sorted_lists([10, 9, 5], [2, 3, 6]))


line_break()
print("Dictionary Manipulation and Optimization")
line_break()

# Task 1

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2} 

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

print(merge_dicts(dict1, dict2))

# Task 2

def intersection_dicts(dict1, dict2):
    intersection_dict = {}

    for key in dict1:
        if key in dict2:
            intersection_dict[key] = dict2[key]
    return intersection_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}

print(intersection_dicts(dict1, dict2))

# Task 3

def count_words(lst):
    word_freq = {}
    for word in lst:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

print(count_words(lst))