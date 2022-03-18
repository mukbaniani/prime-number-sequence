```python
from simple_number import SimpleNumberList

s = SimpleNumberList(5)
print(s)
# SimpleNumberList(2, 3, 5)

print(5 in s)
# True

print(6 in s)
# False

print(len(s))
# 3

print(s * 2)
# SimpleNumberList(2, 3, 5, 2, 3, 5)

print(2 * s)
# SimpleNumberList(2, 3, 5, 2, 3, 5)

print(s + [1, 2, 3, 4, 5])
# SimpleNumberList(2, 3, 5, 2, 3, 5)

print([1, 2, 3, 4, 5] + s)
# SimpleNumberList(2, 3, 5, 2, 3, 5)

print(s[0])
#2

for num in s:
    print(s)
    # 2
    # 3
    # 5

del s[0]
print(s)
# SimpleNumberList(3, 5)

s[0] = 5
print(s)
# SimpleNumberList(2, 3, 5, 3, 5)
s[0:0] = 19
print(s)
# SimpleNumberList(2, 3, 5, 7, 11, 13, 17, 19, 2, 3, 5, 2, 3, 5)

s[0:3] = 3
# SimpleNumberList(2, 3, 7, 11, 13, 17, 19, 2, 3, 5, 2, 3, 5)

s.append(5)
# append all prime number from 1 to 5

s.pop()
# default remove last item index is optional

s.add_prime(num=5)
# append prime number num must be prime else raise TypeError

s.add_prime_by_index(number=5, index=5)
# append prime number by index number must be prime else raise TypeError

```