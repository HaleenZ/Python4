n = int(input("Enter a positive integer value for n: "))

sum_of_positive_integers = 0
x = 0

while n - x > 0:
    sum_of_positive_integers += n - x
    x += 2

print("Sum of positive integers:", sum_of_positive_integers)
