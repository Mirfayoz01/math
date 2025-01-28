def recursive_square(x, n):
    if n == 0:
        return x
    else:
        return recursive_square(x ** 2, n - 1)

# Test qilish
x = 2
n = 64
natija = recursive_square(x, n)
print(f"{x} ni {n} marta kvadratiga oshirish natijasi: {natija}")
