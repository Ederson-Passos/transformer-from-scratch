import numpy as np
import torch as th

q = [1.0, 2.0, 3.0]
k = np.multiply(q, 2)
q_t = np.transpose(q)

print(np.multiply(q_t, k))