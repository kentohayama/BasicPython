def is_prime(number):
    if number <= 1 or not isinstance(number, int):
        return False

    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

numbers = [61, 10]

for number in numbers:
    if is_prime(number):
        print(f"{number}は素数です。")
    else:
        print(f"{number}は素数ではありません。")
