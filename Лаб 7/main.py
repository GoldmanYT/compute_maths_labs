def f(x):
    return x ** 2


def rect_int(func, a, b, n=1000):
    h = (b - a) / n
    ans = 0
    for i in range(n):
        x1 = a + h * i
        x2 = a + h * (i + 1)
        c = (x1 + x2) / 2
        ans += func(c) * h
    return ans


def simpson_int(func, a, b, n=1000):
    n += n % 2
    h = (b - a) / n
    y = [f(a + i * h) for i in range(n + 1)]
    m = n // 2
    ans = (y[0] + y[2 * m] + 4 * y[1]) * h / 3
    for i in range(2, m + 1):
        ans += (4 * y[2 * i - 1] + 2 * y[2 * i - 2]) * h / 3
    return ans


print(rect_int(f, 1, 2))
print(simpson_int(f, 1, 2))
