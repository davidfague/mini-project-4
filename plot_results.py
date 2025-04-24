import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("times.csv", skipinitialspace=True)
print(df.head())

# Plotting
fig, ax = plt.subplots()
for module, group in df.groupby('module'):
    ax.plot(group['n'], group['time (ms)'], marker='o', label=module)

# Update axis scales and labels
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Upper Bound for Sieve (n)', fontsize=12)
ax.set_ylabel('Execution Time (ms)', fontsize=12)
ax.set_title('Performance of Sieve of Eratosthenes on Different Systems', fontsize=14)
ax.legend(title="System")
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Save and show plot
plt.tight_layout()
fig.savefig('sieve_performance.png')
plt.show()
