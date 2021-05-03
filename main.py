# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 03/05/2021
"""
from Bucket import Bucket
from Radix import Radix

# Driver Code
x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

buck = Bucket()
rad = Radix(x)

print("Ordenado por Bucket Sort")
print(buck.run(x))

print()

print("Ordenado por Radix Sort")
for i in range(len(x)):
    print(x[i], end=" ")

# This code is contributed by
# Oneil Hsiao
