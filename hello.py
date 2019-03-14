# 文字列を出力する
string = 'Hello'
print(string + ' ' + 'World!')

# 文字列配列を「,」で連結する
strings = ['Apple', 'Google']
print(','.join(strings))

# n回繰り返し出力する
print('abc' * 3)

# format
print('%s is %d.' % ('Age', 26))
print('{0}_{1}'.format('hello', 'python'))

# forループで文字を取り出す
for c in 'yuoku':
    print(c)

# forループで文字を取り出す(Indexあり)
theMessage = 'message'
for index in range(len(theMessage)):
    c = theMessage[index]
    print('[{0}]{1}'.format(index, c))

# 演算
num = 10
print('num = {0}'.format(num))

print('num + 1 = {0}'.format(num + 1))
print('num - 1 = {0}'.format(num - 1))
print('num * 2 = {0}'.format(num * 2))
print('num / 2 = {0}'.format(num / 2))
print('num % 3 = {0}'.format(num % 3))
print('num ** 3 = {0}'.format(num ** 3))

decimal = 12.3
print('decimal = {0}'.format(decimal))
print('decimal / 2 = {0}'.format(decimal / 2))
print('decimal // 2 = {0}'.format(decimal // 2))

# 条件演算
result = 'true' if decimal == 12.3 else 'false'
print(result)
result = 'true' if decimal == 12.0 else 'false'
print(result)

result = 'true' if num == 10 and decimal == 12.3 else 'false'
print(result)

result = 'true' if num == 0 or decimal == 12.3 else 'false'
print(result)