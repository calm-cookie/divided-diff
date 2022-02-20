# Divided Differences
import numpy as np

# Function: exp(xln(2))
def divided_diff(xs):
    xs = np.sort_complex(xs)
    if len(xs) == 1:
        return np.exp(np.log(2) * xs[0])
    
    if len(xs) == 2 and (xs[0] == xs[1]):
        return np.log(2) * np.exp(np.log(2) * xs[0])
    
    if len(xs) == 3 and (xs[0] == xs[1] == xs[2]):
        return 0.5 * np.log(2) * np.log(2) * np.exp(np.log(2) * xs[0])
    
    return (divided_diff(xs[:-1]) - divided_diff(xs[1:])) / (xs[0] - xs[-1])

# Inputs: Energy Differences
inputs = [
    # z = 0
    [-2j, 0],
    [0, 2j, 0],
    [-2j, 0, -2j, 0],
    [0, 2j, 0, 2j, 0],
    # z = 1
    [2j, 0],
    [0, -2j, 0],
    [2j, 0, 2j, 0],
    [0, -2j, 0, -2j, 0],
    ]

count = 0
for ip in inputs:

    if count < 4:
        print("z = 0")
    else:
        print("z = 1")
    count += 1
    
    q = len(ip) - 1
    print("q = ", q)
    print("[x1, . . . xq, 0] = ", ip)
    
    denom = ((np.log(2))**q) / np.math.factorial(q)
    div_diff = divided_diff(ip)
    result = div_diff / denom
    
    theta = np.angle(result)
    phi = np.arccos(np.absolute(result))
    
    # Convert theta from (-pi, pi] to [0, 2pi)
    if theta < 0:
        theta = 2*np.pi + theta
    
    sum = (theta + phi) % (2*np.pi)
    diff = (theta - phi) % (2*np.pi)
    
    if diff < 0:
        diff =  2*np.pi + diff
    
    # --- Code to find the phases as multiples of a certain fraction of pi ---
    # bits = 4
    # sum = sum / (2 * np.pi / (2**bits))
    # diff = diff / (2 * np.pi / (2**bits))

    sum = round(sum, 5)
    diff = round(diff, 5)
    print("theta + phi = ", sum, "\ntheta - phi = ", diff, "\n")