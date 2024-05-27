import numpy as np
import scipy.stats as stats

observed_counts_1 = np.array([1, 4, 10, 10, 13, 20, 18, 18, 11, 13, 14])
observed_counts_2 = np.array([3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5])

total_1 = sum(observed_counts_1)
total_2 = sum(observed_counts_2)

probabilities = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36


expected_counts_1 = total_1 * probabilities
expected_counts_2 = total_2 * probabilities

chi_squared_1 = np.sum((observed_counts_1 - expected_counts_1)**2 / expected_counts_1)
chi_squared_2 = np.sum((observed_counts_2 - expected_counts_2)**2 / expected_counts_2)

degrees_of_freedom = len(probabilities) - 1

critical_value = stats.chi2.ppf(0.95, degrees_of_freedom)

def label_randomness(chi_squared, critical_value):
    if chi_squared > critical_value:
        return "not sufficiently random"
    elif chi_squared > critical_value * 0.9:
        return "suspect"
    elif chi_squared > critical_value * 0.8:
        return "almost suspect"
    else:
        return "sufficiently random"

result_1 = label_randomness(chi_squared_1, critical_value)
result_2 = label_randomness(chi_squared_2, critical_value)

print("First Run Chi-Squared:", chi_squared_1, "Result:", result_1)
print("Second Run Chi-Squared:", chi_squared_2, "Result:", result_2)


