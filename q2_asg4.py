import numpy as np
import matplotlib.pyplot as plt
import time


start_time = time.perf_counter()
random_numbers = np.random.rand(10000)
end_time = time.perf_counter()
time_taken = end_time - start_time
print("Time taken to generate 10000 random numbers using np.random.rand():", time_taken, "seconds")


plt.hist(random_numbers, bins=20, density=True, alpha=0.6, color='g', label='Histogram of Generated Numbers using numpy.random.rand()', edgecolor='black', linewidth=1.2, rwidth=0.8)


x = np.linspace(0, 1, 100)
plt.plot(x, np.ones_like(x), 'r--', label='Uniform PDF')

plt.xlabel('Random Numbers')
plt.ylabel('Density')
plt.title('Density Histogram of Generated Random Numbers')
plt.legend()
plt.show()
