def calculate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum

numbers = [5, 10, 15, 20, 25]
total, avg, max_value, min_value = calculate_stats(numbers)

print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")