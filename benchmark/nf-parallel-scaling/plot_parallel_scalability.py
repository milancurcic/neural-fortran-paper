#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

elapsed = np.zeros((5, 9))
pe = np.zeros((9))

cores = np.array([1, 2, 3, 4, 5, 6, 8, 10, 12])

for i in range(5):
    data = [line.strip() for line in 
        open('run' + str(i + 1) + '.txt').readlines()]
    for n, line in enumerate(data):
        line = line.split()
        elapsed[i,n] = float(line[1])

elapsed_mean = np.mean(elapsed, axis=0)
elapsed_std = np.std(elapsed, axis=0)
pe = elapsed_mean[0] / (cores * elapsed_mean)

for n, core in enumerate(cores):
    print(core, '%5.3f' % elapsed_mean[n], '%5.3f' % elapsed_std[n], '%5.3f' % pe[n])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.tick_params(which='both', labelsize=16)
plt.plot(cores, elapsed_mean, 'k-', marker='.', ms=12)
plt.grid()
plt.xlabel('Number of cores', fontsize=16)
plt.ylabel('Elapsed time (s)', fontsize=16)
plt.savefig('nf-parallel-elapsed.png', dpi=300)
plt.close(fig)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.tick_params(which='both', labelsize=16)
plt.plot(cores, pe, 'k-', marker='.', ms=12)
plt.grid()
plt.xlabel('Number of cores', fontsize=16)
plt.ylabel('Parallel efficiency', fontsize=16)
plt.savefig('nf-parallel-efficiency.png', dpi=300)
plt.close(fig)
