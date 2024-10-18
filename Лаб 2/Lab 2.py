from math import inf


A1 = [[0.41, -0.17, 0.01],
      [0.17, 0.76, 0],
      [0, -0.005, 0.925]]
B1 = [0.69, -0.28, -0.025]
'''
A1 = [[0.24, -0.05, -0.24],
      [-0.22, 0.09, -0.44],
      [0.13, -0.02, 0.42]]
B1 = [0.19, 0.97, -0.14]
'''
X = list(B1)
N = len(X)
eps = 1e-4
prev = [inf] * N
k = 0
print('N\tx1\tx2\tx3')
while max(abs(x0 - x) for x0, x in zip(prev, X)) >= eps:
    prev = list(X)
    for i in range(N):
        X[i] = sum(A1[i][j] * X[j] for j in range(N)) + B1[i]
    print(k, '\t'.join(f'{x:.4f}' for x in X), sep='\t')
    k += 1
print('\t'.join(f'x{i}' for i in range(1, N + 1)))
print('\t'.join(f'{x:.3f}' for x in X), sep='\t')
