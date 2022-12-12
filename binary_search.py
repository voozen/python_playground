from random import randint

def binary_search(array, value):
    low = 0
    high = len(array) - 1
    while (low <= high):
        mid = int((high + low) / 2)
        guess = array[mid]
        if guess == value:
            return mid
        if guess > value:
            high = mid - 1
        else:
            low = mid + 1
    return None

array = [randint(1, 10) for _ in range(100)]
print(array)
random_value = randint(1, 10)
print('Random value sought: ' + str(random_value))
print('First found index of searched value: ' + str(binary_search(array, random_value)))
