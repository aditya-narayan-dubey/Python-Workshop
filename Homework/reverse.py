```python
num = int(input("Enter a three-digit number: "))

rev = 0

rev = rev * 10 + num % 10
num = num // 10

rev = rev * 10 + num % 10
num = num // 10

rev = rev * 10 + num % 10

print("Reversed number =", rev)
```