# Challenge 1
def sum_to(n):
    sum = 0
    for num in range (1, n):
        sum = sum + num
            
    return n + sum

# print(sum_to(8))

# Challenge 2
def largest(num_list):
    return max(num_list)

# print(largest([1, 2, 3, 45, 5, 6, 7]))

# Challenge 3
def occurances(items, occur):
    return items.count(occur)

print(occurances('cat, dog, goat, pig, bird, bat', 'a'))

# Challange 4
def product(*args):
    multiply = 1
    for num in args:
        multiply *= num
    return multiply

print(product(5, 6, 2, 4))