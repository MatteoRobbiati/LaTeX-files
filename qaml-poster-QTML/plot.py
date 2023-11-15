import numpy as np
import matplotlib.pyplot as plt

s = np.random.randn(100000)

plt.figure(figsize=(4,4))
plt.hist(s, density=True, histtype="step", color="royalblue", lw=2)
plt.savefig("figures/cdf.png")