text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# テキストから単語の文字数を取得してリスト化
word_lengths = list(map(len, text.split()))

# リストの要素を文字列に結合
result = ''.join(map(str, word_lengths))

print(result)

# 以下をTERMINALに入力し確認
# C:/Users/kent2/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/python.exe c:/Users/kent2/OneDrive/デスクトップ/PG/BasicPython/pi.py
