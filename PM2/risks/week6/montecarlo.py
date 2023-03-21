import powerlaw
import numpy as np
import matplotlib.pyplot as plt

# Set the scaling exponent and minimum value
alpha = 6.16
xmin = 1.19

# Create a power-law distribution object
pl = powerlaw.Power_Law(xmin=xmin, parameters=[alpha], discrete=False)

# Generate N random samples from the distribution
size = 100000
samples = pl.generate_random(size)

print(samples)

# Plot the distribution of the samples
fig, ax = plt.subplots()
# count the number of data in each bin
ax.hist(samples, bins=50, density=False, alpha=0.5)
ax.set_xlabel('Value (Gigabytes)')
ax.set_ylabel('Frequency')
ax.set_title(f'Power-law distribution ({size} samples)')
plt.show()

# Calculate the average and standard deviation of the samples
avg = np.mean(samples)
std_dev = np.std(samples)

print("Average: ", avg)
print("Standard deviation: ", std_dev)

mx = 1.5
count = 0
for s in samples:
    if s > 1.5:
        count += 1
print(f"Greater than {mx}: {count}")

q75, q25 = np.percentile(samples, [75 ,25])
iqr = q75 - q25

print("Interquartile range: ", iqr)
