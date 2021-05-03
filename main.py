# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 03/05/2021
"""
from Bucket import Bucket
from Radix import Radix
from Shell import Shell

# Driver Code
x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

buck = Bucket()
rad = Radix(x)

copy_x = x
shel = Shell(copy_x)

print()
print("Ordenado por Bucket Sort")
vetor_buck = buck.run(x)
for i in range(len(vetor_buck)):
    print(vetor_buck[i], end=" ")
print()


print()
print("Ordenado por Radix Sort")
for i in range(len(x)):
    print(x[i], end=" ")
print()


print()
print("Ordenado por Shell Sort")
for i in range(len(copy_x)):
    print(copy_x[i], end=" ")
print()