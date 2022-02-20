# Divided differences

This short python script is used to calculate the divided differences of an exponential function and thereby certain phase values. The procedure is to be used as a subroutine in a quantum algorithm to simulate Hamiltonians. The calculations are for a very specific two-level quantum system exhibiting Rabi oscillations. The energy differences (input) have been pre-calculated for different eigenstates and `q` values. 

## References
- Quantum Algorithm for Time-Dependent Hamiltonian Simulation by Permutation Expansion ([here](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.030342))
- High Accuracy Quadrature Formulas from Divided Differences with Repeated Arguments ([here](https://www.ams.org/journals/mcom/1956-10-054/S0025-5718-1956-0081551-0/S0025-5718-1956-0081551-0.pdf))

## How to run
`python3 divided_diff.py`

## Output
```
z =  0
q =  1
[x1, . . . xq, 0] =  [(-0-2j), 0]
theta + phi =  5.98807
theta - phi =  5.19201

z =  0
q =  2
[x1, . . . xq, 0] =  [0, 2j, 0]
theta + phi =  0.78343
theta - phi =  0.13403

z =  0
q =  3
[x1, . . . xq, 0] =  [(-0-2j), 0, (-0-2j), 0]
theta + phi =  5.8986
theta - phi =  5.28148

z =  0
q =  4
[x1, . . . xq, 0] =  [0, 2j, 0, 2j, 0]
theta + phi =  0.82954
theta - phi =  0.27744

z =  1
q =  1
[x1, . . . xq, 0] =  [2j, 0]
theta + phi =  1.09118
theta - phi =  0.29512

z =  1
q =  2
[x1, . . . xq, 0] =  [0, (-0-2j), 0]
theta + phi =  6.14915
theta - phi =  5.49975

z =  1
q =  3
[x1, . . . xq, 0] =  [2j, 0, 2j, 0]
theta + phi =  1.00171
theta - phi =  0.38459

z =  1
q =  4
[x1, . . . xq, 0] =  [0, (-0-2j), 0, (-0-2j), 0]
theta + phi =  6.00575
theta - phi =  5.45365
```
