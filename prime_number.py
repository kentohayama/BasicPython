numbers = [61, 10]

for number in numbers:
    if number <= 1 or not isinstance(number, int):
        print("自然数を入力し直してください。")
    else:
        divisor = 2
        prime = True

        while divisor < number:
            if number % divisor == 0:
                prime = False
                break
            divisor += 1

        if prime:
            print(f"{number}は素数です。")
        else:
            print(f"{number}は素数ではありません。")
