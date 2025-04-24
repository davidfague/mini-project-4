import pandas as pd
import matplotlib.pyplot as plt

# Data setup
# data = {
#     'module': ['microbit', 'pc_serial', 'pc_serial', 'pc_parallel', 'pc_parallel', 'fabric_parallel', 'fabric_serial'],
#     'time_ms': [592, 552, 6631, 10136, 376070, 14476, 14670],
#     'n': [20000, 10_000_000, 100_000_000, 10_000_000, 100_000_000, 100_000_000, 100_000_000]
# }

df = pd.read_csv("times.csv", skipinitialspace=True)
print(df.head())

# df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots()
for module, group in df.groupby('module'):
    ax.plot(group['n'], group['time (ms)'], marker='o', label=module)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Number of Simulations (n)')
ax.set_ylabel('Time (ms)')
ax.set_title('Simulation Time vs Number of Simulations')
ax.legend()
plt.tight_layout()
print(fig)
fig.savefig('time.png')