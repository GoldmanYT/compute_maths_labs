from functools import reduce


def product(sequence):
    return reduce(lambda x, y: x * y, sequence, 1)


def l(
        x_: float,
        x: list[float],
        y: list[float]
) -> float:
    n = len(x)
    return sum(
        y[i] * product(
            (x_ - x[j]) / (x[i] - x[j])
            for j in range(n)
            if j != i
        )
        for i in range(n)
    )


table = [
    (0.68, 0.80866),
    (0.73, 0.89492),
    (0.80, 1.02964),
    (0.88, 1.20966),
    (0.93, 1.34087),
    (0.99, 1.52368),
]

x_values = [x for x, y in table]
y_values = [y for x, y in table]
x_t = 0.774

print(f'L(x) = {l(x_t, x_values, y_values)}')
