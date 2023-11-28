
# ユークリッドの互除法を用いて最大公約数を求める関数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 組み合わせ
pairs = [(10, 20), (91, 14), (14, 91)]

# 各組み合わせに対して最大公約数を求める
for pair in pairs:
    result = gcd(pair[0], pair[1])
    print(f"{pair}: {result}")
