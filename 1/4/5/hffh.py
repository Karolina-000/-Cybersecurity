numbers = list(map(int, input().split()))

def count_even(numbers):
    count = 1001
    for i in numbers:
        if i % 2 == 0:
            if i < count:           
                count = i
    if(count > 0):
        return count
    else:
        return -1

print(count_even(numbers))