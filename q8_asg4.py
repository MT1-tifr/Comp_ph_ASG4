import numpy as np

def monte_carlo_unit_circle(num_samples):
    count_inside_circle = 0
    
    for _ in range(num_samples):
        x, y = np.random.uniform(-1, 1, 2)
        if x**2 + y**2 <= 1:
            count_inside_circle += 1
    
    area_estimate = 4 * (count_inside_circle / num_samples)
    return area_estimate

def monte_carlo_unit_sphere_10d(num_samples):
    count_inside_sphere = 0
    
    for _ in range(num_samples):
        point = np.random.uniform(-1, 1, 10)
        if np.sum(point**2) <= 1:
            count_inside_sphere += 1
    
    volume_estimate = 2**10 * (count_inside_sphere / num_samples)
    return volume_estimate

num_samples = 1000000

area_unit_circle = monte_carlo_unit_circle(num_samples)
print(f"Estimated area of the unit circle: {area_unit_circle}")

volume_unit_sphere_10d = monte_carlo_unit_sphere_10d(num_samples)
print(f"Estimated volume of the 10-dimensional unit sphere: {volume_unit_sphere_10d}")
