from math import factorial as fact
from functools import reduce


def product(sequence):
    return reduce(lambda x, y: x * y, sequence, 1)


def n(
        x_: float,
        x: list[float],
        y: list[float]
) -> float:
    delta_y = [[y[i + 1] - y[i]] * (len(y) - i - 1)
               for i in range(len(y) - 1)]
    for j in range(1, len(y) - 1):
        for i in range(len(y) - j - 1):
            delta_y[i][j] = delta_y[i + 1][j - 1] - delta_y[i][j - 1]
    h = x[1] - x[0]
    index = 0
    for i in range(len(x) - 1):
        if x[i] <= x_ <= x[i + 1]:
            index = i
            break
    if index < len(x) // 2:
        # первая формула
        q = (x_ - x[index]) / h
        return y[index] + sum(
            product(
                q - j for j in range(i + 1)
            ) * delta_y[index][i] / fact(i + 1)
            for i in range(len(delta_y[index]))
        )
    else:
        # вторая формула
        index += 1
        q = (x_ - x[index]) / h
        return y[index] + sum(
            product(
                q + j for j in range(i + 1)
            ) * delta_y[index - i - 1][i] / fact(i + 1)
            for i in range(len(delta_y[len(y) - index - 1]))
        )


table = [
    (1.340, 4.25562),
    (1.345, 4.35325),
    (1.350, 4.45522),
    (1.355, 4.56184),
    (1.360, 4.67344),
    (1.365, 4.79038),
    (1.370, 4.91306),
    (1.375, 5.04192),
    (1.380, 5.17744),
    (1.385, 5.32016),
    (1.390, 5.47069),
    (1.395, 5.62968),
]
# table = [
#     (1.215, 0.106044),
#     (1.220, 0.113276),
#     (1.225, 0.119671),
#     (1.230, 0.125324),
#     (1.235, 0.130328),
#     (1.240, 0.134776),
#     (1.245, 0.138759),
#     (1.250, 0.142367),
#     (1.255, 0.145688),
#     (1.260, 0.148809)
# ]

x_values = [x for x, y in table]
y_values = [y for x, y in table]
x_t = 1.3463
# x_t = 1.2273
# x_t = 1.253
print(f'N(x) = {n(x_t, x_values, y_values)}')
