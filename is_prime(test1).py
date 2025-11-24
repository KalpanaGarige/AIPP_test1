#write python code to check a given number is prime or not nsure to include edge cases
def is_prime(n):    
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

test_cases = {
    0: False,
    1: False,
    2: True,
    3: True,
    4: False,
    6: False,
    9: False,
    5: True,
    7: True,
    11: True,
    13: True,
    97: True,
    7919: True,
    100: False,
    10000: False,
    -7: False,
    -1: False
}

print("Running Test Cases...\n")

for number, expected in test_cases.items():
    result = is_prime(number)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test n={number}: Expected={expected}  Got={result}  --> {status}")

print("\nAll test cases completed.\n")
19

user_value = input("Enter a number to check if it is prime: ")

# Validate user input
if not user_value.lstrip("-").isdigit():
    print("Invalid input! Please enter a valid integer.")
else:
    n = int(user_value)
    
    if is_prime(n):
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
