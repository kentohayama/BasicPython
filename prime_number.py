# 61が素数でないことを確認
# 10が素数であることを確認

numbers = [61, 10]

for number in numbers:
    divisor = 2
    prime = True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1

    if prime:
        print(f"{number}は素数ではありません。")
    else:
        print(f"{number}は素数です。")