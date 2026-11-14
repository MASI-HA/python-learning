a = 10
b = a
print("آدرس a:", id(a))
print(" آدرس b:", id(b))
a = 20
print("بعد از تغییر a:")
print("a =", a, "| b =", b)

x = [1, 2, 3]
y = x
print("\nآدرس x:", id(x))
print("آدرس y :", id(y))
x.append(4)
print("بعد از append:")
print("x =", x, "| y =", y)

print("id(a) بعد:", id(a))
print("id(b) بعد:", id(b))
