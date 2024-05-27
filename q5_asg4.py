import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def box_muller(n):
    u1 = np.random.rand(n//2)
    u2 = np.random.rand(n//2)
    z0 = np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * np.pi * u2)
    z1 = np.sqrt(-2.0 * np.log(u1)) * np.sin(2.0 * np.pi * u2)
    return np.concatenate((z0, z1))


n = 10000
gaussian_numbers = box_muller(n)

plt.hist(gaussian_numbers, bins=50, density=True, alpha=0.6, color='g', label='10000 Random Numbers distributed according to Gaussian distribution')

mean = 0
std_dev = 1

x = np.linspace(min(gaussian_numbers), max(gaussian_numbers), 1000)
pdf = norm.pdf(x, mean, std_dev)

plt.plot(x, pdf, 'r-', lw=2, label='Gaussian PDF')
plt.title('Density Histogram of Random Numbers and Theoretical Gaussian PDF')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
