import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import halfnorm, expon

def target_pdf(x):
    return np.sqrt(2 / np.pi) * np.exp(-x**2 / 2)

def proposal_sample():
    return np.random.exponential(1)

# Maximum value of the ratio target_pdf(x) / (c * proposal_pdf(x))
# for the chosen exponential distribution (c is a scaling factor)
c = np.sqrt(2 * np.e / np.pi)

def rejection_sampling(n):
    samples = []
    while len(samples) < n:
        x = proposal_sample()
        u = np.random.uniform(0, 1)
        if u < target_pdf(x) / (c * np.exp(-x)):  
            samples.append(x)
    return np.array(samples)


n_samples = 10000
random_numbers = rejection_sampling(n_samples)


plt.hist(random_numbers, bins=50, density=True, alpha=0.6, color='g', label='10000 Random Numbers')


x = np.linspace(0, np.max(random_numbers), 1000)
pdf = target_pdf(x)

plt.plot(x, pdf, 'r-', lw=2, label='Given PDF')
plt.title('Density Histogram of Random Numbers distributed according to given Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
