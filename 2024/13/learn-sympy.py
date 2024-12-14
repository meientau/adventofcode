from sympy import Symbol
from sympy.solvers import solve

a, b = [Symbol(v, integer=True) for v in ['a', 'b']]
print(solve([a*94+b*22-8400, a*34+b*67-5400], [a, b]))
print(solve([a*26+b*67-12748, a*66+b*21-12176], [a, b]))
