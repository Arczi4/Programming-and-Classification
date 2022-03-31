import numpy as np
import itertools
s = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
N = 27

l = np.array(list(itertools.product(*s)))
vec_len = [np.linalg.norm(x) for x in l]

p = 1/N
ev = 0
for i in range(N):
    ev += vec_len[i] * p
print(f"Expected value = {ev}")

v = np.var(np.array(vec_len))
print(f"var = {v}")

