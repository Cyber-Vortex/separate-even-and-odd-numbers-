# Program to separate even and odd numbers into different lists
numbers = [12, 7, 9, 24, 33, 46, 55, 88]
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)   # Add to even list
    else:
        odd_numbers.append(num)    # Add to odd list

print("Original List:", numbers)
print("Even Numbers List:", even_numbers)
print("Odd Numbers List:", odd_numbers)
