# Megan Ellis Protocol - Simulation v1.0
# Dual-pattern orthogonal neuromodulation
# Vagus = Reverse Fibonacci (gaps get SHORTER)
# Pelvic = Forward Fibonacci (gaps get LONGER)

import matplotlib.pyplot as plt
import numpy as np

# Patterns - inter-pulse intervals in ms (example units)
vagus_reverse = [13, 8, 5, 3, 2, 1, 1]   # tightening
pelvic_forward = [1, 1, 2, 3, 5, 8, 13]  # stretching

def pulses_from_gaps(gaps):
    times = [0]
    for g in gaps:
        times.append(times[-1] + g)
    return times

vagus_times = pulses_from_gaps(vagus_reverse)
pelvic_times = pulses_from_gaps(pelvic_forward)

print("Vagus (reverse) pulse times:", vagus_times)
print("Pelvic (forward) pulse times:", pelvic_times)

# Simple orthogonality check - correlation of gap patterns
corr = np.corrcoef(vagus_reverse, pelvic_forward)[0, 1]
print(f"Correlation of gap patterns: {corr:.3f}")
print("Near -1 = opposite patterns = good, they stay separable")

# Plot
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.stem(vagus_times, [1]*len(vagus_times), basefmt=" ")
plt.title("Vagus - Reverse Fibonacci\nGaps get SHORTER")
plt.xlabel("Time")
plt.ylabel("Pulse")
plt.ylim(0, 1.5)

plt.subplot(1, 2, 2)
plt.stem(pelvic_times, [1]*len(pelvic_times), basefmt=" ")
plt.title("Pelvic - Forward Fibonacci\nGaps get LONGER")
plt.xlabel("Time")
plt.ylabel("Pulse")
plt.ylim(0, 1.5)

plt.tight_layout()
plt.savefig("figure1.png")
plt.show()
print("Saved figure1.png")
