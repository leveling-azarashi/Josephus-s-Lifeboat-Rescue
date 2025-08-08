import math

def last_survivor(n):
    # Find the largest power of 2 less than or equal to n
    power = 2 ** (n.bit_length() - 1)
    # Apply the Josephus formula
    return 2 * (n - power) + 1

# Example usage
n = int(input("Enter number of people: "))
print(f"The last person standing is: {last_survivor(n)}")
