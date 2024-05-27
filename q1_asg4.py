import matplotlib.pyplot as plt
import numpy as np
import time

def linear_congruential_generator(seed, a, c, m, n):
    random_numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        random_numbers.append(x / m)
    return random_numbers


start_time = time.perf_counter()
seed = 12345
a = 1103515245
c = 12345
m = 2**31 - 1
n = 10000


random_numbers = linear_congruential_generator(seed, a, c, m, n)
end_time = time.perf_counter()

plt.hist(random_numbers, bins=20, density=True, alpha=0.6, color='g', label='Histogram of Generated Numbers', edgecolor='black', linewidth=1.2, rwidth=0.8)
time_taken = end_time - start_time
print(f"Time taken to generate 10000 random numbers using LCG method: {time_taken} seconds")

x = np.linspace(0, 1, 100)
plt.plot(x, np.ones_like(x), 'r--', label='Uniform PDF')

plt.xlabel('Random Numbers')
plt.ylabel('Density')
plt.title('Density Histogram of Generated Random Numbers')
plt.legend()
plt.show()
