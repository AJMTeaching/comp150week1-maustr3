# ------------------------------------------------------------------------

# Lab 1
# Problem 1
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
# 1. Create a list called my_list with the values [1, 5, 'apple', 20.5].

my_list = [1, 5, 'apple', 20.5]
print(my_list)

# 2. Using indexing, print the value 'apple' from my_list.

if 'apple' in my_list:
    print("'apple'")
#better answer: print(my_list[2])

# 3. Add the value 10 to the end of my_list using the append() method. Print the updated list.

my_list.append(10)
print(my_list)

# 4. Remove the value 20.5 from my_list using the remove() method. Print the updated list.

my_list.remove(20.5)
print(my_list)

# 5. Reverse the order of the elements in my_list using a method. Print the reversed list.

my_list.reverse()
print(my_list)
#better answer: my_list_reversed = [::-1]

# Problem 2
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
# 1. Create a dictionary called person with keys 'name', 'age', 'job' and values 'John', 30, 'teacher'.

my_dict =dict(name='John', age=30, job='teacher')
print(my_dict)

# 2. Print the value corresponding to the 'job' key.

print(my_dict['job'])

# 3. Add a new key-value pair: 'city': 'Paris' to the person dictionary. Print the updated dictionary.

my_dict['city'] = 'Paris'
print(my_dict)
#alt answer: my_dict.update(city='Paris')
#alt answer: my_dict |= {'city': 'Paris'}

# 4. Remove the 'age' key-value pair from person. Print the updated dictionary.

del my_dict['age']
print(my_dict)
#alt answer: my_dict.pop('age')

# 5. Iterate through the person dictionary and print out each key-value pair on a separate line.

for key, value in my_dict.items():
    print(key, ":", value)
#alt answer: for key in my_dict.keys():
#print(f"Key: {key}, Value: {person[key]})

# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    # TODO: Implement this function
    # Step 1: What is it asking? 
    # This question is asking me to write a function
    # we're getting a parameter called 's' and we need to figure out how many vowels
    # then we need to return the count at the ned
    # Step 2: Pseudocode
    # step 1: iterate over input string
    # step 2: use for loop to check each letter 
    # step 3: check to see if letter is vowel or not 
    # step 4: if letter is vowel, then keep track of it 
    # step 5: return the result of that process of keeping track  
    
    #vowels: list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels = "aeiouAEIOU"
    vowel_count: int = 0
    for letter in str:
        if letter in vowels:
            vowel_count += 1
    return vowel_count      

# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
    # TODO: Implement this function
    merge_lists = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_lists.append(list1[i])
            i += 1
        else:
            merge_lists.append(list2[j])
            j += 1
    merge_lists.extend(list1[i:])
    merge_lists.extend(list2[j:])

    return merge_lists
print(merge_lists)


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    - words (list): The list of words

    Returns:
    - list: A list containing the lengths of the words
    """
    # TODO: Implement this function
    word_lengths = []
    for word in words:
        word_lengths.appen(len(word))
    return word_lengths


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
    # TODO: Implement this function
    reverse_string.reverse()
    print(reverse_string)


# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """
    # TODO: Implement this function
    set(list1).intersection(list2)
    


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
