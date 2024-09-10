"""
a = (22,33,43,55,70)

#printing each number in the list on a new line 
for number in a:
    print(number)
#add numbers in list 
sum = 0
for number in a:
    sum = sum + number
    print(f"The sum in the middle of the processing is: {sum}")
print(sum)

#only return the odd numbers in my list
print("Only the odd numbers")
odd_numbers = []
for number in a:
    if number %2 ==1:
        print(f"I found an odd number! which is {number}")
        odd_numbers.append(number)
        print(f"Odd numbers is now: {odd_numbers}")
    print(odd_numbers)

# If I want to check if a number of any other value is in a list; I can use the keyword 'in'
print("Example of using in to determine if something is a number of a datastructure")
value = 2
print(f"Is my value: {value} in my list {a}: {value in a}")
value = 55
print(f"Is my value: {value} in my list {a}: {value in a}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x**2 for x in numbers[3:8:2]]
print(result)

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers if x % 2 == 0]
print(squared)

def find_divisible_comprehension(arbitrary_start: int, arbitrary_end: int, n: int) -> list[int]:
    return [num for num in range(arbitrary_start, arbitrary_end + 1) if num % n == 0]

print(find_divisible_comprehension(1, 10, 3))

p = [5, 6, 7, 8, 9]
print(p)
j = p[::2]
print(j)
u = p[::-3]
print(u)

#homework1 answers:
#1
count = 0
vowels = "aeiouAEIOU"
for character in s:
    if character in vowels:
        count += 1
    return count

#2

if len(list) ==0:
        return list2
if len(list2) ==0:
        return list1

li = [...]
lj = [...]
li = [1, 6, 9, 12]
lj = [0, 2, 3, 8, 15]
lk = [0, 1, 2, 3, 6, 8, 9, 12, 15]

for every value in li:
    li[n] >= li[n-1]


c = 0

def f(x):
    for i in x:
        if i > 0:
            c -= 2
        elif i == 0:
            c +=1
    else:
            c *= 2
    print(c)
    return c 

#3
lengths = []
for word in words:
    lengths.append(len(word))
return lengths

#4

#5
inter_list = []
for i in list1"
     listif i in list2"listinter+list.append(i)
return inter_list
"""
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    vowel_count: int = 0
    for letter in str:
        if letter in vowels:
            vowel_count += 1
    return vowel_count  

def word_lengths(words: list) -> list:
    word_lengths = []
    for word in words:
        word_lengths.appen(len(word))
    return word_lengths

def reverse_string(s: str) -> str:
    reverse_string.reverse()
    print(reverse_string)
