n = int(input())
s = input()

r = 31
M = 1234567891

result = 0
power = 1

for i in range(n):
    value = ord(s[i]) - ord('a') + 1
    result = (result + value * power) % M
    power = (power * r) % M

print(result)