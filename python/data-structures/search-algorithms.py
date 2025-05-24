def constant_search(array, target):
    return target in array

def linear_search(array, target):
    for i in array:
        if i == target:
            return True
    return False

def quadratic_search(array, target):
    for i in array:
        for j in array:
            if i == target and j == target:
                return True
    return False

array = input("Enter the array of integers: ").split()
array = [int(num) for num in array]

target = int(input("Enter the target integer: "))

if len(array) <= 10 ** 5:
    print(constant_search(array, target))
    print(linear_search(array, target))
    print(quadratic_search(array, target))
else:
    print("Invalid array input.")