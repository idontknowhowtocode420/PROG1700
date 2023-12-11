
#strings
str1 = "hello,"
str2 = "world"
result_str = str1 + str2
print(result_str)
 
#substring
sentence = "this is a sentance for prog1700."
substring = sentence[:5]
print(substring)
 
#format
name = "joe"
age = 30
formatted_string = "my name is {} and I am {} years old".format(name, age)
print(formatted_string)
 
#loops
for num in range(1, 11):
    print(num)
 
#factor
def calculate_factor(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
 
# Example usage:
factorial_result = calculate_factor(5)
print("Factorial of 5:", factorial_result)
 
#sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
 
intersection_set = set1.intersection(set2)
union_set = set1.union(set2)
difference_set = set1.difference(set2)
 
print("Intersection:", intersection_set)
print("Union:", union_set)
print("Difference:", difference_set)
 
#lists
number_list = [1, 2, 3, 4, 5]
 
#sum
sum_result = sum(number_list)
print("Sum:", sum_result)
 
#avg overall
average_result = sum_result / len(number_list)
print("Average:", average_result)
 
#max val
max_value = max(number_list)
print("Maximum:", max_value)
 
#min val
min_value = min(number_list)
print("Minimum:", min_value)