#write a function to count the number of negative and positive numbers in a list 
#logic use a loop to iterate through the list and keep two counters 
#time complexity of linear search O(N)
#Space complexity O(1)
def count_positive_negative(numbers):
    positive_count = 0
    negative_count = 0

    for num in numbers:
        if num >= 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    return positive_count, negative_count


numbers = [5, -2, 0, 8, -7, 3, -1]

positive, negative = count_positive_negative(numbers)

print("Positive numbers:", positive)  # 3
print("Negative numbers:", negative)  # 3