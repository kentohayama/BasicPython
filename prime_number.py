
numbers = [61, 10, 2, 5]

for number in numbers:
    if not isinstance(number, int) or number <= 1:
        print("2以上の自然数を入力してください")
    elif number == 2:
        print(f"{number}は素数です")
    else:
        divisor = 2
        is_prime = True

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            print(f"{number}は素数です")
        else:
            print(f"{number}は素数ではありません")