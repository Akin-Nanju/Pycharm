# # student = {"name": "Anjali", "age": 19, "grade": "A"}
# # Write code to print the student’s grade only if it exists. If not, print "No grade found"
#
# def check():
#     student = {"name": "Anjali", "age": 19, "grade": "A"}
#     if "grade" in student:
#      print(student.get("grade"))
#     else:
#         print("no grade")
#
# check()

# You’ve probably heard of FizzBuzz, but we’re doing it my way 😈
#
# Problem:
# Print numbers from 1 to 50, but:
#
# If the number is divisible by 3, print "Fizz" instead.
#
# If it’s divisible by 5, print "Buzz" instead.
#
# If it’s divisible by both 3 and 5, print "FizzBuzz" instead.
#
# If it’s not divisible by 3 or 5, just print the number.

# def check_fizz():
#     for i in range(1, 51):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#
# check_fizz()

# def second_largest(a):
#     if len(set(a)) < 2:
#         print("No second largest number found")
#         return
#     largest = second = float('-inf')
#     for i in range(len(a)):
#         if largest < a[i]:
#             second = largest
#             largest = a[i]
#         elif second < a[i] and largest != a[i]:
#             second = a[i]
#     print(second)
# a = [5,5,5,5,5]
# second_largest(a)

# a = "Hello, World!"
# char_count = {}
#
# for i in a.lower():
#     if i.isalpha():
#         if i in char_count:
#             char_count[i] += 1
#         else:
#             char_count[i] = 1
#
# print(char_count)


# def odd(a):
#     count = 0
#     for i in a:
#         if i % 2 !=0:
#             count += 1
#     print(count)
#
# lis = [1,2,3,4,5,6,7,8,9]
# odd(lis)


# def check(a):
#     initial = a.lower().strip().replace(' ','')
#     rev = ''
#     for char in a.lower().strip().replace(' ',''):
#         rev = char + rev
#     print(rev)
#     if rev == initial:
#         print("Yes, it's a palindrome")
#     else:
#         print("No, it's not a palindrome")
#
# A = "A  ki  n"
# check(A)


# def even(a):
#     out = []
#     if len(a) < 2:
#         print("List should have at least two elements")
#         return
#     for i in range(0, len(a)):
#         if a[i] % 2 == 0:
#             out.append(a[i])
#
#     return out
#
# lis = [1,2,3,4,5,6,7,8,9]
# print(even(lis))



# def transform(string):
#     string = string.split(",")
#     result = {}
#     for part in string:
#         key,value = part.split(":")
#         result[key.strip()] = value.strip()
#
#     print(result)
#     print(string)
#
# a = "UserID:123, Name:John Doe, Country:Nepal"
# transform(a)




def avg(data):
    sum = 0
    for name in data:
        sum += name.get("age")
    return avg

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
    ]
print(avg(data))


